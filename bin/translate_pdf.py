#-*- coding:utf-8 -*-

import os
from googletrans import Translator
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )


def pdf_to_txt(pdf_path):

    pwd = os.getcwd()
    py_file = pwd + '/' + 'pdf2txt.py'
    out_file = 'output.txt'
    str = '{} -o {} {}'.format(py_file, out_file, pdf_path)
    p = os.system(str)
    return p


def extract_paragraph():

    pwd = os.getcwd()
    txt_path = pwd + "/output.txt"
    f = open(txt_path, 'r')
    content = f.read()

    symbol = '<-=n=->'
    content2 = content.replace('\n\n', symbol)
    content3 = content2.replace('\n', '')
    content4 = content3.replace(symbol, '\n\n')
    paragraphs = content4.split('\n')

    print (paragraphs)

    fp = open(pwd+'/target.txt', 'w')
    fp.write(content4)
    fp.flush()
    fp.close()

    return content4


def main(pdf_path):

    p = pdf_to_txt(pdf_path=pdf_path)

    if p == 0:
        translator = Translator()
        content = extract_paragraph()

    else:
        print ('pdf to text error!')


if __name__=="__main__":
    main('/Users/gavintan/PycharmProjects/python2_learning/bin/naacl06-shinyama.pdf')