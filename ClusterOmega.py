import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式: 不考虑歧义，这个模式会将所有的可以成词的词语都扫描出来，因而速度会非常快。

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式: 它会试图将句子最精确的切开，适合文本分析。

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
# 搜索引擎模式: 该模式是在精确模式的基础上，对长词再进行切分，提高召回率，适用于搜索引擎分词。
print(", ".join(seg_list))

# Hidden Markov Mode
# 对于未登录词，采用了基于汉字成词能力的 HMM 模型，使用了 Viterbi 算法
seg_list = jieba.cut("他来到了网易杭研大厦",HMM=False)
print("HMM为False：" + "/ ".join(seg_list))

seg_list = jieba.cut("他来到了网易杭研大厦",HMM=True)
print("HMM为True：" + "/ ".join(seg_list))

