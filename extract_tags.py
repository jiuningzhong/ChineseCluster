# 基于TF-IDF的关键词提取
import sys
sys.path.append('../')
import jieba
import jieba.analyse
from optparse import OptionParser

file_name = "weicheng.txt"
topK = 10

content = open(file_name, 'rb').read()

tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)

for i in tags :
    print(i)
