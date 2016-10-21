#!/bin/env python
# -*- coding:utf8 -*-


def load_ticket(path, exclude_list=[]):
    code_list = list()
    with open(path, 'r') as f:
        for i in f.readlines():
            code = i.strip()
            if code not in exclude_list:
                code_list.append(code)
    return code_list

def get_code_list():
    black_code_list = load_ticket('common/b50.txt')
    code_list = load_ticket('common/s50.txt', black_code_list)
    return code_list
