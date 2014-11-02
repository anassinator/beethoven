#!/usr/bin/env python

"""Wave Stream."""

import wave
import numpy as np
import pylab as pl
from stream import Stream


class Wave(object):

    """Wave class."""

    def __init__(self, filename):
        """Construct Wave object.

        filename: path to .wav file
        """
        self.filename = filename
        self.wav = None
        self.dtype = None
        self.stream = None

    def __enter__(self):
        """Open and return wave."""
        self.open()
        return self

    def __exit__(self, type, value, traceback):
        """Close wave audio stream."""
        self.close()

    def get_dtype(self):
        """Get data type for processing."""
        if self.wav.getsampwidth() == 1:
            return np.dtype(np.uint8)
        elif self.wav.getsampwidth() == 2:
            return np.dtype(np.int16)
        elif self.wav.getsampwidth() == 4:
            return np.dtype(np.int32)
        else:
            raise ValueError('Unsupported format')

    def open(self):
        """Open specified wave file."""
        self.wav = wave.open(self.filename, 'rb')
        self.dtype = self.get_dtype()

    def close(self):
        """Close wave file."""
        self.wav.close()

    def read(self, frames):
        """Read a number of frames of data into the stream."""
        raw = self.wav.readframes(frames)
        self.stream = Stream(raw, self.dtype)


def main():
    """Plot one second of data in the time domain."""
    with Wave('1kHz.wav') as wav:
        wav.read(8192)
        pl.subplot(2, 1, 1)
        pl.plot(wav.stream.channel_1)
        pl.subplot(2, 1, 2)
        pl.plot(wav.stream.channel_2)
        pl.show()


if __name__ == '__main__':
    main()
