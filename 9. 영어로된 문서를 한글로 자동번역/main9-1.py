import googletrans 

class Translator:

    def __init__(self):
        self.text = ''
        self.read_path = ''
        self.write_path = ''
        self.translator = googletrans.Translator()

    def set_text(self, text):
        self.text = text

    def set_read_path(self, path):
        self.read_path = path

    def set_write_path(self, path):
        self.write_path = path

    def en_to_kr(self):
        #str2 = "I am happy"
        result2 = self.translator.translate( self.text, dest='ko', src='en')
        return result2.text

    def en_to_kr_file(self):
        with open(self.read_path, 'r') as f:
            readLines = f.readlines()

        for lines in readLines:
            result1 = self.translator.translate(lines, dest='ko')
            print(result1.text)
            with open(self.write_path, 'a', encoding='UTF8') as f:
                f.write(result1.text + '\n')

    def kr_to_en_file(self):
        with open(self.read_path, 'r') as f:
            readLines = f.readlines()

        for lines in readLines:
            result1 = self.translator.translate(lines, dest='en')
            print(result1.text)
            with open(self.write_path, 'a', encoding='UTF8') as f:
                f.write(result1.text + '\n')

if __name__ == '__main__':
    t = Translator()

    while 1:
        menu = input('0:종료 1:EN->KR 2:KR->EN 3:영어파일->한글 4:한글파일->영어')
        if menu == '0':
            print('프로그램 종료')
            break
        elif menu == '1':
            text = input('번역할 영문을 입력하세요.')
            t.set_text(text)
            c = t.en_to_kr()
            print(f'번역결과 : {c}')
        elif menu == '2':
            text = input('번역할 한글을 입력하세요.')
            t.set_text(text)
            c = t.kr_to_en()
            print(f'번역결과 : {c}')
        elif menu == '3':
            path = input('번역할  영어파일을 입력하세요.')
            write_path = input('번역결과 저장 파일 경로 : ')
            t.set_read_path(path)
            t.set_write_path(write_path)
            t.en_to_kr_file()
        elif menu == '4':
            path = input('번역할  한글파일을 입력하세요.')
            write_path = input('번역결과 저장 파일 경로 : ')
            t.set_read_path(path)
            t.set_write_path(write_path)
            t.kr_to_en_file()
        else:
            print('메뉴에 없는 항목입니다')
            continue




