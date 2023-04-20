import cv2
import dropbox
import time
import random
import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

start_time = time.time()

def capture():
    number = random.randint(0,100)
    vidcaptureobj = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = vidcaptureobj.read()
        imgname = "img" + str(number) + ".png"
        cv2.imwrite(imgname,frame)
        start_time = time.time
        result = False
    return imgname
    print("Snapshot successfully Taken")
    vidcaptureobj.release()
    cv2.destroyAllWindows()
capture()

def upload_file(imgname):
    access_token = os.getenv('DROPBOX_API_KEY')
    file = imgname
    fromfile = file
    tofile = "/newfolder1" + (imgname)
    dbx = dropbox.Dropbox(access_token)
    with open(fromfile, 'rb') as f:
        dbx.files_upload(f.read(),tofile,mode = dropbox.files.WriteMode.overwrite)
        print(f"File successfully uploaded to {tofile}")

def main():
    while(True):
        if((time.time() - start_time) >= 3):
            print("Capturing Image")
            name = capture()
            print("Image Captured/nUploading Image")
            upload_file(name)
main()