'''
Created on 2019年9月22日

@author: Neko
'''
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

while 1:
    ch = input("请选择功能：1=生成密钥，2=加密文件，3=解密文件，4=退出")
    if ch == '1':
        password = input("请输入口令：").encode(encoding='utf-8')
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password)) 
        #上面使用口令和加盐生成了密钥
        open('D:/keyFile.txt','wb').write(key)      #保存密钥便于重复使用  
    elif ch == '2':
        enPath = input("请输入密钥路径：")
        enKey = open(enPath,'rb').read()
        filePath = input("请输入待加密文件路径：")
        plainFile = open(filePath,'rb').read()
        f = Fernet(enKey)   #加载密钥
        enFile = f.encrypt(plainFile)   #开始加密
        open('D:/enFile','wb').write(enFile)    #保存加密后的文件
    elif ch == '3':
        dePath = input("请输入密钥路径：")
        deKey = open(dePath,'rb').read()
        filePath = input("请输入待解密文件路径：")
        enFile = open(filePath,'rb').read()
        f = Fernet(deKey)
        deFile = f.decrypt(enFile)
        open('D:/deFile','wb').write(deFile)
    else :
        exit()
    
    
    
    
    
    
    
    
    
    
    
    