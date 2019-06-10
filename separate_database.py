#coding=utf-8
import codecs
import json
import os
from urllib import urlopen
username = "zhangyingjie"
root_dir = "/home/"+username+"/poetry/chinese-poetry/"
origin_dir = root_dir + "json/"
diff_path = root_dir + "diff_path/"
punct_path = root_dir + "punct_path/"
clear_path = root_dir + "clear_path/"


def contain_punct(paras):
    Flag = False
    for para in paras:
        if u"()[]{}" in para:
            Flag = True
    return Flag

def diff_length_sentence(paras):
    Flag = False
    for i in range(len(paras)-1):
        if len(paras[i]) != len(paras[i+1]):
            Flag =True
    return Flag

def push_to_diff_database(r, diff_path):
    with codecs.open(diff_path,'w',encoding='utf-8') as fw:
        json.dump(r,fw)

def push_to_punct_database(r, punct_path):
    with codecs.open(punct_path,'w',encoding='utf-8') as fw:
        json.dump(r,fw)

def push_to_clear_database(r, clear_path):
    print(type(r))
    with codecs.open(clear_path, 'w',encoding='utf-8') as fw:
        json.dump(r, fw)

def main():
    for file in os.listdir(origin_dir):
        u = urlopen(origin_dir + file)
        resp = json.loads(u.read().decode('utf-8'))
        print(type(resp))
        for r in resp:
            if r:
                p = r.get("paragraphs")
                if contain_punct(p):
                    push_to_punct_database(r,punct_path+file)
                    break
                if diff_length_sentence(p):
                    push_to_diff_database(r,diff_path+file)
                    break
                push_to_clear_database(r,clear_path+file)

if __name__ == '__main__':
    main()