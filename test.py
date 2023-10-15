import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class Tab:
    def __init__(self, notebook:ttk.Notebook):
        self.filename = None
        self.notebook = notebook

        self.text_widget = tk.Text(self.notebook)
        self.text_widget.bind("<Control-o>", self.open)
        self.text_widget.bind("<Control-s>", self.save)
        self.text_widget.bind("<Control-Shift-S>", self.saveas)
        self.notebook.add(self.text_widget, text="The tab name")

    def open(self, _=None):
        filename = filedialog.askopenfilename()
        if filename != "":
            with open(filename, "r") as file:
                data = file.read()
            self.text_widget.delete("0.0", "end")
            self.text_widget.insert("end", data)
            self.filename = filename
        return "break"

    def save(self, _=None):
        if self.filename is None:
            self.saveas()
        else:
            self._save()
        return "break"

    def saveas(self, _=None):
        filename = filedialog.asksaveasfilename()
        if filename == "":
            return "break"
        self.filename = filename
        self._save()

    def _save(self):
        assert self.filename is not None, "self.filename shouldn't be None"
        data = self.text_widget.get("0.0", "end")
        with open(self.filename, "w") as file:
            file.write(data)


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.new_tab_button = tk.Button(self.root, text="New tab", command=self.add_new_tab)
        self.new_tab_button.pack()
        self.open_button = tk.Button(self.root, text="Open file", command=self.open_file)
        self.open_button.pack()
        self.save_button = tk.Button(self.root, text="Save file", command=self.save_file)
        self.save_button.pack()
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()
        self.tabs = []

    def add_new_tab(self):
        tab = Tab(self.notebook)
        self.tabs.append(tab)

    def get_current_tab(self):
        # This code gets the currently selected tab
        idx = self.notebook.index(self.notebook.select())
        tab = self.tabs[idx]
        return tab

    def open_file(self):
        tab = self.get_current_tab()
        tab.open() # Call `open` on the tab

    def save_file(self):
        tab = self.get_current_tab()
        tab.save() # Call `save` on the tab

    def mainloop(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.mainloop()