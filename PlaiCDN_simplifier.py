import os
from binascii import hexlify, unhexlify

titleID = raw_input('Please paste titleID: ')
decTitleKeys = {}

def getDecKeys():
    with open('decTitleKeys.bin', 'rb') as file_handler:
        n_entries = os.fstat(file_handler.fileno()).st_size / 32
        file_handler.seek(16, os.SEEK_SET)
        for i in range(int(n_entries)):
            file_handler.seek(8, os.SEEK_CUR)
            title_id = file_handler.read(8)
            decrypted_title_key = file_handler.read(16)
            title_ID = (hexlify(title_id)).decode()
            decTitleKey = (hexlify(decrypted_title_key)).decode()
            decTitleKeys[title_ID] = decTitleKey

getDecKeys()



print('plaiCDN.exe' + ' ' + titleID + ' ' + decTitleKeys[titleID])
os.system('plaiCDN.exe' + ' ' + titleID + ' ' + decTitleKeys[titleID])
