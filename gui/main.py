from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
from arduino.gui import arduinoWindow


class App():
    def __init__(self,width = 600,height = 600):
      self.window = Tk()
      self.width = width
      self.height = height
      self.window.geometry(f"{self.width}x{self.height}")
      self.window.title("legacy")
      self.ardrun = 0 


    def run(self):
         self.arduino_Btn()
         mainloop()
      
      
    
    def arduino_Btn(self):
            window = arduinoWindow()
            B = Button(self.window, text ="Arduino", command = window.run)
            B.place(x=50,y=50)

