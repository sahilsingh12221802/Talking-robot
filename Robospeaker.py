import os
from gtts import gTTS

def speak(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("temp.mp3")
    os.system("afplay temp.mp3")

if __name__ == '__main__':
    print("Welcome to your robot assistant 1.0, Created by Sahil. Type Whatever you want me to speak.")
    speak("Welcome to your robot assistant 1.0, Created by Sahil. Type Whatever you want me to speak", lang='en')

    while True:
        user_input = input("Enter what you want me to speak: ")
        if user_input.lower() == 'q':
            speak('Bye bye, I take your leave.', lang='en')
            break

        lang = 'hi'  
        speak(user_input, lang=lang)
