#!/usr/bin/env python
import os,requests
ROOT = os.path.dirname(__file__)
os.chdir(ROOT)
theme_fn=os.path.join(ROOT,'theme.html')
with open(theme_fn) as theme_f: theme=theme_f.read()
#r = requests.get('https://raw.githubusercontent.com/ComradOrg/Comrad/master/README.md')
# with open('/home/ryan/comrad/code/README.md','w') as of:
    # of.write(r.text)

os.system('pandoc /home/ryan/comrad/code/README.md > content.html')
# os.system('pandoc README.md > content.html')

with open('content.html') as content_f,open('index.html','w') as of:
    content = content_f.read() #.replace('\n  * ','</li>\n<li>')
    content=content.replace('&lt;','<').replace('&gt;','>')
    content=content.replace('comrad/app/assets','assets')
    content=content.replace('<h1 id="comrad">Comrad</h1>','')
    content=content.replace('href="comrad/','href="https://github.com/ComradOrg/Comrad/tree/master/comrad/')
    total = theme.replace('[[CONTENT]]',content)
    of.write(total)
# os.remove('content.html')
