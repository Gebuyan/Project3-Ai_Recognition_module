# Project3-违规信息识别模块

## 项目简介
本项目属于课题3（基于智能感知与多方门限签名的区块链分布式监管决策体系）的违规信息识别模块。主要工作是基于深度学习训练两个能够对链上信息进行识别的AI模型，并通过
flask框架实现模型推理接口，最终通过docker部署到云端。

## 项目结构
```
.
├── chain_violation(Deprecated)
├── gun_detection                     #(违规图片识别)
│   ├── app.py                # 启动文件
│   ├── Images                # 部分数据集
│   ├── static                # 静态文件存储
│   ├── templates             # 模板文件
│   ├── Object_Detection.py   # 模型训练
│   ├── ssh.py                # 数据库连接
│   ├── Dockerfile            # docker镜像创建
│   └── requirements.txt      # 依赖列表 
├── toxic_comment_identification       #(违规评论识别)
│   ├── app.py                # 启动文件
│   ├── txt_process           # 部分数据集
│   ├── static                # 静态文件存储
│   ├── templates             # 模板文件
│   ├── LSTM.py               # 模型推理
│   ├── LSTM_train.py         # 模型训练
│   ├── ssh.py                # 数据库连接
│   ├── Dockerfile            # docker镜像创建
│   └── requirements.txt      # 依赖列表 
└── README                          
```

## 特性
- 使用 Tensorflow 训练违规评论识别模型。
- 使用 Pytorch 训练违规图片识别模型。
- 使用 Flask 构建高效的Web API。
- 使用 MySQL 数据库进行数据存储。

## 快速开始

### 克隆仓库

```bash
git clone https://github.com/Gebuyan/Project3-Ai_Recognition_module.git
cd Project3-Ai_Recognition_module
cd Project
```

### 创建虚拟环境及安装依赖

```conda
conda create --name gun_detection python=3.9
conda activate gun_detection
conda install pip
pip install -r requirements.txt



conda create --name toxic_comment_identification python=3.9
conda activate toxic_comment_identification
conda install pip
pip install -r requirements.txt
```

### 启动
```bash
cd gun_detection
set FLASK_APP=app.py
flask run


cd  toxic_comment_identification
set FLASK_APP=app.py
flask run
```

