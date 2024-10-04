from typing import Optional, List
from fastapi import FastAPI, Request, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.background import BackgroundTask
import os
from utils import *

app = FastAPI()

@app.post("/process/{u_id}")
async def create_upload_file(
    files: List[UploadFile],
    threshold: str = Form(...),
    u_id: str = u_id
):
    if id:
        fp = f'data/{userid}.txt'
        with open(fp, 'wb') as f:
            for file in files:
                f.write(file.file.read())
                f.write(b'\n')
        with open(fp, 'a') as f:
            f.write(f'threshold: {threshold}')
            f.write('\n')
            f.write(f'userid: {userid}')
        return FileResponse(fp, background=BackgroundTask(lambda: os.remove(fp)))
    else:
        return {"message": "id not specified"}

@app.get("/")
async def main():
    content = """
                <body>
                <form action="/process/" enctype="multipart/form-data" method="post">

                <label for="userid">UserID:</label><br>
                <input type="text" id="userid" name="userid"><br>

                <label for="threshold">threshold:</label><br>
                <input type="text" id="threshold" name="threshold"><br>

                <input name="files" type="file" multiple><br>
                <input name="files" type="file" multiple><br>

                <input type="submit"><br>
                </form>
                </body>
            """
    return HTMLResponse(content=content)

@get("/")