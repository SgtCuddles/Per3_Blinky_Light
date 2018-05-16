from gpiozero import LED
from gpiozero import Buzzer
from gpiozero import Button
from time import sleep

buzz_buzz = Buzzer(18)

seg_a = LED(27)
seg_b = LED(22)
seg_c = LED(5)
seg_d = LED(6)
seg_e = LED(13)
seg_f = LED(19)
seg_g = LED(26)

ltl = LED(23)
ltr = LED(24)
lbl = LED(4)
lbr = LED(25)

btl = Button(21)
btr = Button(20)
bbl = Button(16)
bbr = Button(12)

button_nums = {
	btl: 0,
	btr: 1,
	bbl: 2,
	bbr: 3
}

notes = {
        'C': 261.6,
        'Cs': 277.2,
        'D': 293.7,
        'Eb': 311.1,
        'F': 329.6,
        'Fs': 370.0,
        'G': 392.0,
        'Gs': 415.3,
        'A': 440.0,
        'Bb': 466.2,
        'B': 493.9
}

def tester():
	for i in range(0,10):
		display_num(i)
		sleep(1)

def startup():
	cont = True
	difficulty = 4
	display_num(difficulty)
	while cont:
		for button, num in button_nums.items():
			if button.is_pressed:
				if num == 0:
					if difficulty > 0:
						difficulty -= 1
					display_num(difficulty)
					sleep(0.3)
				elif num == 1:
					if difficulty < 9:
						difficulty += 1
					display_num(difficulty)
					sleep(0.3)
				elif num == 3:
					cont = False

	

def display_num(num):
	seg_a.off()
	seg_b.off()
	seg_c.off()
	seg_d.off()
	seg_e.off()
	seg_f.off()
	seg_g.off()
	if num >= 0 and num <= 9:
		if num == 0:
			seg_a.on()
			seg_b.on()
			seg_c.on()
			seg_d.on()
			seg_e.on()
			seg_f.on()
		elif num == 1:
			seg_b.on()
			seg_c.on()
		elif num == 2:
			seg_a.on()
			seg_b.on()
			seg_d.on()
			seg_e.on()
			seg_g.on()
		elif num == 3:
			seg_a.on()
			seg_b.on()
			seg_c.on()
			seg_d.on()
			seg_g.on()
		elif num == 4:
			seg_b.on()
			seg_c.on()
			seg_f.on()
			seg_g.on()
		elif num == 5:
			seg_a.on()
			seg_c.on()
			seg_d.on()
			seg_f.on()
			seg_g.on()
		elif num == 6:
			seg_a.on()
			seg_c.on()
			seg_d.on()
			seg_e.on()
			seg_f.on()
			seg_g.on()
		elif num == 7:
			seg_a.on()
			seg_b.on()
			seg_c.on()
		elif num == 8:
			seg_a.on()
			seg_b.on()
			seg_c.on()
			seg_d.on()
			seg_e.on()
			seg_f.on()
			seg_g.on()
		elif num == 9:
			seg_a.on()
			seg_b.on()
			seg_c.on()
			seg_d.on()
			seg_f.on()
			seg_g.on()

def make_note(note, length):
        frequency = notes[note]
        delay_value = float((1.0/frequency)/2.0)
        num_cycles = int(length * frequency)
        for i in range(num_cycles):
                buzz_buzz.on()
                sleep(delay_value)
                buzz_buzz.off()
                sleep(delay_value)
                
			
startup()
