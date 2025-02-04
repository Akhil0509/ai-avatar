import os
import requests
import re

class ResponseGenerator:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def get_response(self, prompt):
        """Get response from Groq API."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        prompt_avatar = (
            "You are a female AI animation avatar. Speak in a friendly and engaging way, like a cartoon character. "
            "Use expressive and lively language with emotions. Respond to this: " + prompt
        )
        
        payload = {
            "model": "deepseek-r1-distill-llama-70b",
            "messages": [
                {"role": "system", "content": """
                 Only output in hindi. Keep your response concise.
                 You are a female animated avatar. Speak in an engaging way. 
                 Do not include any special characters or emojis in your response.
                 Do not bolden or italicize any text.
                 """},
                {"role": "user", "content": prompt_avatar}
            ]
        }

        try:
            response = requests.post(self.url, json=payload, headers=headers)
            response.raise_for_status()
            response_text = response.json()["choices"][0]["message"]["content"]
            return self._clean_response(response_text)
        except Exception as e:
            print(f"Error calling Groq API: {e}")
            return None

    def _clean_response(self, response_text):
        """Clean the response text by removing unwanted elements."""
        # Remove think tags
        cleaned = re.sub(r"<think>.*?</think>", "", response_text, flags=re.DOTALL).strip()
        cleaned = cleaned.replace('*', '')
        
        # Remove emojis
        emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', cleaned) 