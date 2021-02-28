from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Si la imagen sale al revés descomentar la siguiente linea y cambiar el ángulo de rotación
#camera.rotation = 180

# Para cambiar la resolución de la imagen descomentar esta linea (resolución máxima: 2592x1944, mínima:64x64)
#camera.resolution = (2592, 1944)

# se debe establecer framerate a 15 para utilizar la resolución máxima
#camera.framerate = 15

camera.start_preview()
sleep(5) # este sleep es necesario porque esto le da tiempo al sensor de la cámara para detectar los niveles de luz.
camera.capture('/home/pi/Desktop/test_imagen.jpg')
camera.stop_preview()
