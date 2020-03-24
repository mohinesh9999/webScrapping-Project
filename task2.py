def alert(x):
    l=[]
    for i in range(len(x)):
        if(float(x[i])<=-2):
            l.append(i)
    return l
import time
import requests
from bs4 import BeautifulSoup
def task():
    url="https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9"


    r=requests.get(url)
    htmlcontent=r.content

    soup = BeautifulSoup(htmlcontent, 'html.parser')


    e=soup.find('tr',class_="bggry")
    e=soup.find_all('th',class_="brdrgtgry")
    # print(e)
    d=dict()
    t=0
    l=[]
    for i in e:
        # print(i.get_text())
        d.setdefault(i.get_text(),[])
        l.append(i.get_text())
        t+=1
    # print(d)
    e=soup.find_all('tr')
    # print(e,len(e))
    t1=0
    for i in range(len(e)):
        t1=0
        if(i!=0):
            x=e[i].find_all('td',class_="brdrgtgry")
            for j in x:
                if t1==0:
                    # print(j.get_text()[:j.get_text().index('\n')])
                    d[l[t1]].append(j.get_text()[:j.get_text().index('\n')])
                else:
                    d[l[t1]].append(j.get_text())
                t1+=1
    x=alert(d[l[4]])
    print(d)
    for i in x:
        print(d[l[0]][i],d[l[4]][i])
    time.sleep(30)
while(True):
    task()

