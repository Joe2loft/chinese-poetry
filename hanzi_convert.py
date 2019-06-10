#encoding=utf8
from hanziconv import HanziConv
import codecs
import os

print(HanziConv.toSimplified('繁簡轉換器'))
username = 'zhangyingjie'
# file_in = '/home/'+username+'/poetry/chinese-poetry/json/poet.song.0.json'
# file_out =  '/home/'+username+'/poetry/chinese-poetry/simple_json/poet.song.0.json'
root_in = '/home/'+username+'/poetry/chinese-poetry/json/'
root_out = '/home/'+username+'/poetry/chinese-poetry/simple_json/'

def convertToSimple(inputPath, outputPath):
    with codecs.open(inputPath, 'r', encoding='utf-8') as fin:
        content = fin.read()
        with codecs.open(outputPath, 'w', encoding='utf-8') as fout:
            fout.write(HanziConv.toSimplified(content))

def read_files(root_in, root_out):
    for file in os.listdir(root_in):
        file_in = root_in  + file
        file_out = root_out + file
        print(file)
        convertToSimple(file_in,file_out)

# convertToSimple(file_in, file_out)

read_files(root_in, root_out)