import speech_recognition as sr
import os
import webbrowser as wb
import time
from tkinter import messagebox

class VoiceController:

    try:
        def user_command(self):
            cobj=sr.Recognizer()
            cmd=''
            with sr.Microphone() as source:
                cmd=cobj.listen(source,phrase_time_limit=3)
                inp = cobj.recognize_google(cmd)
                return inp
    except sr.RequestError as e:
        messagebox.showinfo('Error!','Try Again!')       
        print('voice is not audible\n Error : '+e)


    #function used to open something online
    def online(self,inp):
            wb.open(inp.lower())
            return
            
# function to search path 
    def path(self,fts):
            res_path = os.path.join(os.path.join(os.environ['USERPROFILE']), fts)
            os.startfile(res_path)

# function used to open application or folder
    def open_func(self,inp): 
            inp = inp.lower()

            if "d drive" in inp:
                os.startfile(r'D:\\')

            elif "c drive" in inp:
                os.startfile(r'C:\\')

            elif "desktop" in inp:
                self.path('Desktop')
            
            elif "documents" in inp:
                self.path('Documents')

            elif "downloads" in inp:
                self.path('Downloads')
        
            elif "pictures" in inp:
                self.path('Pictures')

            elif "firefox" in inp:
                os.startfile(r'C:\Program Files\Mozilla Firefox\\firefox.exe')

            elif "chrome" in inp:
                os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

            elif "word" in inp:
                os.startfile(r'C:\Program Files (x86)\Windows NT\Accessories\wordpad.exe')

            elif "excel" in inp:
                os.startfile(r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE')

            else :
                messagebox.showinfo('Sorry!',"No application Found.")  
            return 
  
if __name__== "__main__":

    vc = VoiceController()