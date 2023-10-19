import tkinter

class Button_GUI:
    def __init__(self):
        self.mw = tkinter.Tk()

        self.button1 = tkinter.Button(self.mw, text="Button 1", command=self.function_1)
        self.button2 = tkinter.Button(self.mw, text="Button 2", command=self.function_2)
        self.button1.pack(side="left")
        self.button2.pack(side="left")
        tkinter.mainloop()

    def function_1(self):
        print("Button 1 is clicked")

    def function_2(self):
        print("Button 2 is clicked")

# Create an instance of the Button_GUI class and assign it to a variable
gui = Button_GUI()