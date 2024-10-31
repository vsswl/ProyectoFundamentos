from machine import Pin
import time

# Definimos los pines para los LEDs
leds = [Pin(i, Pin.OUT) for i in range(15, 21)]
contacto1 = Pin(10, Pin.IN, Pin.PULL_DOWN)
contacto2 = Pin(11, Pin.IN, Pin.PULL_DOWN)
contacto3 = Pin(21, Pin.IN, Pin.PULL_DOWN)
contacto4 = Pin(13, Pin.IN, Pin.PULL_DOWN)
contacto5 = Pin(12, Pin.IN, Pin.PULL_DOWN)

Button = Pin(14, Pin.IN, Pin.PULL_DOWN)

pts = 0
vidas = 3

def parpadeo_leds(led_indices, tiempo_parpadeo):
    start_time = time.time()
    while (time.time() - start_time) < tiempo_parpadeo:
        for i in led_indices:
            leds[i].on()
        time.sleep(0.1)
        for i in led_indices:
            leds[i].off()
        time.sleep(0.1)

def resta_vidas():
    global vidas
    if Button.value() == 1:
        vidas -= 1
        time.sleep(0.2)
        print("Lanzamientos restantes:", vidas)

parpadeo_realizado1 = False
parpadeo_realizado2 = False
parpadeo_realizado3 = False
parpadeo_realizado4 = False
parpadeo_realizado5 = False

while True:
    
    if contacto1.value() == 1 and not parpadeo_realizado1:
        parpadeo_leds([0], 3)  # Parpadea LED 1
        parpadeo_realizado1 = True
        pts += 100
        print("Puntos obtenidos:", pts)
    elif contacto1.value() == 0:
        parpadeo_realizado1 = False
        for i in range(3):
            leds[i].off()

    if contacto2.value() == 1 and not parpadeo_realizado2:
        parpadeo_leds([1], 3)  # Parpadea LED 2
        parpadeo_realizado2 = True
        pts += 200
        print("Puntos obtenidos:", pts)
    elif contacto2.value() == 0:
        parpadeo_realizado2 = False
        for i in range(3, 6):
            leds[i].off()
            
    if contacto3.value() == 1 and not parpadeo_realizado3:
        parpadeo_leds([2], 3)  # Parpadea LED 3
        parpadeo_realizado3 = True
        pts += 300
        print("Puntos obtenidos:", pts)
    elif contacto3.value() == 0:
        parpadeo_realizado3 = False
        for i in range(4, 6):
            leds[i].off()
            
    if contacto4.value() == 1 and not parpadeo_realizado4:
        parpadeo_leds([3], 3)  # Parpadea LED 4
        parpadeo_realizado4 = True
        pts += 400
        print("Puntos obtenidos:", pts)
    elif contacto4.value() == 0:
        parpadeo_realizado4 = False
        for i in range(4, 6):
            leds[i].off()
            
    if contacto5.value() == 1 and not parpadeo_realizado5:
        parpadeo_leds([4, 5], 3)  # Parpadea LEDs 5 y 6
        parpadeo_realizado5 = True
        pts += 600
        print("Puntos obtenidos:", pts)
    elif contacto5.value() == 0:
        parpadeo_realizado5 = False
        for i in range(4, 6):
            leds[i].off()

    resta_vidas()

    time.sleep(0.1)