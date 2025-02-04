import os
import assemblyai as aai

class Transcriber:
    def __init__(self):
        aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
        self.transcriber = aai.Transcriber()
        self.config = aai.TranscriptionConfig(
            language_code="hi",
            speech_model=aai.SpeechModel.best
        )

    def transcribe(self, audio_source, is_file=False):
        """Transcribe audio using AssemblyAI."""
        try:
            transcript = self.transcriber.transcribe(audio_source, self.config)

            if transcript.status == aai.TranscriptStatus.error:
                print(f"Error: {transcript.error}")
                return None
            
            print("Transcription (Hindi): ", transcript.text)
            
            if not is_file and os.path.exists(audio_source):
                os.remove(audio_source)
                
            return transcript.text

        except Exception as e:
            print(f"Error: {e}")
            return None 