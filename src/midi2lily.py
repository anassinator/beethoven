import midi
import subprocess
import shlex
import os

note_list = ["c","cis","d","dis","e","f","fis","g","gis","a","ais","b"]
        
class MidiParser(object):
    def __init__(self, filename):
        self.pattern = midi.read_midifile(filename)
#        self.pattern.make_ticks_abs()
    
    def getFilteredTrack(self,track_no):
        new_track = []
        for event in self.pattern[track_no]:
            if isinstance(event, midi.NoteOffEvent) or isinstance(event, midi.NoteOnEvent):
                new_track.append(event)
        return new_track

    def parseTrack(self,track):
        note = []
        lastTime=0
        for x in range(0,len(track),2):
            pauseDuration = track[x].tick - lastTime
            if pauseDuration !=0:
                note.append([-1,pauseDuration])
            #print track[x]
            #print track[x+1]
            lastTime = track[x+1].tick
            note.append([track[x].data[0], track[x+1].tick - track[x].tick])
        return note 
            




class LyGenerator():
    def __init__(self,note):
        self.note=note
        self.output = ""
        for x in note:
            self.output += LyGenerator.parseDuration(x[1], LyGenerator.parsePitchLetter(x[0]))

        

    @staticmethod        
    def parseDuration(duration, pitch_letter):
        for x in range(0,8):
            if duration >= 64*16/2**x:
                return "{letter}{x} {parsed}".format(
                    letter=pitch_letter, x = 2 ** x,
                    parsed=LyGenerator.parseDuration(duration - 64*16/(2**x),
                                                     pitch_letter)
                )
        return ""
    
    @staticmethod            
    def parsePitchLetter(note):
        if note == -1:
            return "r"
        else:
            return note_list[note%12] + LyGenerator.parseOctave(int(note/12)) 
    
    @staticmethod
    def parseOctave(octave):
        octave -= 4
        if octave > 0:
            return "\'" * octave
        else:
            return "," * abs(octave)

