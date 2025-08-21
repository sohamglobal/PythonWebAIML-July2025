import os

try:
    os.rename('abc.txt','python.txt')
    print('file name changed')
except:
    print('404 file not found')