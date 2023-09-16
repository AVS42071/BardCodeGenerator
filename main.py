import http.server
import socketserver
import tkinter as tk
import GitHubCodeEditor

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create a GitHubCodeEditor instance.
        github_code_editor = GitHubCodeEditor()

        # Start the mainloop.
        self.mainloop()

if __name__ == '__main__':
    myapp = MyApp()
