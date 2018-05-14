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
	btl: ltl,
	btr: ltr,
	bbl: lbl,
	bbr: lbr
}


def tester():
	#while True:
	#	for button, light in button_nums.items():
	#		if button.is_pressed:
	#			light.on()
	#			sleep(1)
	#			light.off()
	for i in range(0,10):
		display_num(i)
		sleep(1)

#def startup():

def display_num(num):
	seg_a.off()
	seg_b.off()
	seg_c.off()
	seg_d.off()
	seg_e.off()
	seg_f.off()
	seg_g.off()
	if num >= 1 and num <= 9:
		if num == 1:
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
			
tester()