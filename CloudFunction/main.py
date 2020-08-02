import os
os.system('apt get update')
os.system('apt install aptitude')
os.system('aptitude install mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file -y')

import MeCab
import urllib.request
from bs4 import BeautifulSoup
import zipfile
import requests
url='https://storage.googleapis.com/wetelework/ja.zip'
urllib.request.urlretrieve(url,'/tmp/ja.zip')
with zipfile.ZipFile('/tmp/ja.zip') as existing_zip:
    existing_zip.extractall('/tmp')

import gensim
model = gensim.models.Word2Vec.load('/tmp/ja.bin')

def tokenizer(text):
    tokens=[]
    tagger = MeCab.Tagger("-Ochasen")
    node = tagger.parse(text).split('\n')
    for n in node:
        if ( '名詞' in n):
            tokens.append(n.split('\t')[0])
        if(n=='EOS'):
            break
    return tokens


def personal_vector(words):
    tokens=tokenizer(words)
    num_token=1.0
    v=[0.]*300
    for t in tokens:
        try :
            v=v+model[t]
            num_token+=1
        except KeyError:
            pass
        return [x/num_token for x in v]

def hotel_vector(hotel_id):
    v=[0.]*300
    num_token=1.0
    for i in range(0,100,20):#100件取得
        load_url = "https://review.travel.rakuten.co.jp/hotel/voice/"+hotel_id+"/?f_sort=4&f_next="+str(i)
        html = requests.get(load_url)
        soup = BeautifulSoup(html.content, "html.parser")
        elements = soup.find_all(class_='commentSentence')
        for e in elements:
            if e is not []:
                ts=tokenizer(e.text)
            for t in ts:
                try:
                    v+=model[t]
                    num_token+=1
                except KeyError:
                    pass
    v=v/num_token 
    return [x/num_token for x in v]
    


def main(request):
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        if request.args.get('type')=='0':
            a=personal_vector(str(request.args.get('value')))
            return str(a)
        elif  request.args.get('type')=='1':
            b=hotel_vector(request.args.get('value'))
            return str(b)
        else :
            return 'invalid type'
