#!/usr/bin/env python

"""Microphone audio stream."""

import pyaudio
import pylab as pl
from stream import Stream


class Mic(object):

    """Microphone class."""

    def __init__(self, name=None, fs=8192, buffersize=1024):
        """Construct Microphone object.

        name: name of the microphone
        """
        self.name = name
        self.audio = pyaudio.PyAudio()
        self.device = None
        self.stream = Stream()
        self.fs = fs
        self.buffersize = buffersize

    def __enter__(self):
        """Open and return microphone."""
        self.open()
        return self

    def __exit__(self, type, value, traceback):
        """Close microphone audio stream."""
        self.close()

    def open(self):
        """Open microphone of the specified name."""
        for i in range(self.audio.get_device_count()):
            device = self.audio.get_device_info_by_index(i)
            if device['name'] == self.name:
                self.device = self.audio.open(
                    format=pyaudio.paFloat32, channels=2,
                    input=True, rate=self.fs,
                    frames_per_buffer=self.buffersize,
                    input_device_index=device['index']
                )
                break
        else:
            self.device = self.audio.open(
                format=pyaudio.paFloat32, channels=2,
                input=True, rate=self.fs,
                frames_per_buffer=self.buffersize
            )

    def close(self):
        """Close audio streams."""
        self.audio.close(self.device)
        self.audio.terminate()

    def read(self, frames):
        """Read a number of frames of data into the stream."""
        raw = self.device.read(frames)
        self.stream = Stream(raw)


def main():
    """Plot one second of data in the time domain."""
    with Mic('Blue Snowball') as mic:
        mic.read(mic.fs)
        pl.subplot(2, 1, 1)
        pl.plot(mic.stream.channel_1)
        pl.subplot(2, 1, 2)
        pl.plot(mic.stream.channel_2)
        pl.show()


if __name__ == '__main__':
    main()
