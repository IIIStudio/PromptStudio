#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将 默认标签.csv 转换为 OHAO AI Prompt Studio.json 格式
只使用前4列：标签名,标签值,一级分类,二级分类
"""

import csv
import json
from collections import defaultdict


def csv_to_json(csv_file_path, output_json_path):
    """
    将 CSV 文件转换为 JSON 格式

    CSV 格式: 标签名,标签值,一级分类,二级分类,三级分类,四级分类
    JSON 格式: { "common": { "一级分类": { "groups": { "二级分类": [{"text": "标签值", "lang_zh": "标签名", "pinned": true}] } } } }
    """

    # 读取 CSV 文件
    data = []
    with open(csv_file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        # 获取实际的列名并打印
        fieldnames = reader.fieldnames
        print(f"CSV 列名: {fieldnames}")

        for row in reader:
            data.append(row)

    # 构建分类结构
    common_data = {}

    for row in data:
        # 获取各字段（只使用前4列）
        tag_name = row['标签名'].strip()
        tag_value = row['标签值'].strip()
        level1 = row['一级分类'].strip()
        level2 = row['二级分类'].strip()

        # 跳过空行
        if not tag_name or not tag_value:
            continue

        # 确定分类和小分类的层级
        if not level1:
            # 如果没有一级分类，跳过
            continue

        # 创建标签对象
        tag = {
            "text": tag_value,
            "lang_zh": tag_name,
            "pinned": True
        }

        # 确定分类键名（使用一级分类）
        category_key = level1

        # 确定小分类键名（使用二级分类，如果没有则为"默认"）
        sub_category = level2 if level2 else "默认"

        # 初始化分类
        if category_key not in common_data:
            common_data[category_key] = {"groups": {}}

        # 初始化小分类
        if sub_category not in common_data[category_key]["groups"]:
            common_data[category_key]["groups"][sub_category] = []

        # 添加标签
        common_data[category_key]["groups"][sub_category].append(tag)

    # 构建完整的 JSON 结构
    output_data = {
        "common": common_data,
        "history": [],
        "menus": []
    }

    # 写入 JSON 文件
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"转换完成！")
    print(f"输入文件: {csv_file_path}")
    print(f"输出文件: {output_json_path}")
    print(f"共处理 {len(data)} 条记录")
    print(f"生成 {len(common_data)} 个一级分类")

    # 统计每个分类下的标签数量
    for cat_key, cat_value in common_data.items():
        total_tags = sum(len(tags) for tags in cat_value["groups"].values())
        print(f"  - {cat_key}: {len(cat_value['groups'])} 个小分类, 共 {total_tags} 个标签")


if __name__ == "__main__":
    # 文件路径 - 使用绝对路径
    csv_file = "/workspace/Excel/默认标签.csv"
    output_json = "/workspace/Excel/OHAO AI Prompt Studio.json"

    # 执行转换
    csv_to_json(csv_file, output_json)
