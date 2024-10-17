import pandas as pd
import numpy as np

#数据读取：
video_data = pd.read_excel('video_list.xlsx')
speech_data = pd.read_excel('speech_text.xlsx')
# video_data.info()
# speech_data.info()

#修改数据类型：
video_data['AwemeId']= video_data['AwemeId'].astype(str)
speech_data['VideoId']= speech_data['VideoId'].astype(str)
# video_data.info()
# speech_data.info()

#表连接将几个excel连接起来：
merge=pd.merge(video_data,speech_data,how='inner',left_on='AwemeId',right_on='VideoId')

#访问结果表中每一行的数据：
for i in range(len(merge)):
    # print(merge.iloc[i])
    print(merge.iloc[i]['品牌'])    
    
# 访问的数据写入word：
from datetime import datetime
from docx import Document
from docx.shared import Inches
doc= Document()
for i in range(len(merge)):
    # print(merge.iloc[i])
    print(merge.iloc[i]['品牌'])    
    
