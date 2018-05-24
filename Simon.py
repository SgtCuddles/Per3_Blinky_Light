from gpiozero import LED
from gpiozero import Buzzer
from gpiozero import Button
from time import sleep
from random import randint

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

button_ids = {
        0: btl,
        1: btr,
        2: bbl,
        3: bbr
}

A = 440
B = 493.883
C = 523.251
D = 587.33
E = 659.255
F = 698.456
G = 783.991

def tester():
	for i in range(0,10):
		display_num(i)
		sleep(1)

def startup():
	cont = True
	difficulty = 3
	display_num(difficulty)
	while cont:
		num = get_button_press()
		if num == 0:
			if difficulty > 1:
				difficulty -= 1
			display_num(difficulty)
			sleep(0.3)
		elif num == 1:
			if difficulty < 9:
				difficulty += 1
			display_num(difficulty)
			button_ids[button].wait_for_release()
		elif num == 3:
			cont = False
		elif num == 2:
                        cont = False
                        difficulty = 0
	display_num()
	game(difficulty * 3)

def game(difficulty):
	instructions = []
	for i in range(difficulty):
		instructions.append(randint(0,3))
	lost = False
	for i in range(difficulty):
		for n in range(i):
			if not lost:
				if instructions[n] == 0:
					ltl.on()
					make_note(A, 0.5)
					ltl.off()
					sleep(0.3)
				elif instructions[n] == 1:
					ltr.on()
					make_note(C, 0.5)
					ltr.off()
					sleep(0.3)
				elif instructions[n] == 2:
					lbl.on()
					make_note(E, 0.5)
					lbl.off()
					sleep(0.3)
				else:
					lbr.on()
					make_note(G, 0.5)
					lbr.off()
					sleep(0.3)

		for n in range(i):
			if not lost:
				button = get_button_press()
				if button != instructions[n]:
                                        lost = True
					break
				elif button == 0:
					ltl.on()
					make_note(A, 0.3)
				elif button == 1:
					ltr.on()
					make_note(C, 0.3)
				elif button == 2:
					lbl.on()
					make_note(E, 0.3)
				else:
					lbr.on()
					make_note(G, 0.3)
				ltl.off()
				ltr.off()
				lbl.off()
				lbr.off()
				button_ids[button].wait_for_release()
		if lost:
                        break
		sleep(0.5)
	end(lost, difficulty)

def end(lost, difficulty):
	if lost:
		print('You Lost')
		display_letter('Y')
		sleep(0.5)
		display_letter('O')
		sleep(0.5)
		display_letter('U')
		sleep(1)
		display_letter('L')
		sleep(0.5)
		display_letter('O')
		sleep(0.5)
		display_letter('S')
		sleep(0.5)
		display_letter('E')
		sleep(0.5)
	elif difficulty != 0:
		print('You Won')
		display_letter('Y')
		sleep(0.5)
		ltl.on()
		display_letter('O')
		sleep(0.5)
		ltr.on()
		ltl.off()
		display_letter('U')
		sleep(1)
		lbl.on()
		ltr.off()
		display_letter('W')
		sleep(0.5)
		lbr.on()
		lbl.off()
		display_letter('I')
		sleep(0.5)
		ltl.on()
		lbr.off()
		display_letter('N')
		sleep(0.5)
		ltl.off()
		display_num()
		
	

def display_num(num=20):
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

def display_letter(letter = 'b'):
	seg_a.off()
	seg_b.off()
	seg_c.off()
	seg_d.off()
	seg_e.off()
	seg_f.off()
	seg_g.off()
	if letter == 'Y':
		seg_b.on()
		seg_c.on()
		seg_d.on()
		seg_f.on()
		seg_g.on()
	elif letter == 'O':
		seg_a.on()
		seg_b.on()
		seg_c.on()
		seg_d.on()
		seg_e.on()
		seg_f.on()
	elif letter == 'U':
		seg_c.on()
		seg_d.on()
		seg_e.on()
	elif letter == 'W':
		seg_b.on()
		seg_d.on()
		seg_f.on()
	elif letter == 'L':
		seg_d.on()
		seg_e.on()
		seg_f.on()
	elif letter == 'S':
		seg_a.on()
		seg_c.on()
		seg_d.on()
		seg_f.on()
		seg_g.on()
	elif letter == 'N':
		seg_c.on()
		seg_e.on()
		seg_g.on()
	elif letter == 'E':
		seg_a.on()
		seg_d.on()
		seg_e.on()
		seg_f.on()
		seg_g.on()
	elif letter == 'I':
		seg_e.on()
		seg_f.on()
	elif letter == 'G':
                seg_a.on()
                seg_b.on()
                seg_c.on()
                seg_d.on()
                seg_f.on()
                seg_g.on()
        elif letter == 'D':
                seg_b.on()
                seg_c.on()
                seg_d.on()
                seg_e.on()
                seg_g.on()
        elif letter == 'B':
                seg_c.on()
                seg_d.on()
                seg_e.on()
                seg_f.on()
                seg_g.on()
        
		

def make_note(note, length):
	frequency = note
	delay_value = float((1.0/frequency)/2.0)
	num_cycles = int(length * frequency)
	for i in range(num_cycles):
		buzz_buzz.on()
		sleep(delay_value)
		buzz_buzz.off()
		sleep(delay_value)
	buzz_buzz.off()

def get_button_press():
	cont = True
	while cont:
		for button, num in button_nums.items():
			if button.is_pressed:
				cont = False
				return num
conti = 2
while conti:
        startup()
        conti = get_button_press()
        if get_button_press != 2:
                conti = False
                display_letter('G')
                sleep(0.3)
                display_letter('O')
                sleep(0.6)
                display_letter('D')
                sleep(0.3)
                display_letter('B')
                sleep(0.3)
                display_letter('Y')
                sleep(0.3)
                display_letter('E')
                sleep(0.3)
        else:
                sleep(0.3)
