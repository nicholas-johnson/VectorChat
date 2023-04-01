# import tkinter as tk
# import sounddevice as sd
# from scipy.io.wavfile import write
# import threading
# import time

# class RecorderWindow:
#     def __init__(self, callback):
#         self.callback = callback
#         self.recording = False
#         self.audio_data = None

#         # Initialize the tkinter window
#         self.window = tk.Tk()
#         self.window.title("Recorder")

#         self.record_button = tk.Button(self.window, text="Start Recording", command=self.toggle_recording)
#         self.record_button.pack()

#     def toggle_recording(self):
#         if not self.recording:
#             self.start_recording()
#         else:
#             self.stop_recording()

#     def start_recording(self):
#         self.recording = True
#         self.record_button.config(text="Stop Recording")
#         self.audio_data = sd.rec(frames=44100, samplerate=44100, channels=1, blocking=False)

#     def stop_recording(self):
#         sd.stop()
#         self.recording = False
#         self.record_button.config(text="Start Recording")
#         write("output.wav", 44100, self.audio_data)

#         # Call the callback with the recorded file path
#         self.callback("output.wav")

#     def run(self):
#         self.window.mainloop()


import tkinter as tk
from audio_recorder import AudioRecorder  # Import the AudioRecorder class from your audio_recorder.py file
from whisper_asr import WhisperASR 

class RecorderWindow:
    def __init__(self, callback):
        self.recorder = AudioRecorder()
        self.whisper_asr = WhisperASR()
        self.is_recording = False

        self.callback = callback
        
        self.window = tk.Tk()
        self.window.title("Audio Recorder")
        self.window.geometry("300x200")

        self.record_button = tk.Button(self.window, text="Start Recording", command=self.toggle_recording)
        self.record_button.pack(pady=20)

    def toggle_recording(self):
        if not self.is_recording:
            self.recorder.start()
            self.record_button.config(text="Stop Recording")
            self.is_recording = True
        else:
            self.recorder.stop()
            self.record_button.config(text="Start Recording")
            self.is_recording = False

            # Call the callback with the recorded file path
            self.callback("output.wav")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    window = tk.Tk()
    app = RecorderWindow(window)
    window.mainloop()
