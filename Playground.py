# encoding=utf-8
import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))

# 使用jieba.posseg分词，可以查看分词的词性
import jieba.posseg as pseg
#查看词性
words = pseg.cut("我爱北京天安门")
for word, flag in words:
    print('%s %s' % (word, flag))

# 载入词典
# 添加自定义专业词汇
test_sent = (
"李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
"例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
"「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
)

jieba.load_userdict("userdict.txt")  #从文件中添加。每行为一个词：词语 词频 词性

jieba.add_word('石墨烯')  #直接添加词汇
jieba.add_word('凱特琳')  #直接添加词汇
jieba.del_word('自定义词') #直接删除词汇

words = jieba.cut(test_sent)
print('，'.join(words))

# 使用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来。
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
jieba.suggest_freq(('中', '将'), True)   #true若可以就将单词分开，false若可以就将单词合并
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
jieba.suggest_freq('台中', True)
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))

# 基于 TF-IDF 算法的关键词抽取
from jieba import analyse
s = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
for x, w in analyse.extract_tags(s, withWeight=True):
    # sentence：待提取文本
    # topK：数量
    # withWeight：是否一并返回关键词权重值
    # allowPOS：仅包括指定词性的词，默认值为空，即不筛选
    print('%s %s' % (x, w))

# 基于 TextRank 算法的关键词抽取
for x, w in jieba.analyse.textrank(s, withWeight=True):
    print('%s %s' % (x, w))

# 将待抽取关键词的文本进行分词
result = jieba.tokenize(u'永和服装饰品有限公司')   #mode='search' 为搜索模式
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
