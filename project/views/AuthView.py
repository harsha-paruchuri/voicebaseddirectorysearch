from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from control.AuthController import AuthController



class AuthView:

    def load (self):
        self.window=Tk()
        self.window.title("Authorisation")
        self.window['background']='midnight blue'

        self.window.geometry("1080x550+0+0")
        self.window.resizable("False","False")

        tab_control = ttk.Notebook(self.window,width=1080, height=529)

        self.login_tab = Frame(tab_control)
        self.register_tab = Frame(tab_control)
        tab_control.add(self.login_tab,text="LOGIN")
        tab_control.add(self.register_tab,text="REGISTER")
        

        self.login()
        self.register()

        tab_control.grid()
        
        self.window.mainloop()
        
    def login(self):

        window = self.login_tab

        self.bg_icon = PhotoImage(file="views/ground.png")
        self.user_icon = PhotoImage(file="views/user.png")
        self.pwd_icon = PhotoImage(file="views/pwd.png")
        self.name_icon = PhotoImage(file="views/name.png")

        bg_lbl = Label(window,image=self.bg_icon)
        bg_lbl.grid()

        title = Label(window,text="LOGIN",font=("Helvetica",21,"bold"),bg="midnight blue",fg="SlateBlue1",bd=7,relief=RAISED)
        title.place(x=0,y=0,relwidth=1)
        
        LoginFrame = Frame(window,bg="midnight blue")
        LoginFrame.place(x=350,y=170)

        icon = Label(LoginFrame,image=self.user_icon).grid(row=0,column=0,columns=2,pady=20)
       
        unl = Label(LoginFrame,text="Username",image=self.name_icon,compound=LEFT,font=("Helvetica",15,"bold"),bg="midnight blue",fg="SlateBlue1").grid(row=1,column=0,padx=20,pady=10)
        une = Entry(LoginFrame,bd=3,relief=GROOVE,font=("",15))
        une.grid(row=1,column=1) 

        
        pl = Label(LoginFrame,text="Password",image=self.pwd_icon,compound=LEFT,font=("Helvetica",15,"bold"),bg="midnight blue",fg="SlateBlue1").grid(row=2,column=0,padx=20,pady=10)
        pe = Entry(LoginFrame,show="*",bd=3,relief=GROOVE,font=("",15))
        pe.grid(row=2,column=1)

        btn1 = Button(LoginFrame,text="SIGN IN",width=15,font=("Helvetica",14,"bold"),bg="midnight blue",fg="SlateBlue1",bd=3,relief=RAISED,command=lambda: self.loginControl(une.get(),pe.get()))
        btn1.grid(row=3,column=1,sticky='news',padx=5,pady=5)

        btn2 = Button(LoginFrame,text="EXIT",command=self.exit,width=15,font=("Helvetica",14,"bold"),bg="midnight blue",fg="SlateBlue1",bd=3,relief=RAISED)
        btn2.grid(row=3,column=0,sticky='news',padx=5,pady=5)

    def register(self):

        window = self.register_tab

        self.bg = PhotoImage(file="views/ground.png")
        self.reg_icon = PhotoImage(file="views/reg.png")

        bg = Label(window,image=self.bg).grid()

        title = Label(window,text="REGISTER",font=("Helvetica",21,"bold"),bg="midnight blue",fg="SlateBlue1",bd=7,relief=RAISED)
        title.place(x=0,y=0,relwidth=1)
        
        RegisterFrame = Frame(window,bg="midnight blue")
        RegisterFrame.place(x=350,y=100)

        icon = Label(RegisterFrame,image=self.reg_icon).grid(row=0,column=0,columns=3,pady=20)


        nl = Label(RegisterFrame,text="Name",compound=LEFT,font=("Helvetica",15,"bold"),bg="midnight blue",fg="SlateBlue1")
        nl.grid(row=1,column=0)

        ne = Entry(RegisterFrame,bd=3,relief=GROOVE,font=("",15),width=10)
        ne.grid(row=1,column=1)

        el = Label(RegisterFrame,text="Email",compound=LEFT,font=("Helvetica",15,"bold"),bg="midnight blue",fg="SlateBlue1")
        el.grid(row=2,column=0)

        ee = Entry(RegisterFrame,bd=3,relief=GROOVE,font=("",15),width=10)
        ee.grid(row=2,column=1)

        phl = Label(RegisterFrame,text="phone",compound=LEFT,font=("Helvetica",15,"bold"),bg="midnight blue",fg="SlateBlue1")
        phl.grid(row=3,column=0)

        phe = Entry(RegisterFrame,bd=3,relief=GROOVE,font=("",15),width=10)
        phe.grid(row=3,column=1)

        ul = Label(RegisterFrame,text="username",compound=LEFT,font=("Helvetica",15,"bold"),bg="midnight blue",fg="SlateBlue1")
        ul.grid(row=4,column=0)

        ue = Entry(RegisterFrame,bd=3,relief=GROOVE,font=("",15),width=10)
        ue.grid(row=4,column=1)

        pl = Label(RegisterFrame,text="password",compound=LEFT,font=("Helvetica",15,"bold"),bg="midnight blue",fg="SlateBlue1")
        pl.grid(row=5,column=0)

        pe = Entry(RegisterFrame,show="*",bd=3,relief=GROOVE,font=("",15),width=10)
        pe.grid(row=5,column=1)
        

        btn3 = Button(RegisterFrame,text="SIGN UP",command = lambda: self.registerControl(ne.get(),phe.get(),ee.get(),ue.get(),pe.get()),width=15,padx=5,pady=5,compound=LEFT,font=("Helvetica",15,"bold"),bg="midnight blue",fg="SlateBlue1",bd=3,relief=RAISED)
        btn3.grid(row=6,column=1,sticky='news',padx=5,pady=5)

        btn4 = Button(RegisterFrame,text="EXIT",command=self.exit,width=15,font=("Helvetica",14,"bold"),bg="midnight blue",fg="SlateBlue1",bd=3,relief=RAISED)
        btn4.grid(row=6,column=0,sticky='news',padx=5,pady=5)

    def loginControl(self,username,password):
        ac = AuthController()
        msg = ac.login(username,password)
       
        if msg[0] == 1 :
            messagebox.showinfo('Welcome!',msg[1])
            self.window.destroy()
            self.transfer_control()
        
        else:
            messagebox.showinfo('Alert!',"User not found!")


    def registerControl(self,name,phone,email,username,password):
    
        ac = AuthController()
        message = ac.register(name,phone,email,username,password)
        messagebox.showinfo('Message', message)

    def exit(self):
        exit()

if __name__ == '__main__':
    av = AuthView()
    av.load()

