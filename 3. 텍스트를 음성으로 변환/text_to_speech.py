from gtts import gTTS
from playsound import playsound
# pip install playsound==1.2.2

#import 에러나면 터미널에서 pip install gTTS 입력하면 설치 됨.
class TextToSpeech:
    def __init__(self):
        self.text = ""

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def save_mp3(self, title):
        #tts.save(r"3. 텍스트를 음성으로 변환\hi.mp3")
        tts = gTTS(text=self.text, lang = 'ko')
        tts.save(f"./{title}.mp3")

if __name__ == '__main__':
    t = TextToSpeech()
    title = input('변환하려는 파일명을 입력하세요.')
    text = input('변환하려는 문장을 입력하세요.')
    t.set_text(text)
    t.save_mp3(title)

    playsound(f"./{title}.mp3")
