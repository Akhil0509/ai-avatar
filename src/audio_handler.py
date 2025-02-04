import pyaudio
import wave
import os

class AudioHandler:
    def __init__(self):
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.sample_rate = 16000
        self.pyaudio = pyaudio.PyAudio()

    def record_audio(self, duration=10):
        """Record audio from the microphone using PyAudio."""
        print("Recording...")
        
        stream = self.pyaudio.open(
            format=self.format,
            channels=self.channels,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk
        )
        
        frames = []
        for _ in range(0, int(self.sample_rate / self.chunk * duration)):
            data = stream.read(self.chunk)
            frames.append(data)
        
        print("Recording finished.")
        
        stream.stop_stream()
        stream.close()
        self.pyaudio.terminate()
        
        temp_file = "temp_audio.wav"
        self._save_to_wav(temp_file, frames)
        return temp_file

    def _save_to_wav(self, filename, frames):
        """Save recorded audio to WAV file."""
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.pyaudio.get_sample_size(self.format))
            wf.setframerate(self.sample_rate)
            wf.writeframes(b''.join(frames))

    @staticmethod
    def get_audio_file():
        """Get audio file path from user."""
        while True:
            file_path = input("Enter the path to your audio file: ").strip()
            if os.path.exists(file_path):
                return file_path
            print("File not found. Please try again.") 