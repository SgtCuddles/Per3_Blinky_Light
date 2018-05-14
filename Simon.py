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

for button, light in button_nums.items():
	button.when_pressed = light.on()
	sleep(1)
	light.off()