import speech_recognition as sr
from googletrans import Translator, LANGUAGES
import random

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 请对着麦克风说话...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="zh-CN")
            print("🗣️ 识别结果：", text)
            return text
        except sr.UnknownValueError:
            print("❌ 无法识别，请再试一次。")
            return None
        except sr.RequestError:
            print("⚠️ 网络错误，请检查网络连接。")
            return None

def random_translate(text):
    translator = Translator()
    target_lang = random.choice(list(LANGUAGES.keys()))
    translated = translator.translate(text, dest=target_lang)
    print(f"🌍 随机语言: {LANGUAGES[target_lang].capitalize()}")
    print(f"💬 翻译结果: {translated.text}")

def main():
    print("🎧 VoiceCamTranslator 启动！")
    text = speech_to_text()
    if text:
        random_translate(text)

if __name__ == "__main__":
    main()

