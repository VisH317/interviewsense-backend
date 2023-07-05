import os
import openai
from bucket import bucket
from dotenv import load_dotenv
from pydub import AudioSegment
from typing import List

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]


def transcribe(file_name: str) -> str:
    file = bucket.Object(file_name).get()

    # generate audio segment for chunking
    extension = file_name.split(".")[-1]
    segment = AudioSegment.from_file(file, extension)
    ten_minutes = 10 * 60 * 1000

    chunks = []

    for i in list(range(0, len(segment), ten_minutes))[:-1]:
        chunks.append(segment[i:(i+ten_minutes)])

    transcripts: List[str] = []

    for chunk in chunks:
        transcript = openai.Audio.transcribe("whisper-1", chunk)
        transcripts.append(transcript["text"])

    return " ".join(transcripts)

