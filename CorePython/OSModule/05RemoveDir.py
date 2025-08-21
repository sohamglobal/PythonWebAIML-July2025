import os

try:
    os.rmdir("football")
    print('directory deleted')
except:
    print('directory does not exist')