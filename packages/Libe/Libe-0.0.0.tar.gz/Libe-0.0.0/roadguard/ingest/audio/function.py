import os
from openai import OpenAI

from roadguard.ingest.audio import parameter


def transcribe(path: str,
               model=parameter.model) -> str:
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    response = client.audio.transcriptions.create(
        model=model,
        file=open(path, "rb"),
    )
    return response.choices[0].message.content
