#coding=utf-8
import sys
import os
import json
import re
import numpy as np

# round_bracket = re.compile('(.*)', '')
# square_bracket = re.compile('[\]\[]', '')
# curly_bracket = re.compile(u'{.*}', '')
# guillemet = re.compile(u'《.*》', '')
# double_period = re.compile(u'。。','。')
# double_comma = re.compile(u'，，','，')



def get_data(opt):

    #导入已经处理好的二进制数据文件
    if os.path.exists(opt.pickle_path):
        data = np.load(opt.pickle_path)
        data, word2ix, ix2word = data['data'], data['word2ix'].item(), data['ix2word'].item()
        return data, word2ix, ix2word

    #如果没有处理好的二进制文件,则梳理原始json文件
    #opt 为config实体



def _parseRawDate(author=None, constrain=None, src='/home/zhangyingjie/poetry/chinese-poetry/simple_json/', category='poet.tang'):

    def sentenceParse(para):

        result, number = re.subn(u"（.*）", "", para)
        result, number = re.subn(u"{.*}", "", result)
        result, number = re.subn(u"《.*》", "", result)
        result, number = re.subn(u"《.*》", "", result)
        result, number = re.subn(u"[\]\[]", "", result)
        r = ""
        for s in result:
            if s not in  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']:
                r += s
        r, number = re.subn(u"。。", u"。", r)
        return r

    def handleJson(file):
        rst = []
        data = json.loads(open(file).read())
        for poetry in data:
            pdata = ''
            if (author!=None and poetry.get("author")!= author):
                continue
            plist = poetry.get('paragraphs')
            flag = False
            for s in plist:
                sp = re.split("[,!.．，]", s)
                for tr in sp:
                    if constrain is not None and len(tr) != constrain and len(tr) != 0:
                        flag  = True
                    if flag:
                        break
            if flag:
                continue
            for sentence in poetry.get("paragraphs"):
                #将诗句拼接成一个字符串,减少调用清理函数的次数
                pdata += sentence
            pdata = sentenceParse(pdata)
            if pdata != "":
                rst.append(pdata)
        return rst

    data = []
    for filename in os.listdir(src):
        if filename.startswith(category):
            data.extend(handleJson(src+filename))

    return data

#
#
# if __name__ == '__main__':
#     _parseRawDate()