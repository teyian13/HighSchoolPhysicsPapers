import os
import re

directory = '高考备考/高考真题/2023/'

for filename in os.listdir(directory):
    if filename.endswith('.md'):
        filepath = os.path.join(directory, filename)
        
        # 打开文件并读取内容
        with open(filepath, 'r', encoding='utf-8') as md_file:
            content = md_file.read()

        # 选择填空 ____
        content = content.replace('（    ）', '$(\qquad)$')
        content = content.replace('（\n   ）', '$(\qquad)$')
        content = content.replace('（\n  ）', '$(\qquad)$')

        # 去除空格
        content = content.replace(' ', '')

        # 半角➡️全角
        content = content.replace(',', '，')
        content = content.replace(';', '；')
        content = content.replace(':', '：')
        content = content.replace(' ', '')
        content = content.replace('．', '。')
        content = content.replace('“', '"')
        content = content.replace('”', '"')
        content = content.replace('https：//', 'https://')

        # 如何替换英文的括号为中文的括号
        content = content.replace( '（','(',)
        content = content.replace( '）',')',)

        # mathpix
        content = content.replace('$$', '$')
        content = content.replace('\n$\n', '\n$$\n')
        content = content.replace('\\text{', '\\mathrm{')
        content = re.sub(r'\$([ABCD]+)\$', r'\1', content)
        content = content.replace('Ω', '\ohm')
        content = content.replace('\mathrm{/}', '/')
        content = content.replace('°', '^\\circ')

        # +空格
        keywords_for_space_addition = ['\\cdot', '\\sin', '\\sim', '\\mu', '\\geq', '\\leq', '\\Delta', '\\pi', '\\omega', '\\times', '\\rho', '\\approx', '\\rightarrow', '\\propto','\\triangle','\\angle']

        for keyword in keywords_for_space_addition:
            content = content.replace(keyword, keyword + ' ')


        # 空格
        content = content.replace('【解析】', '【解答】')
        content = content.replace('【解答】解：', '【解答】')
        content = content.replace('【解答】解', '【解答】')
        content = content.replace('#202', '# 202')
        content = content.replace('\：', '')

        # \n
        content = content.replace('\n\n', '\n')
        content = content.replace('\n\n', '\n')


        content = re.sub(r"\$.*?\$", lambda x: ' ' + x.group() + ' ', content)
        content = content.replace(' $$ ', '$$')

        # 仅在行首题号后添加空格
        # '^' 代表行首， '\d{1,2}' 匹配1到2位的数字
        content = re.sub(r'^(\d{1,2}\.)', r'\1 ', content, flags=re.MULTILINE)
        content = re.sub(r'^ \$', '$', content, flags=re.MULTILINE)
        content = re.sub(r'\$ $', '$', content, flags=re.MULTILINE)

        # 在每两道题之间添加空行
        # 注意，此处的 "\n" 其实是为了匹配上一题的结束，所以我们要保留它，即替换为 "\n\n" （两个换行符）
        content = re.sub(r'(\n)(\d{1,2}\. )', r'\n\1\2', content)

        # 把处理后的字符串写回文件
        with open(filepath, 'w', encoding='utf-8') as md_file:
            md_file.write(content)