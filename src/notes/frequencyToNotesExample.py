from numpy import *
from matplotlib import pyplot as plt
from time import sleep

def frange(x,y,jump):
	while x<y:
		yield x
		x+=jump

frequencyMin = 65.406391325149658
frequencyMax = 3520
disMin = [50.*sin(2.*frequencyMin*pi*(x/1000.))+50. for x in frange(0.,1000.,0.125)]
disMax = [50.*sin(2.*frequencyMax*pi*(x/1000.))+50. for x in frange(0.,1000.,0.125)]

freMin = absolute(fft.fft(disMin)[:4001])
freMax = absolute(fft.fft(disMax)[:4001])

recording = True
start = 0
while recording:
	goodFreMin = []
	goodFreMax = []

	frequencies = [65.40639132514966, 69.29565774421802, 73.41619197935191, 77.78174593052023, 82.4068892282175, 87.30705785825099, 92.4986056779086, 97.99885899543733, 103.8261743949863, 110.0, 116.54094037952248, 123.47082531403103, 130.8127826502993, 138.59131548843604, 146.8323839587038, 155.56349186104046, 164.813778456435, 174.61411571650194, 184.9972113558172, 195.99771799087466, 207.65234878997256, 220.0, 233.08188075904496, 246.94165062806206, 261.6255653005986, 277.1826309768721, 293.6647679174076, 311.1269837220809, 329.6275569128699, 349.2282314330039, 369.9944227116344, 391.99543598174927, 415.3046975799451, 440.0, 466.1637615180899, 493.8833012561241, 523.2511306011972, 554.3652619537442, 587.3295358348151, 622.2539674441618, 659.2551138257398, 698.4564628660078, 739.9888454232688, 783.9908719634985, 830.6093951598903, 880.0, 932.3275230361799, 987.766602512248, 1046.5022612023945, 1108.7305239074883, 1174.65907166963, 1244.5079348883237, 1318.5102276514797, 1396.9129257320155, 1479.9776908465376, 1567.981743926997, 1661.2187903197805, 1760.0, 1864.6550460723593, 1975.533205024496, 2093.004522404789, 2217.4610478149766, 2349.31814333926, 2489.0158697766474, 2637.020455302959, 2793.825851464031, 2959.955381693075, 3135.9634878539937, 3322.437580639561, 3520.0, 3729.3100921447185]

	for x in range(1,4001):
		if freMin[x] > 20000:
			goodFreMin.append((x,freMin[x]))
		if freMax[x] > 20000:
			goodFreMax.append((x,freMax[x]))

	goodMin = []
	goodMax = []

	for x in range(0,len(frequencies)):
		pos = [i for i, v in enumerate(goodFreMin) if v[0]-0.5 <= frequencies[x] and v[0]+0.5 >= frequencies[x]]
		if pos:
			goodMin.append(x+1)
			
	for x in range(0,len(frequencies)):
		pos = [i for i, v in enumerate(goodFreMax) if v[0]-0.5 <= frequencies[x] and v[0]+0.5 >= frequencies[x]]
		if pos:
			goodMax.append(x+1)
				
	print goodMin
	print goodMax
	recording = False
	

	


