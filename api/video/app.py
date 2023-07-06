from fastapi import FastAPI
from transcribe import transcribe
from chain import chain
from pydantic import BaseModel
from typing import List


app = FastAPI()


class Req(BaseModel):
    file_name: str
    # summary: str

class Res(BaseModel):
    summary: List[str]


@app.post("/video", status_code=200, response_model=Res)
def get_video_summary(req: Req) -> Res:
    transcription = transcribe(req.file_name)
    summary = chain.run(input_text=transcription)
    return Res(summary)
