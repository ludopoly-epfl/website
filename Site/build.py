#ORDER : cfr, cen, pfr, pen

import os
import shutil
from glob import glob

#READ TEXT FILE

file = open("text.txt","r")
lines = file.readlines()

for i in range(len(lines)):
    if lines[i][-1:] == "\n":
        lines[i] = lines[i][:-1]

#PARSE TEXT

cnt = 0
globa = []
page = []
pages = []
for line in lines:
    if line == "/#/#/":
        if cnt < 6:
            globa.append(page[0])
            page = []
            cnt += 1
        else:
            pages.append(page)
            page = []
    else:
        page.append(line)

navmid = len(pages)//2+len(pages)%2

navcfr = ""
navcen = ""
navfr = []
naven = []
for i in range(len(pages)):
    navcfr += '<li><a id="nav" href="./'+pages[i][0]+'.html">'+pages[i][1]+'</a></li>'
    navcen += '<li><a id="nav" href="./'+pages[i][0]+'.html">'+pages[i][2]+'</a></li>'
    if i == navmid-1 or i == len(pages)-1:
        navfr.append(navcfr)
        naven.append(navcen)
        navcfr = ""
        navcen = ""

#BASIC PAGE STRUCTURE

base0 = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script src="../../script.js"></script>
    <link rel="stylesheet" href="../style.css">
</head>
<body  onload="content();">
    <div id="navbar">
        <a id="navright" href="'''
base1 = '''
            <img id="trad" src="../../image/trad.png" alt="Translate" height="100%"></img>
        </a>
        <ul id="navleft">'''
base2p = '''
        </ul>
    </div>
    <div id="navbar2">
        <ul id="navleft">'''
base3 = '''
        </ul>
    </div>
    <div id="mainblock">
        <div id="maintitle">'''
base4 = '''
        </div>
        <div id="maintext">'''
base5 = '''
        </div>
    </div>'''
base6c = '''
    <img id="mainimage" src="../../image/logo.png" alt="Image"></img>'''

base = [
    base1+navfr[0]+navfr[1]+base3,
    base1+naven[0]+naven[1]+base3,
    base1+navfr[0]+base2p+navfr[1]+base3,
    base1+naven[0]+base2p+naven[1]+base3]

htmls = [[],[],[],[]]
for page in pages:
    htmls[0].append(base0+"../en/"+page[0]+'.html">'+base[0]+page[3]+base4+page[5]+base5+base6c)
    htmls[1].append(base0+"../fr/"+page[0]+'.html">'+base[1]+page[4]+base4+page[6]+base5+base6c)
    htmls[2].append(base0+"../en/"+page[0]+'.html">'+base[2]+page[3]+base4+page[5]+base5)
    htmls[3].append(base0+"../fr/"+page[0]+'.html">'+base[3]+page[4]+base4+page[6]+base5)

#END OF PAGE

end1 = '''
    <div id="bar">
        <span>'''
end2 = '''
        </span>
        <a href="'''
end3 = '''
        " target="_blank" id="barright">'''
end4 = '''
        </a>
    </div>
</body>
</html>'''

endfr = end1+globa[0]+end2+globa[4]+end3+globa[2]+end4
enden = end1+globa[1]+end2+globa[5]+end3+globa[3]+end4

#ITEMS OF A PAGE

item1 = '''
    <div id="block">
      <div id="title">'''
item2 = '''
      </div>
      <div id="text">'''
item3 = '''
      </div>
    </div>'''

for i in range(len(pages)):
    for n in range((len(pages[i])-7)//4):
        htmls[0][i] += item1+pages[i][7+n*4]+item2+pages[i][9+n*4]+item3
        htmls[1][i] += item1+pages[i][8+n*4]+item2+pages[i][10+n*4]+item3
        htmls[2][i] += item1+pages[i][7+n*4]+item2+pages[i][9+n*4]+item3
        htmls[3][i] += item1+pages[i][8+n*4]+item2+pages[i][10+n*4]+item3
    htmls[0][i] += endfr
    htmls[1][i] += enden
    htmls[2][i] += endfr
    htmls[3][i] += enden

#FILES MANAGEMENT

shutil.rmtree("c/fr")
shutil.rmtree("c/en")
shutil.rmtree("p/fr")
shutil.rmtree("p/en")

os.mkdir("c/fr")
os.mkdir("c/en")
os.mkdir("p/fr")
os.mkdir("p/en")

for i in range(len(pages)):
    final = open("c/fr/"+pages[i][0]+".html","w")
    final.write(htmls[0][i])
    final = open("c/en/"+pages[i][0]+".html","w")
    final.write(htmls[1][i])
    final = open("p/fr/"+pages[i][0]+".html","w")
    final.write(htmls[2][i])
    final = open("p/en/"+pages[i][0]+".html","w")
    final.write(htmls[3][i])

#ROOT PAGES

for f in glob("*.html"):
   os.unlink(f)

index = '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <script src="script.js"></script>
  </head>
  <body onload="start();">
  </body>
</html>'''

for i in range(len(pages)):
    if pages[i][0] == "home":
        final = open("index.html","w")
    else:
        final = open(pages[i][0]+".html","w")
    final.write(index)
