# coding: UTF-8

def file(data, path='./default.txt'):
    with open(path, mode='w') as f:
        f.write(data)