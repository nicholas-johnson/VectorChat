import tkinter as tk

class RecorderWindow:
    def __init__(self, on_start_recording, on_stop_recording, on_close):
        self.is_recording = False

        self.on_start_recording = on_start_recording
        self.on_stop_recording = on_stop_recording
        self.on_close = on_close
        
        self.window = tk.Tk()
        self.window.title("Vector Chat")
        self.window.geometry("600x400")

        self.record_button = tk.Button(self.window, text="Talk to Vector", command=self.toggle_recording)
        self.record_button.pack(pady=20)

        self.text = tk.Text(self.window, state='disabled', wrap="word", width=400, height=400)
        self.text.pack(padx=20, pady=20)
        self.log('...')

        self.window.protocol("WM_DELETE_WINDOW", self.close)

    def toggle_recording(self):
        if not self.is_recording:
            self.record_button.config(text="Stop Talking")
            self.is_recording = True
            self.on_start_recording()
        else:
            self.record_button.config(text="Talk to Vector")
            self.is_recording = False
            self.on_stop_recording()

    def log(self, text):
        self.text.configure(state='normal')
        self.text.delete(1.0, "end")
        self.text.insert('end', text)
        self.text.see('end')
        self.text.configure(state='disabled')

    def close(self):
        self.on_close()
        self.window.destroy()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    window = tk.Tk()
    app = RecorderWindow(window)
    window.mainloop()
