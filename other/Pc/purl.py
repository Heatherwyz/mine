import urllib.request
import re
url="https://www.52pojie.cn/forum-24-1.html"#爬的地址
page=urllib.request.urlopen(url).read()#获取到该地址的所有内容
page=page.decode('gbk') #转码
#正则表达式
zz = r'<a href="(thread-.+?)".+? class="s xst">(.+?)</a>'
#匹配所有符合规则的内容存到html集合里面
html=re.findall(zz,page,re.S)#re.S表示.可以代表\n
i = 0
for line in html:
    line = html[i]
    #链接
    m1 = "https://www.52pojie.cn/"+line[0]
    #标题
    m2 = line[1]
    #打印标题和链接
    print(m2+" "+m1)
    i = i + 1