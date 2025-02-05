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

    def record_audio(self):
        """Record audio from the microphone using PyAudio. Records until user stops."""
        print("Recording... Press Enter to stop recording.")
        
        stream = self.pyaudio.open(
            format=self.format,
            channels=self.channels,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk
        )
        
        frames = []
        try:
            import threading
            stop_recording = threading.Event()
            
            def wait_for_enter():
                input()
                stop_recording.set()
            
            threading.Thread(target=wait_for_enter, daemon=True).start()
            
            while not stop_recording.is_set():
                data = stream.read(self.chunk)
                frames.append(data)
                
        except KeyboardInterrupt:
            pass
        
        print("\nRecording finished.")
        
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