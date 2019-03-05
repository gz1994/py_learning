#!/usr/bin/env python
# -*- coding: utf-8 -*-
#CalThreeKingdoms.py        统计三国演义中出现最多的人名
import jieba
txt = open("threekingdoms.txt", "r", encoding="utf-8").read()
excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此", "商议", "如何"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        reword = "孔明"
    elif word == "关公" or word == "云长":
        reword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        reword = "刘备"
    elif word == "孟德" or word == "丞相":
        reword = "曹操"
    else:
        reword = word
    counts[reword] = counts.get(reword, 0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
