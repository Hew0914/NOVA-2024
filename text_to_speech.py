from openai import OpenAI
import pyaudio
import io
from pydub import AudioSegment
from pathlib import Path
from text_translator import translate_to_chinese

def example_tts(text):
    """ 
    Examples of text-to-speech from the proxy
    """
    client = OpenAI(
        api_key="", 
        base_url="https://nova-litellm-proxy.onrender.com"
    )
    
    translated = translate_to_chinese(text)

    speech_file_path = Path(__file__).parent / "example_tts_output.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=translated
    )
    # print(dir(response))

    audio_data = response.content

    audio_segment = AudioSegment.from_file(io.BytesIO(audio_data), format="mp3")

    # Set up PyAudio for playback
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(audio_segment.sample_width),
                    channels=audio_segment.channels,
                    rate=audio_segment.frame_rate,
                    output=True)

    # Play the audio directly
    stream.write(audio_segment.raw_data)

    # Clean up
    stream.stop_stream()
    stream.close()
    p.terminate()

    # response.with_streaming_re(speech_file_path)

# if __name__ == "__main__":
#     english_input = ""
#     example_tts(english_input)
