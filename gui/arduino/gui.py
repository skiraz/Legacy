from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
import pyfirmata

class arduinoWindow():
    def __init__(self, width=600, height=600):
        self.width = width
        self.height = height
        self.window = None
        self.led_states = {}  # Dictionary to track LED states


    def init_pyfirmat(self):
        # TODO: grab the serial port the arduino is on automatically  
        self.board = pyfirmata.Arduino('COM4')



    def create_window(self):
        self.window = Toplevel()
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.title("arduino")
        self.window.protocol("WM_DELETE_WINDOW", self.on_window_close)

    def run(self):
        if self.window is None:
            self.create_window()
        self.init_pyfirmat()
        self.add_led_buttons()
        self.window.mainloop()
    def hand_gesture_led(self):
        def hands():
            pass
        button = Button(self.window,text=f"Hand Gesture", command=hands)
        button.pack()

        


    def on_window_close(self):
        # This method is called when the Toplevel window is closed
        self.window.destroy()
        self.window = None
        self.__del__()
    
    def add_led_buttons(self):
        # Create buttons for each LED
        for led_id in range(2, 7):  # Assuming you have 3 LEDs (change the range accordingly)
            self.led_states[led_id] = 0  # Initialize LED states to off
            button = Button(self.window,text=f"LED {led_id}", command=lambda id=led_id: self.toggle_led(id))
            button.pack()

    def toggle_led(self, led_id):
        if led_id in self.led_states:
            if self.led_states[led_id]:
                # Turn the LED off (replace this with your actual LED control logic)
                print(f"LED {led_id} Off")
                self.led_states[led_id] = 0
            else:
                # Turn the LED on (replace this with your actual LED control logic)
                print(f"LED {led_id} On")
                self.led_states[led_id] = 1

            self.board.digital[led_id].write(self.led_states[led_id])
    def turnOn(self,pin):
        pass
    def turn_all_leds_off(self):
        for led_id in self.led_states:
            self.board.digital[led_id].write(0)
        
    def __del__(self):
        self.turn_all_leds_off()








    
            
