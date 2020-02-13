#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import jieba
from os import path

d = path.dirname(__file__) # 获取当前文件的dir路径
stopwords_path = 'stopwords.txt'  # 停用词表路径

text_path = 'weicheng.txt' #《围城》的文本路径
text = open(path.join(d, text_path),'r', encoding='utf8', errors='ignore').read()

def RmStopWords(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list) # 添加切分符
    f_stop = open(stopwords_path , 'r', encoding='utf8', errors='ignore')
    try:
        f_stop_text = f_stop.read()
    finally:
        f_stop.close( )
    f_stop_seg_list=f_stop_text.split('\n') # 停用词是每行一个，所以用/n分离
    for myword in liststr.split('/'):
        #对于每个切分的词都去停用词表中对比
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    return ''.join(mywordlist) #返回一个字符串

txt2 = RmStopWords(text)
text_write = '2.txt'
with open(text_write,'w', encoding="utf-8") as f:
    f.write(txt2)
    print("Success")
