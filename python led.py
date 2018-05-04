from gpiozero import LED
from time import sleep
led = LED(2)

def choose_Blink(on_time, off_time):
	led.on()
	sleep(on_time)
	led.off()
	sleep(off_time)

		
#.-.. --- .-. . -- / .. .--. ... ..- --

while True:
	choose_Blink(0.25,0.5)#l
	choose_Blink(0.5,0.5)
	choose_Blink(0.25,0.5)
	choose_Blink(0.5,1)
	
	choose_Blink(0.5,0.5)#o
	choose_Blink(0.5,0.5)
	choose_Blink(0.5,1)
	
	choose_Blink(0.25,0.5)#r
	choose_Blink(0.50,0.5)
	choose_Blink(0.25,1)
	
	choose_Blink(0.25,1)#e
	
	choose_Blink(0.5,0.5)#m
	choose_Blink(0.5,2)
	
	
	choose_Blink(0.25,0.5)#i
	choose_Blink(0.25,1)
	
	choose_Blink(0.25,0.5)#p
	choose_Blink(0.5,0.5)
	choose_Blink(0.5,0.5)
	choose_Blink(0.25,0.5)
	
	choose_Blink(0.25,0.5)#s
	choose_Blink(0.25,0.5)
	choose_Blink(0.25,1)
	
	choose_Blink(0.25,0.5)#u
	choose_Blink(0.25,0.5)
	choose_Blink(0.5,1)
	
	choose_Blink(0.5,0.5)#m
	choose_Blink(0.5,1)