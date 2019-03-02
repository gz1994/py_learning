#!/usr/bin/env python
# -*- coding: utf-8 -*-
count = 0
def hanoi(n, src, dst, mid): #n代表圆盘个数，src代表第一个塔，
                            # dst代表目标塔，mid代表中间塔
    global count
    if n == 1 :
        print("{}:{}->{}".format(1,src,dst))
        count += 1
    else :
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n-1, mid, dst, src)
hanoi(3, "A", "C","B")#测试程序
print(count)

