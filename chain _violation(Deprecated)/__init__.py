import aiohttp
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import tensorflow as tf
import joblib
from tensorflow.keras.preprocessing.sequence import pad_sequences
from settings import labels, top_k

http: aiohttp.client.ClientSession

app = FastAPI(
    title="链上信息感知",
)

tokenizer = joblib.load('token.pkl')
model = tf.keras.models.load_model("LSTM.h5")


class Predicted(BaseModel):
    name: str
    probability: float


class QueryRes(BaseModel):
    tops: List[Predicted]
    target: float


class Text(BaseModel):
    data: str = ''


@app.post("/api/v1/recon_text", response_model=List[Predicted], responses={
    200: {
        "description": "输入需要检测的文本内容，输出可能的违规或正常类别及其概率（当前仅有敏感词一类）",
        "content": {
            "application/json": {
                "example": [
                    {"name": "敏感词", "value": 0.6},
                    {"name": "正常", "value": 0.4},
                ]
            }
        }
    }
})
async def recon_draw(text: Text = Text()):
    tex = tokenizer.texts_to_sequences([text.data])
    tex=pad_sequences(tex, maxlen=50)
    pred = model.predict(tex)[0]
    res = []
    for i in pred.argsort()[-top_k:]:
        res.append(Predicted(name=labels[i], probability=pred[i]))
    return res
