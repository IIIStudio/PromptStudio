import json

# 读取 JSON 文件
with open('/workspace/Excel/OHAO AI Prompt Studio.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 收集所有的 text 和 lang_zh
text_dict = {}

def extract_texts(obj):
    if isinstance(obj, dict):
        if 'text' in obj:
            text = obj['text']
            lang_zh = obj.get('lang_zh', '')
            if text in text_dict:
                text_dict[text].append(lang_zh)
            else:
                text_dict[text] = [lang_zh]
        for value in obj.values():
            extract_texts(value)
    elif isinstance(obj, list):
        for item in obj:
            extract_texts(item)

extract_texts(data)

# 找出重复的 text
duplicates = {}
for text, lang_zh_list in text_dict.items():
    if len(lang_zh_list) > 1:
        duplicates[text] = lang_zh_list

print(f"找到 {len(duplicates)} 个重复的 text")

# 写入 name.txt
with open('/workspace/Excel/name.txt', 'a', encoding='utf-8') as f:
    f.write('\n\n=== 重复的 text ===\n')
    for text, lang_zh_list in duplicates.items():
        for lang_zh in lang_zh_list:
            f.write(f"{text}\t{lang_zh}\n")
        f.write('\n')

print("已写入 name.txt")
