
#!/usr/bin/env python
import midi

class MidiGenerator(object):
    def __init__(self,resolution,format):
        self.pattern=midi.Pattern([],resolution,format,False)
    
    def save(self,filename):
        self.pattern.make_ticks_rel()
        midi.write_midifile(filename,self.pattern)
    
    def addChannel(self,channel):
        self.pattern.append(channel.track)

class Channel(object):
    def __init__(self):
        self.track = midi.Track([],False)

    def addNote(self,note):
        self.track.append(midi.NoteOnEvent(tick=note.start, velocity=127, pitch=note.pitch))
        self.track.append(midi.NoteOffEvent(tick=note.end, velocity=0, pitch=note.pitch))
    
    def endTrack(self):
        x = 0
        for note in self.track:
            if note.tick > x:
                x = note.tick
        self.track.append(midi.EndOfTrackEvent(tick = x))

class Note(object):
    def __init__(self,pitch,start,end):
        self.pitch=pitch
        self.start=start
        self.end=end

   
