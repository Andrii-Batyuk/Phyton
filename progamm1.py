import Tkinter

app = Tkinter.Tk()
app.title("hello world")
app.minsize(300, 300)
helloLabel = Tkinter.Label(app, text="hello GUI")
helloLabel.pack()

app.mainloop()