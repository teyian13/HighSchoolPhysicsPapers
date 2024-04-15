import os

directory = '高考备考/高考真题/2021/'

for filename in os.listdir(directory):
    if filename.endswith('.md'):
        filepath = os.path.join(directory, filename)
        
        # 打开文件并读取内容
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