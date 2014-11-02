#!/usr/bin/env python

"""Audio stream parser."""

import numpy as np


class Stream(object):

    """Dual-channel audio stream class."""

    def __init__(self, raw=None, dtype=np.float32):
        """Construct Stream object from raw audio data."""
        self.channel_1 = []
        self.channel_2 = []
        self.dtype = dtype
        if raw:
            self.append(raw)

    def parse(self, raw):
        """Parse incoming raw stream."""
        data = np.fromstring(raw, dtype=self.dtype)
        return data

    def append(self, raw):
        """Append audio stream into separate channels."""
        data = self.parse(raw)
        self.channel_1.extend(data[::2])
        self.channel_2.extend(data[1::2])
