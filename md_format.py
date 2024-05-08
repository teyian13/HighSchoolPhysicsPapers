import os
import re

directory = '高考备考/高考真题/2023/'

for filename in os.listdir(directory):
    if filename.endswith('.md'):
        filepath = os.path.join(directory, filename)
        # 打开文件并读取内容
        with open(filepath, 'r', encoding='utf-8') as md_file:
            content = md_file.read()

        # 去除空格
        content = content.replace(' ', '')
        # 去除选项前后$
        content = re.sub(r'(?<![^\W\d_])\$([ABCD]+)\$(?![^\W\d_])', r'\1', content)
        # 半角➡️全角
        content = content.translate(str.maketrans({
            ',': '，',
            ';': '；',
            ':': '：',
            ' ': '',
            '．': '。',
            '“': '"',
            '”': '"',
            '(': '（',
            ')': '）'
        }))

        # 如果冒号的前后都没有汉字，那么就把它改成半角的 
        content = re.sub(r'(?<![^\x00-\xff])：(?![^\x00-\xff])', ':', content)
        # 匹配全角圆括号且括号内没有中文的子串，做替换，将全角圆括号替换为半角圆括号
        content = re.sub(r'（[^一-龥]*）', lambda m: m.group(0).replace('（', '(').replace('）', ')'), content)

        # 全角➡️半角
        content = content.translate(str.maketrans({
            '１': '1',
            '２': '2',
            '３': '3',
            '４': '4',
            '５': '5'
        }))

        # mathpix
        content = content.translate(str.maketrans({
            'Ω': '\\Omega',
            '°': '^\\circ'
        }))

        # 选择填空 ____
        content = content.replace(' $($ )', '$(\qquad)$')
        content = content.replace(' ( )', '$(\qquad)$')
        content = content.replace('$(\quad)$', '$(\qquad)$')
        content = content.replace('\n$\n', '\n$$\n')
        content = content.replace('\\text{', '\\mathrm{')
        content = content.replace('\mathrm{/}', '/')
        content = content.replace('overparen', 'overset{\\frown}')

        # LaTeX公式+空格
        keywords_for_space_addition = ['\\nu','\\eta','\\cdot', '\\sin', '\\sim', '\\mu', '\\geq', '\\leq', '\\Delta', '\\pi', '\\omega', '\\times', '\\rho', '\\approx', '\\rightarrow', '\\propto','\\triangle','\\angle','\\hline']
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
        content = content.replace('；B', '；\nB')
        content = content.replace('；C', '；\nC')
        content = content.replace('；D', '；\nD')
        content = content.replace('。故选：', '。\n故选：')
        content = content.replace('；故选：', '。\n故选：')

        # $$公式前后加空格
        content = re.sub(r"\$.*?\$", lambda x: ' ' + x.group() + ' ', content)
        # 单位前加空格
        content = content.replace('mathrm{~', 'mathrm{')
        content = content.replace('mathrm{', 'mathrm{~')

        # 仅在行首题号后添加空格
        # '^' 代表行首， '\d{1,2}' 匹配1到2位的数字
        content = re.sub(r'^(\d{1,2}\.)', r'\1 ', content, flags=re.MULTILINE)
        content = re.sub(r'^ \$', '$', content, flags=re.MULTILINE)
        content = re.sub(r'\$ $', '$', content, flags=re.MULTILINE)

        # 在每两道题之间添加空行
        content = re.sub(r'(\n)(\d{1,2}\. )', r'\n\1\2', content)

        # content = re.sub(r'^\s*[\w\s]*。\s*', lambda m: m.group().replace('。', '.'), content, flags=re.M)  

        # 两个空格➡️一个空格
        content = content.replace('  ', ' ')

        # 把处理后的字符串写回文件
        with open(filepath, 'w', encoding='utf-8') as md_file:
            md_file.write(content)