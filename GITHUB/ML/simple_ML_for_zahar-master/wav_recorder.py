import pyaudio
import wave
from array import array
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100


def record(filename):
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []
    start_time = time.time()
    silent = True
    silent_chuncks = []
    while True:
        data = stream.read(CHUNK)
        data_chunk = array('h', data)
        if max(data_chunk) > 400:
            silent = False
            silent_chuncks.clear()
        else:
            silent_chuncks.append(True)
        if len(silent_chuncks) >= 20:
            silent = True
        frames.append(data)
        if time.time() - start_time >= 5 and silent:
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
