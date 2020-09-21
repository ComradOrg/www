#!/usr/bin/env python
import os,requests
ROOT = os.path.dirname(__file__)
os.chdir(ROOT)
theme_fn=os.path.join(ROOT,'theme.html')
with open(theme_fn) as theme_f: theme=theme_f.read()
r = requests.get('https://raw.githubusercontent.com/Komrade/Komrade/master/README.md')
with open('README-Komrade.md','w') as of:
    of.write(r.text)

os.system('pandoc README-Komrade.md > content.html')

with open('content.html') as content_f,open('index.html','w') as of:
    content = content_f.read() #.replace('\n  * ','</li>\n<li>')
    content=content.replace('&lt;','<').replace('&gt;','>')
    content=content.replace('komrade/app/assets','assets')
    content=content.replace('href="komrade/','href="https://github.com/Komrade/Komrade/tree/master/komrade/')
    total = theme.replace('[[CONTENT]]',content)
    of.write(total)
# os.remove('content.html')
