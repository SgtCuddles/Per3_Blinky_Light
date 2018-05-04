from gpiozero import LED
from time import sleep
led = LED(2)

#while True:
#	led.on()
#	sleep(1)
#	led.off()
#	sleep(1)
	
def choose_Blink(on_time, off_time):
	while True:
		led.on()
		sleep(on_time)
		led.off()
		sleep(off_time)

		
duration1 = float(input("How many seconds should the LED stay on?\n"))
duration2 = float(input("How many seconds should the LED stay off?\n"))
choose_Blink():