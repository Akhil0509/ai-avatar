import argparse
import dotenv
from src.audio_handler import AudioHandler
from src.transcriber import Transcriber
from src.response_generator import ResponseGenerator
from src.text_to_speech import TextToSpeech

def parse_arguments():
    parser = argparse.ArgumentParser(description='Audio Processing CLI')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--speak', action='store_true', help='Record audio from microphone')
    group.add_argument('--file', action='store_true', help='Process audio from file')
    return parser.parse_args()

def main():
    dotenv.load_dotenv()
    args = parse_arguments()
    
    audio_handler = AudioHandler()
    transcriber = Transcriber()
    response_generator = ResponseGenerator()
    tts = TextToSpeech()
    
    # Handle audio input
    if args.speak:
        audio_input = audio_handler.record_audio()
        hindi_text = transcriber.transcribe(audio_input, is_file=False)
    else:  # args.file
        audio_file = audio_handler.get_audio_file()
        hindi_text = transcriber.transcribe(audio_file, is_file=True)
    
    # Get and play response
    if hindi_text:
        response = response_generator.get_response(hindi_text)
        if response:
            print("\nGroq Response:")
            print(response)
            tts.speak(response)
        else:
            print("Failed to get response from Groq")
    else:
        print("Failed to transcribe audio")

if __name__ == "__main__":
    main()
