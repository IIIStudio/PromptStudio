#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

csv_file = "/workspace/Excel/默认标签.csv"

# 测试不同编码
for encoding in ['utf-8', 'utf-8-sig', 'gbk', 'gb2312']:
    try:
        with open(csv_file, 'r', encoding=encoding) as f:
            reader = csv.reader(f)
            header = next(reader)
            print(f"编码 {encoding}: {header}")
            break
    except Exception as e:
        print(f"编码 {encoding} 失败: {e}")
