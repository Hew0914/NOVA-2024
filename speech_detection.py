from openai import OpenAI
import logging
from RealtimeSTT import AudioToTextRecorder
from text_to_speech import example_tts
import pyaudio
import time
import io
import threading

def process_text(text):
    example_tts(text)

def live_transcribe():
    print("Wait until it says 'speak now'")
    recorder = AudioToTextRecorder(no_log_file=True)
    try:
        while True:
            recorder.text(process_text)
    except KeyboardInterrupt:
         print('\nRecording stopped.')

if __name__ == '__main__':
     live_transcribe()