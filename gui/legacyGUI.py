from customtkinter import *
from customtkinter import CTkButton as Button
from arduino.arduinoGUI import arduinoWindow


class App():
    def __init__(self,width = 600,height = 600):
      self.window = CTk()
      self.width = width
      self.height = height
      self.window.geometry(f"{self.width}x{self.height}")
      self.window.title("legacy")
      


    def run(self):
         self.arduino_Btn()
         self.window.mainloop()
      
      
    
    def arduino_Btn(self):
            window = arduinoWindow()
            B = Button(self.window, text ="Arduino", command = window.run)
            B.place(x=50,y=50)

