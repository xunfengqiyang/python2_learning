# -*- coding: utf-8 -*-
import os
import json

test_file = '/Users/gavintan/Desktop/testfile'
test_sentence = '我爱编程'


def test_write_file():

    dict = {
        'key':test_sentence
    }

    str = json.dumps(dict)

    f = open(test_file, 'w')

    f.write(str)
    f.flush()
    f.close()


test_write_file()
