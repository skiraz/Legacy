from customtkinter import *
from customtkinter import CTkButton as Button
from customtkinter import CTk as Tk
from customtkinter import CTkToplevel as Toplevel
from customtkinter import CTkProgressBar 
from threading import Thread

class LoadingWindow:
    def __init__(self, root):
        self.root = root
        self.loading_window = None
        self.i = 5
        self.maximum=100
        self.close = 0

    def create_loading_window(self):
        self.loading_window = Toplevel()
        self.loading_window.title("Loading...")
        self.loading_window.geometry("300x50")

        # Progress bar 
        self.progress_var = IntVar()
        self.progress_bar = CTkProgressBar(self.loading_window, variable=self.progress_var)
        self.progress_bar.pack(fill=BOTH, expand=True)

        # Start the loading process
        
        self.loading_thread = Thread(target=self.simulate_loading)
        self.loading_thread.start()

    def simulate_loading(self):
        sum=0
        while 1:
            print(self.close)
            if not self.close and sum<self.maximum/2:
                self.progress_var.set(sum)
                self.loading_window.update()
                self.loading_window.after(100)  # Simulate some loading work (e.g., time-consuming task)
                sum+=self.i
            elif self.close:
                self.progress_var.set(sum)
                self.loading_window.update()
                self.loading_window.after(50)
                sum+=self.i
            

        self.loading_window.destroy()

        # Execute the task function when loading is done
        

    def start_loading(self):
        if not self.loading_window:
            self.create_loading_window()

    def close_loading(self):
        print(0)
        self.close=1
        if self.loading_window:
            self.loading_window.destroy()
        self.loading_thread.join()

# Example usage:
if __name__ == "__main__":
    def my_task():
        # Replace this with your actual task after loading is complete
        print("Loading complete. Performing the main task.")

    root = Tk()
    from time import sleep
    root.update()
    sleep(1)
    loading_window = LoadingWindow(root)
    loading_window.start_loading()

    root.mainloop()
