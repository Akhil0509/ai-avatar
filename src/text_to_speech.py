from gtts import gTTS
from pygame import mixer
import soundfile as sf
import numpy as np
import time
import os

class TextToSpeech:
    def __init__(self):
        self.output_file = "output_hindi.wav"  # Changed to WAV format
        self.speed_adjusted_file = "speed_adjusted_output.wav"
        self.speed_factor = 1.1

    def speak(self, text):
        """Convert text to speech and play using pygame mixer."""
        try:
            mixer.init()
            
            # Generate speech
            tts = gTTS(text=text, lang='hi')
            tts.save(self.output_file)
            
            # Adjust speed using soundfile and numpy
            data, samplerate = sf.read(self.output_file)
            # Resample the audio using numpy
            new_length = int(len(data) / self.speed_factor)
            time_axis = np.linspace(0, len(data), len(data))
            new_time_axis = np.linspace(0, len(data), new_length)
            data_adjusted = np.interp(new_time_axis, time_axis, data)
            # Save the speed-adjusted audio
            sf.write(self.speed_adjusted_file, data_adjusted, samplerate)
            
            # Play the speed-adjusted audio
            print("Playing response...")
            mixer.music.load(self.speed_adjusted_file)
            mixer.music.play()
            
            while mixer.music.get_busy():
                time.sleep(0.1)
                
            mixer.quit()
            self._cleanup()
            
        except Exception as e:
            print(f"Error in text-to-speech: {e}")
            self._cleanup()

    def _cleanup(self):
        """Remove temporary audio files."""
        for file in [self.output_file, self.speed_adjusted_file]:
            if os.path.exists(file):
                os.remove(file) 