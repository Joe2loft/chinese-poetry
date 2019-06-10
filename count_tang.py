#coding=utf-8
import codecs
import json
from  urllib import urlopen
import os

username = 'zhangyingjie'
root = '/home/'+username+'/poetry/chinese-poetry/json_new/'

punct_type = u"punct"
clear_type = u"clear"
diff_type  = u"diff"

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

def count_num(file):
    u = urlopen(file)
    resp = json.loads(u.read().decode('utf-8'))
    count_5 = 0
    count_7 = 0
    count_p2 = 0
    count_p4 = 0
    count_p8 = 0
    count_s2 = 0
    count_s4 = 0
    count_s8 = 0
    count_other = 0
    for r in resp:
        if r:
            para = r.get("paragraphs")
            if not para:
                continue
            if len(para[0]) == 12:
                count_5 += 1
                if len(para) == 2:
                    count_p2 += 1
                elif len(para) == 4:
                    count_p4 += 1
                elif len(para) == 8:
                    count_p8 += 1
            elif len(para[0]) == 16:
                count_7 += 1
                if len(para) == 2:
                    count_s2 += 1
                elif len(para) == 4:
                    count_s4 += 1
                elif len(para) == 8:
                    count_s8 += 1
    return count_5, count_p2, count_p4 , count_p8, count_7 , count_s2, count_s4, count_s8

def count_all(root, start="poet.song"):
    count_all_5 = 0
    count_all_p2 = 0
    count_all_p4 = 0
    count_all_p8 = 0

    count_all_7 = 0
    count_all_s2 = 0
    count_all_s4 = 0
    count_all_s8 = 0
    for file in os.listdir(root):
        if file.startswith(start):
            file_check = root + file
            p, p2, p4, p8, s, s2, s4, s8= count_num(file_check)
            count_all_5 += p
            count_all_7 += s
            count_all_p2 += p2
            count_all_p4 += p4
            count_all_p8 += p8
            count_all_s2 += s2
            count_all_s4 += s4
            count_all_s8 += s8
    return count_all_5,count_all_p2,count_all_p4, count_all_p8, count_all_7,count_all_s2,count_all_s4, count_all_p8


def count_num(root, start="poet.song"):
    punct_count = 0
    diff_count =0
    clear_count = 0
    try:
        for file in os.listdir(root):
            if file.startswith(start):
                file_punct = root + file
                u = urlopen(file_punct)
                data = json.loads(u.read().decode('utf-8'))
                for resp in data:
                    if resp:
                        p = resp.get("type")
                        if p == punct_type:
                            punct_count += 1
                        elif p == diff_type:
                            diff_count += 1
                        else:
                            clear_count += 1
    except AttributeError:
        print("unicode object has no attribute 'get' ")
    return punct_count, diff_count, clear_count

def count_clear(root, start="poet.song"):
    for file in os.listdir(root):
        file_check = root + file
        u = urlopen(file)
        resp = json.loads(u.read().decode('utf-8'))

if __name__ == '__main__':
    # five,five_2,five_4,five_8,  seven, seven_2,seven_4 , seven_8= count_all(root,"poet.tang")
    # print("五言: {five}, 五言2句: {five_2}, 五言4句 {five_4}, 五言8句: {five_8},"
    #       " 七言: {seven} , 七言2句:{seven_2}, 七言4句 {seven_4} ,七言8句: {seven_8} ".format(five=five, five_2=five_2, \
    #     five_4 =five_4, five_8=five_8,seven=seven, seven_2=seven_2, seven_4=seven_4, seven_8=seven_8))

    p, d ,c = count_num(root)
    print("punct :{p}, diff :{d}, clear:{c}".format(p=p, d=d, c=c) )
