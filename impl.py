from parts import plugboard, rotor, reflector
alphabet='abcdefghijklmnopqrstuvwxyz'

class enigma:
	def __init__(self, settings):
		#initialize the components
		self.plugboard=plugboard(*settings['plugboard'])
		self.rotor1=rotor(*settings['rotor1'])
		self.rotor2=rotor(*settings['rotor2'])
		self.rotor3=rotor(*settings['rotor3'])
		self.reflector=reflector(*settings['reflector'])
	def run(self, char):
		#initialization
		u=char==char.upper()
		char=char.lower()

		#running char through machine
		char=self.plugboard.run(char)
		char=self.rotor1.runfw(char)
		char=self.rotor2.runfw(char)
		char=self.rotor3.runfw(char)
		char=self.reflector.run(char)
		char=self.rotor3.runbw(char)
		char=self.rotor2.runbw(char)
		char=self.rotor1.runbw(char)
		char=self.plugboard.run(char)

		#return
		if u:
			return char.upper()
		return char
	def rotate(self):
		self.rotor1.rotate()
		if self.rotor2.pos == self.rotor2.notch:
			#double step
			self.rotor2.rotate()
			self.rotor3.rotate()
		else:
			#normal step
			if self.rotor1.pos==self.rotor1.notch:
				self.rotor2.rotate()