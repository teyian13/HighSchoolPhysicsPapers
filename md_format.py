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
        # 如果圆括号的前后都没有汉字，那么就把它改成半角的 
        # content = re.sub(r'(?<![^\x00-\xff])（(?![^\x00-\xff])', '(', content)
        # content = re.sub(r'(?<![^\x00-\xff])）(?![^\x00-\xff])', ')', content)
        content = re.sub(r'（[^一-龥]*）', lambda m: m.group(0).replace('（', '(').replace('）', ')'), content)

        # 全角➡️半角
        content = content.replace('１', '1')
        content = content.replace('２', '2')
        content = content.replace('３', '3')
        content = content.replace('４', '4')
        content = content.replace('５', '5')

        # 选择填空 ____
        content = content.replace('（）', '$(\qquad)$')
        content = content.replace(' $($ )', '$(\qquad)$')
        content = content.replace(' ( )', '$(\qquad)$')
        content = content.replace('（    ）', '$(\qquad)$')
        content = content.replace('（\n   ）', '$(\qquad)$')
        content = content.replace('（\n  ）', '$(\qquad)$')
        content = content.replace('$(\quad)$', '$(\qquad)$')
        # mathpix
        content = content.replace('\n$\n', '\n$$\n')
        content = content.replace('\\text{', '\\mathrm{')
        # content = re.sub(r'\$([ABCD]+)\$', r'\1', content)
        content = content.replace('Ω', '\Omega')
        content = content.replace('\mathrm{/}', '/')
        content = content.replace('°', '^\\circ')
        content = content.replace('overparen', 'overset{\\frown}')

        # +空格
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


        content = re.sub(r"\$.*?\$", lambda x: ' ' + x.group() + ' ', content)

        # 仅在行首题号后添加空格
        # '^' 代表行首， '\d{1,2}' 匹配1到2位的数字
        content = re.sub(r'^(\d{1,2}\.)', r'\1 ', content, flags=re.MULTILINE)
        content = re.sub(r'^ \$', '$', content, flags=re.MULTILINE)
        content = re.sub(r'\$ $', '$', content, flags=re.MULTILINE)

        # 在每两道题之间添加空行
        # 注意，此处的 "\n" 其实是为了匹配上一题的结束，所以我们要保留它，即替换为 "\n\n" （两个换行符）
        content = re.sub(r'(\n)(\d{1,2}\. )', r'\n\1\2', content)

        # content = re.sub(r'^\s*[\w\s]*。\s*', lambda m: m.group().replace('。', '.'), content, flags=re.M)  

        content = content.replace('.png)\nB.', '.png)B.')
        content = content.replace('.png)\nC.', '.png)C.')
        content = content.replace('.png)\nD.', '.png)D.')
        # 单位前加空格
        content = content.replace('mathrm{~', 'mathrm{')
        content = content.replace('mathrm{', 'mathrm{~')

        
        # 
        content = content.replace('试卷(等级性)', '试卷（等级性）')
        content = content.replace('试卷(选择性)', '试卷（选择性）')
        content = content.replace('试卷(甲卷)', '试卷（甲卷）')
        content = content.replace('试卷(乙卷)', '试卷（乙卷）')
        content = content.replace('试卷(新课标)', '试卷（新课标）')
        content = content.replace('  ', ' ')

        
        # 把处理后的字符串写回文件
        with open(filepath, 'w', encoding='utf-8') as md_file:
            md_file.write(content)