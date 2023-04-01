import os
import openai
import openai

OPENAI_API_KEY = "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"

class WhisperASR:
    def __init__(self):
        
        self.api_key = OPENAI_API_KEY
        if self.api_key is None:
            raise Exception("OPENAI_API_KEY not found in environment variables.")
        openai.api_key = self.api_key

    def transcribe(self, file_path):
        audio_file= open("output.wav", "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript
        