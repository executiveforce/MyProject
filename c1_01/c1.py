import requests
import numpy
import random
import re
from bs4 import BeautifulSoup

def reptile():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content,'html.parser')

    for div in soup.find_all('div',{'class':'content'}):
        print div.text.strip()

def demo_list():
    lista = [1,2,3] #vector ArrayList
    print 1,lista
    listb = [1,'a',4]
    print 2,listb
    lista.extend(listb)
    print 3,lista
    print 4, 'a' in lista
    listb.insert(0,'W')
    print 5, listb
    listb.reverse()
    print 6, listb
    listc = [3,1,5,7,2,0,9]
    print 7,listc
    listc.sort()
    print 8,listc

def demo_dict():
    dicta = {1:1,2:4,6:10}
    print 1, dicta
    print 2, dicta.keys()
    print 3, dicta.values()
    print 4, dicta.has_key(1)

    for key, value in dicta.items():
        print 'Key-Value:',key,value

    dictb = {'+': 'add', '-': 'sub'}
    print 5,dictb

def demo_set():
    seta = set((1,2,3,4))
    setb = set((2,3,4,5,2))
    print 1,seta
    print 2,setb
    seta.add(3)
    print 3,seta
    seta.intersection(setb)
    print 4,seta, seta &setb, seta | setb, seta.union(setb)
    print 5, seta - setb
    print 6, seta.difference(setb)
    while(len(seta)>0):
        print seta.pop()
    print 7, seta
    print 8, seta.isdisjoint(setb)

class User:
    type ='USER'
    def __init__(self,name,uid):
        self.name = name
        self.uid = uid
    def __repr__(self):
        return 'I am '+self.name+' '+str(self.uid)

class Guest(User):
    type = 'Guest'
    def __repr__(self):
        return 'I am '+self.name+' '+str(self.uid)

def demo_exception():
    try:
        print 2/0
        raise Exception('Raise Error','NowCoder')
    except Exception as e:
        print 'error:',e
    finally:
        print 'clearn up'

def demo_random():
    random.seed(1)
    print 1,random.random()
    print 2,random.random()*100
    print 3,random.randint(0,100)
    print 4,random.choice(range(0,100,10))
    print 5,random.sample(range(1,100),4)

def demo_re():
    str = '213sdasdsad3312'
    pl = re.compile('[\d]+')
    p2 = re.compile('\d')
    print 1,pl.findall(str)
    print 2,p2.findall(str)

    str2 = 'a@163.com;b@gmail.com'
    p3 = re.compile('[\w]+@163\.com')
    print 3,p3.findall(str2)


if __name__=='__main__':
    print 'Hello Python'
    #demo_list()
    #demo_dict()
    #demo_set()
    #user1 = User('LB',1)
    #$guest1 = Guest('Allen',2)
    #print guest1
    #demo_exception()
    #demo_random()
    #demo_re()
    reptile()


