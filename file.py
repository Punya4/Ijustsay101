import dropbox
class Ijust:
    def __init__(self,say):
        self.say=say
    def uf(self,ffrom,f2):
        dbx=dropbox.Dropbox(self.say)
        f=open(ffrom,'rb')
        dbx.files_upload(f.read(),f2)
def Ijust2():
    say='zGnrj8CODigAAAAAAAAAATp-garWtAEhiXfeeVRBzCCnbKrRM_07i8PB_4oVZYuk'
    iobj=Ijust(say)
    ffrom=input('Enter the file name to transfer(path) - ')
    f3=input('enter folder name - ')
    f2='/'+f3+'/'+ffrom
    iobj.uf(ffrom,f2)
    print('file has been uploaded')
    
Ijust2()