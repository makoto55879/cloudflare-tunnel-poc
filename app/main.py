from fastapi import FastAPI, UploadFile, File
import shutil, os

app = FastAPI()


# GET /ping : 疎通確認用エンドポイント
@app.get("/ping")
def ping():
    return {"message": "pong"}


# POST /upload : ファイル受け取り用エンドポイント
@app.post("/upload")
def upload(file: UploadFile = File(...)):
    save_dir = "/data/uploads"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, file.filename)
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "status": "saved"}
