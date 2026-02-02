import json
import os
import re

# IELTS目录路径
ielts_dir = "/workspace/IELTS"

# 合并后的输出文件
output_file = os.path.join(ielts_dir, "IELTS.json")

# 存储所有单词
all_words = []

# 遍历day1到day18的文件
for day in range(1, 19):
    input_file = os.path.join(ielts_dir, f"IELTS-listening-18days-day{day}.json")
    
    if os.path.exists(input_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                all_words.extend(data)
                print(f"已读取: {input_file} ({len(data)} 个单词)")
    else:
        print(f"文件不存在: {input_file}")

# 去重（基于name字段）并转换格式
seen = set()
unique_words = []
for word in all_words:
    if isinstance(word, dict) and 'name' in word:
        if word['name'] not in seen:
            seen.add(word['name'])
            # 转换为新格式，并去掉词性标记
            trans = word['trans'][0] if word['trans'] else ""
            # 去掉词性标记（如 n. adj. v. 等）
            trans = re.sub(r'^[a-z]+\.\s*', '', trans)
            # 将分隔符统一改为 -
            trans = re.sub(r'[，：；]', '-', trans)
            new_word = {
                "en": word['name'],
                "zh": trans
            }
            unique_words.append(new_word)
    else:
        print(f"跳过无效条目: {word}")

# 写入合并后的文件
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(unique_words, f, ensure_ascii=False, indent=4)

print(f"\n合并完成！")
print(f"原始单词总数: {len(all_words)}")
print(f"去重后单词数: {len(unique_words)}")
print(f"输出文件: {output_file}")
