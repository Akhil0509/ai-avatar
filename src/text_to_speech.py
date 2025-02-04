from gtts import gTTS
from pygame import mixer
import time
import os

class TextToSpeech:
    def __init__(self):
        self.output_file = "output_hindi.mp3"

    def speak(self, text):
        """Convert text to speech and play using pygame mixer."""
        try:
            mixer.init()
            
            tts = gTTS(text=text, lang='hi')
            tts.save(self.output_file)
            
            print("Playing response...")
            mixer.music.load(self.output_file)
            mixer.music.play()
            
            while mixer.music.get_busy():
                time.sleep(0.1)
                
            mixer.quit()
            self._cleanup()
            
        except Exception as e:
            print(f"Error in text-to-speech: {e}")
            self._cleanup()

    def _cleanup(self):
        """Remove temporary audio file."""
        if os.path.exists(self.output_file):
            os.remove(self.output_file) 