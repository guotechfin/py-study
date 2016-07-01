#!/bin/env python
# -*- coding:utf8 -*-


def load_ticket():
    code_list = list()
    with open("common/s50.txt", 'r') as f:
        for i in f.readlines():
            code_list.append(i.strip())
    return code_list
