import pyttsx3
import PyPDF2
import time
book = open('secret.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
speaker.setProperty('rate', 120)
speaker.setProperty('volume', 2.0)
propertyName = input("Enter property name: ")
propertyValue = input("Enter property value: ")
speaker.setProperty(propertyName, propertyValue)
for i in range(pages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
    speaker.stop()
    speaker.save_to_file(text, 'audio.mp3')
    speaker.runAndWait()