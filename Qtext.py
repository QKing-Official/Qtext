import tkinter as tk
from tkinter import filedialog

class TextEditor:

    def __init__(self, root):
        self.root = root
        self.root.title('Simple Text Editor')
        self.text_widget = tk.Text(self.root, wrap='word')
        self.text_widget.pack(expand=True, fill='both')
        self.file_path = None
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label='New', command=self.new_file)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_command(label='Save As', command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.root.quit)
        menubar.add_cascade(label='File', menu=file_menu)
        self.root.config(menu=menubar)

    def new_file(self):
        self.text_widget.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(tk.END, content)
            self.file_path = file_path

    def save_file(self):
        if not self.file_path:
            self.save_as_file()
            return
        content = self.text_widget.get(1.0, tk.END)
        with open(self.file_path, 'w') as file:
            file.write(content)

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if file_path:
            self.file_path = file_path
            content = self.text_widget.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(content)

def main():
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()
if __name__ == '__main__':
    main()
