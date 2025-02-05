# Hindi Voice Assistant

An intelligent voice assistant that processes Hindi speech, generates AI responses, and speaks back in Hindi. Built with modular Python architecture using AssemblyAI for speech recognition and Groq for AI responses.

## Features

- Record audio through microphone
- Process existing audio files
- Hindi speech recognition
- AI-powered conversational responses
- Natural Hindi text-to-speech output

## Project Structure
```
hindi-voice-assistant/
├── src/
│   ├── __init__.py
│   ├── audio_handler.py     # Audio recording and file operations
│   ├── transcriber.py       # Speech recognition using AssemblyAI
│   ├── response_generator.py # AI response generation using Groq
│   └── text_to_speech.py    # Text-to-speech conversion
├── main.py                  # Main application entry point
├── requirements.txt         # Project dependencies
├── .env                     # API keys and configuration
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

## Prerequisites

- Python 3.8+
- AssemblyAI API key
- Groq API key
- Working microphone (for recording mode)

## Quick Start

1. Clone and set up environment:
```bash
git clone <repository-url>
cd hindi-voice-assistant
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Create `.env` file:
```bash
ASSEMBLYAI_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
```

3. Run the assistant:
```bash
# Record mode
python main.py --speak
```
```bash
# File processing mode
python main.py --file
```

## Architecture

The project follows a modular design with four main components:

- **AudioHandler**: Manages audio recording and file operations
- **Transcriber**: Handles Hindi speech recognition
- **ResponseGenerator**: Generates AI responses using Groq
- **TextToSpeech**: Converts responses to spoken Hindi

## Usage Examples

1. Recording Mode:
   - Run with `--speak` flag
   - Speak in Hindi/English and press Enter to end recording
   - Wait for AI response

2. File Mode:
   - Run with `--file` flag
   - Provide path to audio file
   - Receive AI response

## Error Handling

The application includes comprehensive error handling for:
- Audio device issues
- File access problems
- API failures
- Transcription errors
- Speech synthesis issues

## Dependencies

Key packages:
- PyAudio: Audio handling
- AssemblyAI: Speech recognition
- Groq API: AI processing
- gTTS: Text-to-speech
- Pygame: Audio playback

For complete list, see `requirements.txt`.
