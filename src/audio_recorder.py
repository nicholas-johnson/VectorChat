import sounddevice as sd
import numpy as np
import threading
import wave
import time

class AudioRecorder:
    def __init__(self, output_filename="output.wav", channels=1, rate=44100, chunk=1024, dtype='int16'):
        self.output_filename = output_filename
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.dtype = dtype
        self._buffer = np.zeros((0, self.channels), dtype=self.dtype)
        self._is_recording = False
        self._recording_thread = None

    def _record(self):
        with sd.InputStream(samplerate=self.rate, channels=self.channels, dtype=self.dtype, blocksize=self.chunk, callback=self._callback):
            while self._is_recording:
                sd.sleep(100)

    def _callback(self, indata, frames, time, status):
        if self._is_recording:
            self._buffer = np.concatenate((self._buffer, indata))

    def start(self):
        if not self._is_recording:
            self._buffer = np.zeros((0, self.channels), dtype=self.dtype)
            self._is_recording = True
            self._recording_thread = threading.Thread(target=self._record)
            self._recording_thread.start()

    def stop(self):
        if self._is_recording:
            self._is_recording = False
            self._recording_thread.join()
            self._save_wav()

    def _save_wav(self):
        with wave.open(self.output_filename, "wb") as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self._buffer.dtype.itemsize)
            wf.setframerate(self.rate)
            wf.writeframes(self._buffer.tobytes())

# Example usage:
recorder = AudioRecorder()
recorder.start()
time.sleep(1)  # Pause for one second
recorder.stop()