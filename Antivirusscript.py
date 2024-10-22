import os

class antivirusscript():

    
    def countfile(startpath):
        filecount=0
        for dirpath,dirnames,filename in os.walk(startpath):
            filecount+= len(filename)   
            return filecount     