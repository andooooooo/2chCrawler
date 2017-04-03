import re
import time
import requests
from bs4 import BeautifulSoup,NavigableString
import urllib.request

p = re.compile('/livejupiter/[0-9]+/')
p2 = re.compile('class="res">[0-9]+')
p4 = re.compile('res=100">[^&#169]+&#169')
i = 0

#スレッドを保存する
def getth(url2):
    #スレッドget
    response2 = urllib.request.urlopen(url2)
    data = response2.read()
    response4 = requests.get(url2)
    datae = response4.text
    #beautifulsoupでスレッドタイトル取得
    soup = BeautifulSoup(data, "lxml")
    title2 = soup.find("title")
    if isinstance(title2,type(None)):
        return()
    else:
        title2=title2.text
    #partスレッドは除外する（実況スレッド対策）
    if "★" in title2:
        return()
    title2 =title2 +".html"
    with open(title2, "w")as fo:
        fo.write(datae)

while i < 1000:
    i3 = 0
    resnums3 = []
    response = requests.get("http://2ch-ranking.net/index.html?board=livejupiter")
    html = response.text
    #2chのURLすべてを抽出
    links = re.findall(p,html)
    #何レスついてるか抽出
    resnums = re.findall(p2,html)
    #スレッドのタイトルを抽出
    name = re.findall(p4,html)
    #レス数を整形して数字だけにする
    for resnum in resnums:
        resnum2 = resnum.replace("class=\"res\">","")
        resnum2 = int(resnum2)
        resnums3.append(resnum2)
    #50以下ならpass、50以上なら取得（取得したURLは一応保存）
    while i3 < len(resnums3):
        if resnums3[i3] < 50:
            i3 += 1
            continue
        else:
            url = "http://raptor.2ch.net/test/read.cgi" + links[i3]
            print(url)
            with open("urlurlurlurlurl.txt", "a")as f:
                f.write(url + "\n")
            getth(url)
        i3 += 1
    i += 1
    time.sleep(300)
