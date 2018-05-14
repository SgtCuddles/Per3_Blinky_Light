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

led_top_l = LED(23)
led_top_r = LED(24)
led_bottom_l = LED(4)
led_bottom_r = LED(25)

button_top_l = Button(21)
button_top_r = Button(20)
button_bottom_l = Button(16)
button_bottom_r = Button(12)

button_top_l.wait_for_press()
led_top_l.on()
sleep(1)
led_top_l.off()
button_top_r.wait_for_press()
led_top_r.on()
sleep(1)
led_top_r.off()

button_bottom_l.wait_for_press()
led_bottom_l.on()
sleep(1)
led_bottom_l.off()
button_bottom_r.wait_for_press()
led_bottom_r.on()
sleep(1)
led_bottom_r.off()

button_top_l.wait_for_press()
buzzer.on()
sleep(1)
buzzer.off()

button_top_r.wait_for_press()
seg_a.on()
sleep(0.5)
seg_b.on()
sleep(0.5)
seg_c.on()
sleep(0.5)
seg_d.on()
sleep(0.5)
seg_e.on()
sleep(0.5)
seg_f.on()
sleep(0.5)
seg_g.on()
sleep(2)