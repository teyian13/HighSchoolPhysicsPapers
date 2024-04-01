import os

directory = '高考备考/高考真题/2020/'
# 如何遍历一个文件夹的所有.md文件
for root, dirs, files in os.walk('directory'):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            
            # 如何打开文件并读取内容
            with open(filepath, 'r', encoding='utf-8') as md_file:
                content = md_file.read()

            # 如何替换英文的逗号和句号为中文的逗号和句号
            content = content.replace(',', '，')
            content = content.replace(';', '；')
            content = content.replace(' ', '')

            # 如何替换英文的括号为中文的括号
            content = content.replace('(', '（')
            content = content.replace(')', '）')


            # 把处理后的字符串写回文件
            with open(filepath, 'w', encoding='utf-8') as md_file:
                md_file.write(content)