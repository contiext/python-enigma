from impl import enigma
from parts import alphabet

'''
MACHINE SETTINGS ->

settings should be lowercase
settings list follows:
[
    plugboard	settings,
	rotor1		setting, initial position, values, notch,	(fastest)
	rotor2		setting, initial position, values, notch,
	rotor3		setting, initial position, values, notch,	(slowest)
	reflector 	values
]

rer determines if settings should reset for each new input
'''
settings = {
	'plugboard':	['ab cd ef gh'],
	'rotor1':		['a', 'a', 'ekmflgdqvzntowyhxuspaibrcj', 'q'],
	'rotor2':		['a', 'e', 'ajdksiruxblhwtmcqgznpyfvoe', 'e'],
	'rotor3':		['a', 'z', 'bdfhjlcprtxvznyeiwgakmusqo', 'v'],
	'reflector':	['ejmzalyxvbwfcrquontspikhgd',],
}
rer = True

#io handling
machine=enigma(settings)
while True:
	i, o=input('> '), ''
	for j in i:
		if j in alphabet:
			o+=machine.run(j)
			machine.rotate()
		else:
			o+=j
	print(o)
	if rer:
		machine=enigma(settings)