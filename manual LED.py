from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = button(2)

button.wait_for_press()
led.on()
sleep(3)
led.off()