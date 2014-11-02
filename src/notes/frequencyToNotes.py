from numpy import *
from matplotlib import pyplot as plt
from time import sleep
from audio.frequency import FrequencyStream
from midiGenerator import MidiGenerator, Channel, Note

frequencies = [65.40639132514966, 69.29565774421802, 73.41619197935191, 77.78174593052023, 82.4068892282175, 87.30705785825099, 92.4986056779086, 97.99885899543733, 103.8261743949863, 110.0, 116.54094037952248, 123.47082531403103, 130.8127826502993, 138.59131548843604, 146.8323839587038, 155.56349186104046, 164.813778456435, 174.61411571650194, 184.9972113558172, 195.99771799087466, 207.65234878997256, 220.0, 233.08188075904496, 246.94165062806206, 261.6255653005986, 277.1826309768721, 293.6647679174076, 311.1269837220809, 329.6275569128699, 349.2282314330039, 369.9944227116344, 391.99543598174927, 415.3046975799451, 440.0, 466.1637615180899, 493.8833012561241, 523.2511306011972, 554.3652619537442, 587.3295358348151, 622.2539674441618, 659.2551138257398, 698.4564628660078, 739.9888454232688, 783.9908719634985, 830.6093951598903, 880.0, 932.3275230361799, 987.766602512248, 1046.5022612023945, 1108.7305239074883, 1174.65907166963, 1244.5079348883237, 1318.5102276514797, 1396.9129257320155, 1479.9776908465376, 1567.981743926997, 1661.2187903197805, 1760.0, 1864.6550460723593, 1975.533205024496, 2093.004522404789, 2217.4610478149766, 2349.31814333926, 2489.0158697766474, 2637.020455302959, 2793.825851464031, 2959.955381693075, 3135.9634878539937, 3322.437580639561, 3520.0, 3729.3100921447185]
recording = True
uncombined = []

aud = FrequencyStream()
aud.mic.open()

start = 0
jump = 8192/128
qqq = [x for x in aud.read(jump,8192*5)]
for fre in qqq:
	
	goodFre = []
	good = []
	
	avg = sum(fre)/float(len(fre))
	#beams need to be above 
	threshold = avg * 8
	for x in range(1,8192/2):
		if fre[x] > threshold:
			#goodfre contains the freqency, and the amplitude
			goodFre.append([x,fre[x]])
		
	if not goodFre: #nothing above threshold
		continue
	
	#find closest one to each piano note, sum surrounding three,
	#find max

	
	for x in range(0,len(frequencies)): #go through each piano note
		closest = 1
		pos = -1
		for i in range(0,len(goodFre)):
			#difference between frequency and measured
			dist = abs(goodFre[i][0] - frequencies[x])
			if goodFre[i][0] > frequencies[x] + 0.5:
				break
			if dist < closest:
				closest = dist
				pos = i
		if closest <= 0.5: #if piano frequency has a close value
			oldPos = goodFre[pos][1]
			good.append([sum([fre[oldPos],fre[oldPos-1],fre[oldPos+1]]),x+1])#position of piano frequency + 1, and sum of 3 surrounding fft amplitudes
			#good.append([oldPos,x+1])
	
	if not good:
		continue
	
	good = sorted(good)
	
	
	#send all good
	for x in range(len(good)):
		uncombined.append([good[x][1]+35,start,start+jump])
	start += jump

aud.mic.close()
uncombined=sorted(uncombined)
noteSegment = 0
#combine notes next to eachother that are touching
while noteSegment < len(uncombined)-1:
	if uncombined[noteSegment][0] == uncombined[noteSegment+1][0]:
		if uncombined[noteSegment][2] >= uncombined[noteSegment+1][1] - 8192/16:
			uncombined[noteSegment][2] = uncombined[noteSegment+1][2]
			del uncombined[noteSegment+1]
			#delete everything in between
			
		else:
			noteSegment+=1
	else:
		noteSegment+=1
noteSegment = 0
combined = sorted(uncombined, key = lambda x:x[1])

streams = []
streams.append([combined[0]])
for x in combined[1:]:
	posed = False
	for stream in range(len(streams)):
		for note in streams[stream]:
			#test if overlap - smaller to larger so test if comes after
			if note[2] <= x[1]: #make sure right side is before left side
				streams[stream].append(x)
				posed = True
			if posed:
				break
			
		if posed:
			break
	else:
		streams.append([x])
			
		

"""
while noteSegment < len(uncombined)-1:
	for f in range(noteSegment+1,len(uncombined)):
		#check if ahead of segment, but not more than 3 ahead
		c = uncombined[f]
		d = uncombined[noteSegment]
		if c[0] != d[0]:
			continue
		if c[2] < d[1]: #check if in front
			if c[2]+3*128 >= d[1]: #check if in safe range
				c[2]=d[2] #extend time
				del uncombined[noteSegment]
				#delete everything in between
				if range(noteSegment+1,c):
					for between in range(noteSegment+1,c):
						del uncombined[between]
					
				
			else:
				break #ahead
	noteSegment += 1
"""

print streams
newCombinedStreams = []
for x in range(len(streams)):
	newCombinedStreams.append([])
	for y in streams[x]:
		newCombinedStreams[x].append(Note(y[0],y[1],y[2]))

newMidi = MidiGenerator(2048,1)
channels = [Channel() for x in range(len(streams))]

for x in range(len(streams)): #go through channels and streams
	 for y in newCombinedStreams[x]:
		channels[x].addNote(y)

for x in range(len(streams)):
	channels[x].endTrack()
	newMidi.addChannel(channels[x])
print newMidi.pattern
newMidi.save("new.midi")

