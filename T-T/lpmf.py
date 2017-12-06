class lpmFile:
    def __init__(self,path):
        self.path=path
    def arhiveLPM(self, path):
        import zipfile
        if type(path)!=str:
            raise TypeError
        pathz=path+'.lpm'
        first_zip = zipfile.ZipFile(pathz,'w')
        first_zip.write(path, compress_type=zipfile.ZIP_DEFLATED)
        first_zip.close()
        with open(pathz, 'br+') as file:
            file.writelines(['lazyperson'.encode()]+[file.readlines(),file.seek((0))][0])
    def extractLPM(self,path,rewrite=False):
        import os
        if type(path)!=str:
            raise TypeError
        if path[-3:]!='lpm':
            print('Warning! Maybe this file is not LPM!!!')
        with open(path, 'br+') as file:
            #TODO Убрать костыль tmp2314142134.zip
            f2332 = open('tmp2314142134.zip','wb')
            f2332.write(file.read()[10:])
            f2332.close()
            #TODO Дописать чтобы если существует, зависело от флага rewrite
        try:
            file = open(path[:-4],'r')
            print('File already exist..')
            #TODO убрать костыль
            if rewrite:
                0/0
        except:
            import zipfile
            szip = zipfile.ZipFile('tmp2314142134.zip')
            #print('.\\'+path[:-4])
            szip.extractall('./')

            szip.close()
            import os
        os.remove('tmp2314142134.zip')
            #with open(path[:-4], 'w') as file2:
    def CodeToLpm(self,code):
        import os
        import hashlib
        hcode = hashlib.md5(code.encode())
        hcode = hcode.hexdigest()

        with open(str(hcode), 'w') as file:
            file.write(code)
        self.arhiveLPM(self, str(hcode))
        os.remove(str(hcode))
        return hcode
    def LpmToCode(self,hash_):
        import os
        self.extractLPM(self,str(hash_)+'.lpm',rewrite=True)
        with open(str(hash_)) as file:
            exec(file.read())
        os.remove(hash_)