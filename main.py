from fastapi import FastAPI, File, UploadFile
from typing import List # an API that the end-user can access.
import shutil
import os
from predict import predict
import requests
# intialising the fastapi.
app = FastAPI()

# path = os.getcwd()+"\data"
# os.mkdir(path)
# url = 1
#
#
# shutil.rmtree(path)

#files: List[UploadFile] = File(...)
@app.post("/pred")
def pred(files: List[UploadFile] = File(...)):

    path = os.getcwd() + "\\data"

    try:
        shutil.rmtree(path)
    except Exception:
        pass
    os.mkdir(path)


    for file in files:
        try:
            contents = file.file.read()
            with open(path+"\\"+file.filename, 'wb') as f:
                f.write(contents)
        except Exception:
            pass
        finally:
            file.file.close()
    d = {}
    fs = os.listdir(path)
    for i in fs:
        d[i] = predict(path+"\\"+i)
    shutil.rmtree(path)

    return d