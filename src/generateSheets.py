import midi2lily
import subprocess
import shlex

def makePDF (filename,out):
	parser = midi2lily.MidiParser(filename+".midi")
	f = open(out+".ly",'w')
	f.write("\\version \"2.16.2\"\n")
	for x in range(len(parser.pattern)):
	    track= parser.getFilteredTrack(x)
	    note_list = parser.parseTrack(track)
	    #print note_list
	    if note_list:
		output = midi2lily.LyGenerator(note_list).output
		f.write("\\new Staff {\n")
		f.write(output)
		f.write("\n}\n\n")
	cmd = "lilypond " + out + ".ly"
	print cmd
	subprocess.Popen(shlex.split(cmd))

