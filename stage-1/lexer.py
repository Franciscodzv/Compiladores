import os
from enum import Enum

class Tag(Enum):
	EOF = 65535
	ERROR = 65534
	## Operators ##
	GEQ = 258
	LEQ = 259
	NEQ = 260
	ASSIGN = 261
	AND = 262
	OR = 263
	MOD = 264
	## REGULAR EXPRESSIONS ##
	ID = 357
	NUMBER = 358
	STRING = 359
	TRUE = 360
	FALSE = 361
	## RESERVED WORDS ##
	VAR = 457
	FORWARD = 548
	TO = 549
	END = 550
	IF = 551
	REPEAT = 552
	ENDREPEAT = 553
	MAKE = 554
	PRINT = 555
	ERASE = 556
	SHOW = 557
	BACKWARD = 558
	RIGHT = 559
	LEFT = 560
	PENUP = 561
	PENDOWN = 562
	SETX = 563
	SETY = 564
	SETXY = 565
	CLEAR = 566
	CIRCLE = 567
	ARC = 568
	PENWIDTH = 569
	COLOR = 570



	
class Token:
	__tag = Tag.EOF
	
	def __init__(self, value):
		self.__tag = value
		
	def getTag(self):
		return self.__tag
		
	def __str__(self):
		if self.__tag == Tag.GEQ:
			return "Token - value >="
		elif self.__tag == Tag.LEQ:
			return "Token - value <="
		elif self.__tag == Tag.NEQ:
			return "Token - value <>"
		elif self.__tag == Tag.ASSIGN:
			return "Token - value :="
		elif self.__tag == Tag.TRUE:
			return "Token - value TRUE"
		elif self.__tag == Tag.FALSE:
			return "Token - value FALSE"
		elif self.__tag == Tag.VAR:
			return "Token - value VAR"
		elif self.__tag == Tag.AND:
			return "Token - value AND"
		elif self.__tag == Tag.OR:
			return "Token - value OR"
		elif self.__tag == Tag.MOD:
			return "Token - value MOD"
		else:
			return "TOKEN - value " + chr(self.__tag)
			
class Number(Token):
	__value = 0.0
	
	def __init__(self, val):
		super().__init__(Tag.NUMBER)
		self.__value = val

	def getTag(self):
		return super().getTag()
	
	def getValue(self):
		return self.__value
	
	def __str__(self):
		return "Number - value: " + str(self.__value)
	
class Word(Token):
	__lexeme = ""
	
	def __init__(self, tag, lex):
		super().__init__(tag)
		self.__lexeme = lex

	def getTag(self):
		return super().getTag()
	
	def getLexeme(self):
		return self.__lexeme
	
	def __str__(self):
		if (self.getTag() == Tag.ID):
			return "Word - lexeme: " + str(self.__lexeme)
		else:
			return "Reserved Word - lexeme: " + str(self.__lexeme)
		





class String(Token):
	__string = ""
	
	def __init__(self, s):
		super().__init__(Tag.STRING)
		self.__string = s

	def getTag(self):
		return super().getTag()
	
	def getString(self):
		return self.__string
	
	def __str__(self):
		return "String - text: " + str(self.__string)

class Lexer:
	__peek = ' '
	__words = {}
	__input = None

	def __init__(self, filepath):
		#assert(not(os.path.isfile(filepath)), "File Not Found")
		
		self.__input = open(filepath, "r")
		self.__peek = ' '

		self.__words["VAR"] = Word(Tag.VAR, "VAR")
		self.__words["FORWARD"] = Word(Tag.FORWARD, "FORWARD")
		self.__words["FD"] = Word(Tag.FORWARD, "FORWARD")
		self.__words["BACKWARD"] = Word(Tag.BACKWARD, "BACKWARD")
		self.__words["BK"] = Word(Tag.BACKWARD, "BACKWARD")
		self.__words["LEFT"] = Word(Tag.LEFT, "LEFT")
		self.__words["LT"] = Word(Tag.LEFT, "LEFT")
		self.__words["RIGHT"] = Word(Tag.RIGHT, "RIGHT")
		self.__words["RT"] = Word(Tag.RIGHT, "RIGHT")
		self.__words["PENUP"] = Word(Tag.PENUP, "PENUP")
		self.__words["PU"] = Word(Tag.PENUP, "PENUP")
		self.__words["PENDOWN"] = Word(Tag.PENDOWN, "PENDOWN")
		self.__words["PD"] = Word(Tag.PENDOWN, "PENDOWN")
		self.__words["REPEAT"] = Word(Tag.REPEAT, "REPEAT")
		self.__words["REPCOUNT"] = Word(Tag.REPEAT, "REPEAT")
		self.__words[":"] = Word(Tag.REPEAT, "MAKE")
		self.__words["CLEAR"] = Word(Tag.CLEAR, "CLEAR")
		self.__words["CLS"] = Word(Tag.CLEAR, "CLEAR")
		self.__words["PRINT"] = Word(Tag.PRINT, "PRINT")
		self.__words["ENDREPEAT"] = Word(Tag.ENDREPEAT, "ENDREPEAT")
		self.__words["SETX"] = Word(Tag.SETX, "SETX")
		self.__words["SETY"] = Word(Tag.SETY, "SETY")
		self.__words["SETXY"] = Word(Tag.SETXY, "SETXY")
		self.__words["CIRCLE"] = Word(Tag.CIRCLE, "CIRCLE")
		self.__words["ARC"] = Word(Tag.ARC, "ARC")
		self.__words["PENWIDTH"] = Word(Tag.PENWIDTH, "PENWIDTH")
		self.__words["ERASE"] = Word(Tag.ERASE, "ERASE")
		self.__words["CLEAR"] = Word(Tag.CLEAR, "CLEAR")
		self.__words["TO"] = Word(Tag.TO, "TO")
		self.__words["END"] = Word(Tag.END, "END")
		self.__words["IF"] = Word(Tag.IF, "IF")
		self.__words["PRINT"] = Word(Tag.PRINT, "PRINT")
		



	



		## ADD ALL RESERVED WORDS ##

	def read(self):
		self.__peek = self.__input.read(1)
	
	def readch(self, c):
		self.read()
		if self.__peek != c:
			return False

		self.__peek = ' '
		return True

	def __skipSpaces(self):
		while True:
			if self.__peek == ' ' or self.__peek == '\t' or self.__peek == '\r' or self.__peek == '\n':
				self.read()
			else:
				break
	
	def scan(self):
		self.__skipSpaces()
		
		## ADD CODE TO SKIP COMMENTS HERE ##
		if(self.__peek == '%'):
			while self.__peek != '\n':
				self.read()
			self.__skipSpaces()


		if self.__peek == '%':
			while True:
				self.read()
				if self.__peek == '\n' or self.__peek == '\r':
					self.__skipSpaces()
					break


		if self.__peek == '<':
			if self.readch('='):
				return Word(Tag.LEQ, "<=")
			elif self.readch('>'):
				return Word(Tag.NEQ, "<>")
			else:
				return Token(ord('<'))
		elif self.__peek == '>':
			if self.readch('='):
				return Word(Tag.GEQ, ">=")
			else:
				return Token(ord('>'))
		elif self.__peek == '#':
			if self.readch('t'):
				return Word(Tag.TRUE, "#t")
			elif self.readch('f'):
				return Word(Tag.FALSE, "#f")
			else:
				return Token(ord('#'))
		elif self.__peek == ':':
			if self.readch('='):
				#print("reading :=")
				return Word(Tag.ASSIGN, ":=")
			else:
				return Token(ord(':'))

		if self.__peek  == '"':
			val = "\""
			while True:
				val = val + self.__peek
				self.read()
				if self.__peek == '"':
					break
			
			val = val + self.__peek
			self.read()
			return String(val)

		if self.__peek.isdigit():
			val = 0
			while True:
				val = (val * 10) + int(self.__peek)
				self.read()
				if not(self.__peek.isdigit()):
					break
			## ADD CODE TO PROCESS DECIMAL PART HERE ##
			if self.__peek == '.':
				val = str(val) + '.'
				self.read()
				while True:
					val = val + self.__peek
					self.read()
					if not(self.__peek.isdigit()):
						break
				return Number(float(val))
				

			return Number(val)

		if self.__peek.isalpha():
			val = ""
			while True:
				val = val + self.__peek.upper()
				self.read()
				if not(self.__peek.isalnum()):
					break

			if val in self.__words:
				return self.__words[val]

			w = Word(Tag.ID, val)
			self.__words[val] = Word(Tag.ID, val)
			return w

		if not(self.__peek):
			return Token(Tag.EOF)			

		token = Token(ord(self.__peek))
		self.__peek = ' ' 
		return token
