import requests
from bs4 import BeautifulSoup
# url="https://news.google.com/?hl=en-IN&tab=wn1&gl=IN&ceid=IN:en"
def srchwords(x):
    for i in range(len(x)):
        if('surge' in x[i] or 'acquisitions' in x[i] or 'IPO' in x[i]):
            print('->',x[i])
def task():
    url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    r=requests.get(url)
    htmlcontent=r.content
    # print(htmlcontent)

    soup = BeautifulSoup(htmlcontent, 'html.parser')
    e=soup.find_all('div',class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
    main,sub=[],[]
    # print(e)
    k=0
    for i in e:
        x=i.find('h3',class_="ipQwMb ekueJc gEATFF RD0gLb")
        x=x.find('a',class_="DY5T1d").get_text()
        main.append(x)
        sub.append([])
        x=i.find_all('h4',class_="ipQwMb ekueJc gEATFF RD0gLb")
        for j in x:
            t=j.find('a',class_="DY5T1d").get_text()
            sub[k].append(t)
        k+=1
    # print(sub,main)
    for i in range(k):
        print(main[i])
        for j in sub[i]:
            print('*',j)
    srchwords(main)
    srchwords(sub)
task()
