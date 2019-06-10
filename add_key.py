#coding=utf-8
import json
import os
import codecs
from urllib import urlopen
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

username = "zhangyingjie"
root_dir = "/home/"+username+"/poetry/chinese-poetry/"
origin_dir = root_dir + "json/"
new_dir = root_dir + "json_with_type/"

punct_type = "punct"
clear_type = "clear"
diff_type  = "diff"

def contain_punct(paras):
    Flag = False
    if paras:
        for para in paras:
            if "(" in para or '[' in para or '《' in para or '{' in para:
                Flag = True
    return Flag

def diff_length_sentence(paras):
    Flag = False
    if paras:
        for i in range(len(paras)-1):
            if len(paras[i]) != len(paras[i+1]):
                Flag =True
    return Flag




def main():
    for file in os.listdir(origin_dir):
        if file.startswith("poet"):
            try:
                with codecs.open(origin_dir+file, 'r') as f:
                    str = f.read().encode("utf-8")
                    data = json.loads(str)
            except ValueError:
                print(" No JSON object could be decoded")

            for resp in data:
                if resp and isinstance(resp, dict):
                    p = resp.get("paragraphs")
                    if contain_punct(p):
                        resp["type"] = punct_type
                        break
                    if diff_length_sentence(p):
                        resp["type"] = diff_type
                        break
                    resp["type"] = clear_type

            with codecs.open((new_dir+file), 'w') as f:
                f.write(json.dumps(data, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()