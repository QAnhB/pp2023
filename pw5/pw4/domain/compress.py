from zipfile import ZipFile
import os

class compress:
    def __init__(self,txt_file,zip_file):
        self.txt_file = txt_file
        self.zip_file = zip_file
    
    def compress_file(self):
        f = ZipFile(self.zip_file, 'w')
        f.write(self.txt_file)