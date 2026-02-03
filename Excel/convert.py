# 读取1.txt文件
with open('/workspace/Excel/name.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 提取中文和英文
chinese = []
english = []
for line in lines:
    line = line.strip()
    if line and '\t' in line:
        parts = line.split('\t')
        english.append(parts[0])
        chinese.append(parts[1])

# 生成转换后的内容
chinese_line = '，'.join(chinese)
english_line = '，'.join(english)

# 写入文件
with open('/workspace/Excel/name.txt', 'a', encoding='utf-8') as f:
    f.write('\n' + chinese_line + '\n')
    f.write(english_line + '\n')

print("转换完成！")

