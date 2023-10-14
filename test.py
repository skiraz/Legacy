import tkinter as tk

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")
        
        self.open_child_button = tk.Button(root, text="Open Child Window", command=self.open_child_window)
        self.open_child_button.pack()

        self.child_windows = []

    def open_child_window(self):
        child_window = tk.Toplevel(self.root)
        child_window.title("Child Window")

        close_button = tk.Button(child_window, text="Close", command=lambda: self.close_child_window(child_window))
        close_button.pack()

        self.child_windows.append(child_window)

    def close_child_window(self, child_window):
        child_window.destroy()
        self.child_windows.remove(child_window)

if __name__ == "__main__":
    root = tk.Tk()
    main_window = MainWindow(root)
    root.mainloop()