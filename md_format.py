import os
import re

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
        content = content.replace('（　　）', '$（\qquad）$')
        content = content.replace('（\n  ）', '$（\qquad）$')
        content = content.replace('（  ）', '$（\qquad）$')
        content = content.replace('left（', 'left(')
        content = content.replace('right）', 'right)')
        content = content.replace('[          ]{.underline}', '____')
        content = content.replace('$$', '$')


        # +空格
        content = content.replace('\cdot', '\cdot ')
        content = content.replace('\sin', '\sin ')
        content = content.replace('\mu', '\mu ')
        content = content.replace('\geq', '\geq ')
        content = content.replace('\Delta', '\Delta ')
        content = content.replace('\pi', '\pi ')
        content = content.replace('\omega', '\omega ')
        content = content.replace('#####', '##### ')

        # text mathrm
        content = re.sub(r'\\text\{([^a-zA-Z0-9\u4E00-\u9FA5\s]+)\}', r'\\mathrm{\1}', content)
        # 把处理后的字符串写回文件
        with open(filepath, 'w', encoding='utf-8') as md_file:
            md_file.write(content)