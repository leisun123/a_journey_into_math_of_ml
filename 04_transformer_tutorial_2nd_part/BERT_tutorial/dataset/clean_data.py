# coding: utf-8

import pandas as pd
import numpy as np
from BERT_tutorial.Sentiment_Inference

# 导入数据
filePath = '04_transformer_tutorial_2nd_part/BERT_tutorial/dataset/dialogue_content_20200724.csv'
DataDf = pd.read_csv(filePath, encoding="utf-8", dtype=str)

print(DataDf.head())
