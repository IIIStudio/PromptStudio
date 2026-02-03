import json

# 读取 JSON 文件
with open('/workspace/Excel/OHAO AI Prompt Studio.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 收集 JSON 中所有的英文 text
json_texts = set()

def extract_texts(obj):
    if isinstance(obj, dict):
        if 'text' in obj:
            json_texts.add(obj['text'])
        for value in obj.values():
            extract_texts(value)
    elif isinstance(obj, list):
        for item in obj:
            extract_texts(item)

extract_texts(data)

print(f"JSON 中找到 {len(json_texts)} 个英文标签")

# 读取 name.txt 文件
with open('/workspace/Excel/name.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 过滤掉在 JSON 中存在的行
filtered_lines = []
removed_count = 0

for line in lines:
    line_stripped = line.strip()
    if line_stripped and '\t' in line_stripped:
        english = line_stripped.split('\t')[0]
        if english in json_texts:
            removed_count += 1
            print(f"删除: {line_stripped}")
            continue
    filtered_lines.append(line)

# 写回文件
with open('/workspace/Excel/name.txt', 'w', encoding='utf-8') as f:
    f.writelines(filtered_lines)

print(f"\n完成！共删除 {removed_count} 行")
