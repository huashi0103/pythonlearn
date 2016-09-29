from tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #self.helloLabel=Label(self,text='hello world')
        #self.helloLabel.pack()
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.quitButton=Button(self,text='hello',command=self.hello)
        self.quitButton.pack()

    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('message','hello,%s'%name)





app=Application()
app.master.title('hello world')
app.mainloop()
