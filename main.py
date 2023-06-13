import tkinter as tk
from tkinter import messagebox
from plyer import notification


class DangerousWritingPromptApp:

    WINDOW_BG = "#303030"
    TEXTBOX_FG = "#EEEEEE"
    TEXTBOX_BG = "#505050"
    BUTTON_FG = "#FFFFFF"
    BUTTON_BG = "#AA0000"
    INACTIVITY_TIMEOUT = 5000  # ms
    RED_TEXT_TIME = 3500  # ms

    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Dangerous Writing Prompt")
        self.window.geometry("900x600")
        self.window.configure(bg=self.WINDOW_BG)

        self.text_input = tk.Text(self.window,
                                  font=("Arial", 12),
                                  fg=self.TEXTBOX_FG,
                                  bg=self.TEXTBOX_BG,
                                  insertbackground="white",
                                  insertwidth=2,
                                  padx=10,
                                  pady=10)
        self.text_input.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        self.text_input.focus_set()

        button_frame = tk.Frame(self.window, bg=self.WINDOW_BG)
        button_frame.pack()

        info_button = tk.Button(button_frame,
                                text="?",
                                command=self.show_description,
                                bg=self.BUTTON_BG,
                                fg=self.BUTTON_FG,
                                relief=tk.FLAT)
        info_button.pack(side=tk.LEFT, pady=(0, 10))

        copy_button = tk.Button(button_frame,
                                text="Copy",
                                command=self.copy_button_on_press,
                                bg=self.BUTTON_BG,
                                fg=self.BUTTON_FG,
                                relief=tk.FLAT)
        copy_button.pack(side=tk.LEFT, pady=(0, 10), padx=(5, 0))

        self.typing_timer = None
        self.red_text_timer = None

        self.text_input.bind("<Key>", self.check_typing)

    def show_description(self):

        description = "This is a Dangerous Writing Prompt app, " \
                    "where if you stop typing, your progress will be lost " \
                    "after 5 seconds of inactivity."
        messagebox.showinfo("App Description", description)

    def delete_content(self):

        self.text_input.delete(1.0, tk.END)
        self.text_input.config(fg=self.TEXTBOX_FG)

    def red_text(self):

        self.text_input.config(fg="red")

    def start_typing_timer(self):

        if self.typing_timer or self.red_text_timer:
            self.window.after_cancel(self.typing_timer)
            self.window.after_cancel(self.red_text_timer)
            self.text_input.config(fg=self.TEXTBOX_FG)

        self.typing_timer = self.window.after(self.INACTIVITY_TIMEOUT,
                                              self.delete_content)
        self.red_text_timer = self.window.after(self.RED_TEXT_TIME,
                                                self.red_text)

    def check_typing(self, event):

        self.start_typing_timer()

    def copy_content(self):

        self.window.clipboard_clear()
        self.window.clipboard_append(self.text_input.get(1.0, tk.END))

    def show_toast(self):

        notification.notify(
            title="Toast Notification",
            message="This is a toast notification!",
            timeout=5
        )

    def copy_button_on_press(self):

        self.copy_content()
        self.show_toast()

    def run(self):

        self.window.mainloop()


if __name__ == "__main__":
    app = DangerousWritingPromptApp()
    app.run()
