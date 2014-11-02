#!/usr/bin/env python

"""Frequency manager."""

from wavestream import Wave
from mic import Mic
import numpy as np
import pylab as pl


class FrequencyStream(object):

    """Frequency stream."""

    def __init__(self, audio_in):
        """Construct FrequencyStream object."""
        self.input = audio_in

    def __enter__(self):
        """Open and return frequency stream."""
        self.input.open()
        return self

    def __exit__(self, type, value, traceback):
        """Close stream."""
        self.input.close()

    def fft(self, data, jump):
        """Return data in frequency domain."""
        # cut up data
        # start frame
        start = 0
        # go until interval reaches final frame
        while start + 8192 <= len(data):
            # get fft of interval
            freq = np.absolute(np.fft.rfft(data[start:start+8192]))
            # send out fft
            yield freq
            # move to next interval
            start += jump

    def read(self, frames, jump=1024):
        """Read a number of frames of data into the stream."""
        # read all frames
        self.input.read(frames)
        # iterate through buffers
        for buff in self.fft(self.input.stream.channel_1, jump):
            yield buff


def main():
    """Plot one second of data in the frequency domain."""
    with FrequencyStream(Mic('1kHz.wav')) as freq:
        data = [i for i in freq.read(220500)][0]
        pl.subplot(2, 1, 1)
        pl.plot(freq.input.stream.channel_1)
        pl.subplot(2, 1, 2)
        pl.plot(data)
        pl.show()


if __name__ == '__main__':
    main()
