from gpiozero import LED
from time import sleep
led = LED(2)

def choose_Blink(on_time, off_time):
	led.on()
	sleep(on_time)
	led.off()
	sleep(off_time)

def Morse():
	continu = True
	while continu:
		for i in range(0, 2):
			choose_Blink(0.25,0.5)
			choose_Blink(0.5,0.5)
			choose_Blink(0.25,0.5)
			choose_Blink(0.5,1)
			
			choose_Blink(0.5,0.5)
			choose_Blink(0.5,0.5)
			choose_Blink(0.5,1)
			
			choose_Blink(0.25,0.5)
			choose_Blink(0.50,0.5)
			choose_Blink(0.25,1)
			
			choose_Blink(0.25,1)
			
			choose_Blink(0.5,0.5)
			choose_Blink(0.5,2)
			
			
			choose_Blink(0.25,0.5)
			choose_Blink(0.25,1)
			
			choose_Blink(0.25,0.5)
			choose_Blink(0.5,0.5)
			choose_Blink(0.5,0.5)
			choose_Blink(0.25,0.5)
			
			choose_Blink(0.25,0.5)
			choose_Blink(0.25,0.5)
			choose_Blink(0.25,1)
			
			choose_Blink(0.25,0.5)
			choose_Blink(0.25,0.5)
			choose_Blink(0.5,1)
			
			choose_Blink(0.5,0.5)
			choose_Blink(0.5,1)
		
		quit = str(input("Do you want to quit? (type yes to quit)"))
		if quit == 'yes':
			continu = False
			
def Main():
	choices = {'morse':Morse, 'Manual':steady,'repeat':Repeat}
	choice = input("Available Behaviors:\n\t-Morse\n\t-Manual\n\t-Repeat").lower
	choices[choice]()