#!/usr/bin/env python

"""Frequency manager."""

from mic import Mic
import numpy as np
import pylab as pl


class FrequencyStream(object):

    """Frequency stream."""

    def __init__(self):
        """Construct FrequencyStream object."""
        self.mic = Mic('Blue Snowball')

    def __enter__(self):
        """Open and return frequency stream."""
        self.mic.open()
        return self

    def __exit__(self, type, value, traceback):
        """Close stream."""
        self.mic.close()

    def fft(self, data, jump):
        """Return data in frequency domain."""
        #cut up data
        #start frame
        start = 0
        #go until interval reaches final frame
        while start+8192 < len(data):
            #get fft of interval
            freq = np.absolute(np.fft.rfft(data[start:start+8192]))
            #send out fft
            yield freq
            #move to next interval
            start += jump
	

    def read(self, jump, frames=None):
        """Read a number of frames of data into the stream."""
        #read all frames
        self.mic.read(frames)
        #iterate through buffers
        for buff in self.fft(self.mic.stream.channel_1,jump):
            yield buff


def main():
    """Plot one second of data in the frequency domain."""
    with FrequencyStream() as stream:
        stream.read()
        pl.subplot(2, 1, 1)
        pl.plot(stream.channel_1)
        pl.subplot(2, 1, 2)
        pl.plot(stream.channel_2)
        pl.show()


if __name__ == '__main__':
    main()
