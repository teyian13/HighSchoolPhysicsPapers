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
        content = content.replace(':', '：')
        content = content.replace(' ', '')
        content = content.replace(' ', '')
        content = content.replace('．', '.')

        # \n
        content = content.replace('\n\n', '\n')
        content = content.replace('\n\n', '\n')
        content = content.replace('\n', '\n\n')

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
        content = content.replace('\n$\n', '\n$$\n')
        content = content.replace('\\text{', '\\mathrm{')
        content = content.replace('![]（', '![](')
        content = content.replace('.png）', '.png)')
        content = content.replace('https：//', 'https://')

        
        content = re.sub(r'\$([ABCD]+)\$', r'\1', content)

        # mathpix
        
        content = content.replace('Ω', '\ohm')

        # +空格
        content = content.replace('\cdot', '\cdot ')
        content = content.replace('\sin', '\sin ')
        content = content.replace('\mu', '\mu ')
        content = content.replace('\geq', '\geq ')
        content = content.replace('\Delta', '\Delta ')
        content = content.replace('\pi', '\pi ')
        content = content.replace('\omega', '\omega ')
        content = content.replace('#####', '##### ')
        content = content.replace('#202', '# 202')


        content = content.replace('【解析】', '【解答】')
        content = content.replace('【解答】解：', '【解答】')


        # 把处理后的字符串写回文件
        with open(filepath, 'w', encoding='utf-8') as md_file:
            md_file.write(content)