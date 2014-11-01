import src.midi
import subprocess
import shlex
import os


class ValuesOfMidiFile(object):
    def __init__(self, filename):
        self.file = open(filename)

    def checkPitch(self):
        for line in self.file:
            check = line.split("(")
            while check[0] !=  "midi.ControlChangeEvent" and check[0] != "midi.ProgramChangeEvent" :
                tmp = line.split("data=[")
                extractData = tmp[1]
                pitch = extractData[0:2]
                return pitch

    def checkTempo(self):   
        counter = 0
        arr = []
        for line in self.file:
            check = line.split("(")
            while check[0] != "midi.ControlChangeEvent" and check[0] != "midi.ProgramChangeEvent" :
                tmp = line.split("tick=")
                extractData = tmp[1]
                if arr[counter] != arr[counter-1]:
                    arr += int(extractData[0:2])
                counter+=1
        lastEl = arr[-1]


        
                


class MidiToNotesConverter(object):
    
    def __init__(self, filename):
        self.file = open(filename)

    def matchPitchToNote(self,lilypondFilename):
        self.file = open(filename)
        with open("lilypondFilename","w") as f:
            f.write("hello\n")
        
            pitch = ValuesOfMidiFile.checkPitch()
            listNotes = ["C","C#", "D","D#","E","F","F#","G","G#","A","A#","B"]


            if pitch % 12 == 8:
                fileInput.write("\relative \{ %s \}"%listNodes[0])

#            cmd = "\relative \{ {note} \} ".format(note = listNotes[0])
#            subprocess.Popen(shlex.split(cmd))
#        elif pitch % 12 == 1:
#            cmd = "\relative \{ {note} \} ".format(note = listNotes[1])
#            subprocess.Popen(shlex.split(cmd))
#        elif pitch % 12 == 2:
#            cmd = "\relative \{ {note} \} ".format(note = listNotes[2])
#            subprocess.Popen(shlex.split(cmd))
#        elif pitch % 12 == 3:
#            cmd = "\relative \{ {note} \} ".format(note = listNotes[3])
#            subprocess.Popen(shlex.split(cmd))
#        elif pitch % 12 == 4:
#            cmd = "\relative \{ {note} \} ".format(note = listNotes[4])
#            subprocess.Popen(shlex.split(cmd))
#        elif pitch % 12 == 5:
#            cmd = "\relative \{ {note} \} ".format(note = listNotes[5])
#            subprocess.Popen(shlex.split(cmd))
#        elif pitch % 12 == 6:
#            cmd = "\relative \{ {note} \} ".format(note = listNotes[6])
#            subprocess.Popen(shlex.split(cmd))
#        elif pitch % 12 == 7:
#            cmd = "\relative \{ {note} \} ".format(note = listNotes[7])
#            subprocess.Popen(shlex.split(cmd))
#        elif pitch % 12 == 8:
#            cmd = "\relative \{ {note} \} ".format(note = listNotes[8])
#            subprocess.Popen(shlex.split(cmd))

#        elif pitch % 12 == 9:
#            cmd = "\relative \{ {note} \} ".format(note = listNotes[9])
#            subprocess.Popen(shlex.split(cmd))
#        elif pitch % 12 == 10:
#            cmd = "\relative \{ {note} \} ".format(note = listNotes[10])
#            subprocess.Popen(shlex.split(cmd))
#        elif pitch % 12 == 11:
#            cmd = "\relative \{ {note} \} ".format(note = listNotes[11])
#            subprocess.Popen(shlex.split(cmd))




                    ##TODO: call some other function that changes into notes 

        

converter = ValuesOfMidiFile('test')
sumTotal = MidiToNotesConverter('test')
converter.checkPitch()
sumTotal.matchPitchToNote("lilyP")
