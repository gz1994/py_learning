#!/usr/bin/env python
# -*- coding: utf-8 -*-
#CalHamlet.py
def getText():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()       #把文章内的大写字母变成小写
    for ch in '!"#$%&*()+,./:;<=>?@[\\]^_`~·{|}':
        txt = txt.replace(ch," ")       #清除特殊字符并用空格代替
    return txt

hamletTxt = getText()
words = hamletTxt.split()           #切片处理
counts = {}                         #建立一个空字典
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())        #字典类型转换成列表类型
items.sort(key=lambda x:x[1],reverse=True)#按照值进行排序，默认从小到大
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
