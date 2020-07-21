from tkinter import *
from PIL import ImageTk, Image
import speech_recognition as sr
from tkinter import messagebox
from control.VoiceController import VoiceController

class MainView:

        def exit(self):
            exit()

        def load(self):

            self.main=Tk()
            self.main.title("Voice Based Directory Search")
            self.main['background']='midnight blue'

            self.main.geometry("1080x550+0+0")
            self.main.resizable("False","False")


            self.bg = PhotoImage(file="views\ground.png")
            pic = PhotoImage(file = "views\mic.png")
            self.mic = pic.subsample(2,2)

            bg = Label(self.main,image=self.bg)
            bg.grid()

            title = Label(self.main,text="*VOICE BASED DIRECTORY SEARCH APP*",font=("Helvetica",21,"bold"),bg="midnight blue",fg="SlateBlue1",bd=7,relief=RAISED)
            title.place(x=0,y=0,relwidth=1)

            MicFrame = Frame(self.main,bg="midnight blue")
            MicFrame.place(x=300,y=120)

            l1 = Label(MicFrame,text = "INSTRUCTIONS\n1.ASK FOR EITHER ONLINE OR OFFLINE\n 2.TRY 'OPEN DOCUMENTS' OR 'GOOGLE.COM'",bg="midnight blue",fg="SlateBlue1",font=("Times 10 bold", 18))
            l1.grid(row=0,column=0)

            l2 = Label(MicFrame,text="click the mic and ask for your choice ",fg="SlateBlue1",bg="midnight blue",font=("Helvetica", 15))
            l2.grid(row=1,column=0)

            def voice():

                vc = VoiceController()

                go_ahead = Label(MicFrame,text="Go Ahead,we are listening!",font=("Times 10",15),fg="SlateBlue1",bg="midnight blue").grid(row=3,column=0,padx=10,pady=5)
                messagebox.showinfo('Speak...',"waiting for your command")
                
                res1=vc.user_command()

                fc = Label(MicFrame,text="You : "+res1,font=("Times 10",15),fg="SlateBlue1",bg="midnight blue").grid(row=4,column=0,padx=15,pady=15)
                

                messagebox.showinfo('Speak...',"waiting for your command")

                res2=vc.user_command()

                fc = Label(MicFrame,text="You : "+res2,font=("Times 10",15),fg="SlateBlue1",bg="midnight blue").grid(row=5,column=0,padx=15,pady=15)
                
                if res1 == "offline":
                    try:
                        vc.open_func(res2)
                    except:
                        messagebox.showinfo('Sorry!',"No application Found.")  
                else:
                    try:
                        vc.online(res2)
                    except:
                        messagebox.showinfo('Sorry!',"Try again")


            b1 = Button(MicFrame,image = self.mic,command = voice,width=85,height=85,font=("Helvetica",14,"bold"),bg="midnight blue",fg="SlateBlue1",bd=3,relief=RAISED)
            b1.grid(row=6,column=0) 
            
            b2 = Button(MicFrame,text="EXIT",command=self.exit,width=5,font=("Helvetica",14,"bold"),bg="midnight blue",fg="SlateBlue1",bd=3,relief=RAISED)
            b2.grid(row=7,column=0)



            self.main.mainloop()

if __name__ == '__main__':

    mv = MainView()
    mv.load()
