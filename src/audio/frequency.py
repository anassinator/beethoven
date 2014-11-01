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
        self.channel_1 = []
        self.channel_2 = []

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
        start = 0
        while start+1000 < len(data):
			freq = np.absolute(np.fft.rfft(data[start:start+1000]))
			yield freq
			start += jump
	
	def nextB(self):
		for buff in self.fft(self.mix.stream.channel_1,10)
			yield buff

    def read(self, frames=None):
        """Read a number of frames of data into the stream."""
        self.mic.read(frames)
        #self.channel_1 = self.fft(self.mic.stream.channel_1,10)
        #self.channel_2 = self.fft(self.mic.stream.channel_2,10)


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
