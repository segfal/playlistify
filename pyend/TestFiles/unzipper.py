import zipfile as zp
import os

def unzipper(zip_file):
    with zp.ZipFile(zip_file,"r") as zip:
        zip.extractall()
        print("Done!")
        os.remove(zip_file)
    
unzipper("data.csv.zip")
