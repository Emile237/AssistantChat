from dotenv import load_dotenv
from src.voiceText import VoiceText
from gtts import gTTS
import os
from src.chatgpt import ChatGPT

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("CHATGPT_API_KEY")
    chat_gpt = ChatGPT(api_key)

    voice_text = VoiceText(language='fr-FR')
    user_message = voice_text.listen()
    
    print("Votre question est :"+user_message)
    response = chat_gpt.get_response(user_message)
    print(response)

    language = 'fr'
    tts = gTTS(text=response, lang=language)
    tts.save("welcome.mp3")
    os.system("welcome.mp3")
