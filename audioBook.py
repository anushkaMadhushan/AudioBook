import PyPDF2
import pyttsx3

Engine = pyttsx3.init()
PDF_Reader = PyPDF2.PdfFileReader(open("sample.pdf","rb"))
for Page_num in range(PDF_Reader.numPages):
    Text=PDF_Reader.getPage(Page_num).extractText()
    Engine.say(Text)
    Engine.runAndWait()
    #if you want Convert to audio file use below commands
    # Engine.save_to_file(Text,"audio.mp3")
    # Engine.runAndWait()