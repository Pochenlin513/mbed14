import pyb
import sensor, image, time, os, tf

uart = pyb.UART(3,9600,timeout_char=1000)
uart.init(9600,bits=8,parity = None, stop=1, timeout_char=1000)
tmp = ""

def image_classification():
   sensor.reset()                         # Reset and initialize the sensor.
   sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
   sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (?x?)
   sensor.set_windowing((240, 240))       # Set 240x240 window.
   sensor.skip_frames(time=2000)          # Let the camera adjust.
   out = ""
   img = sensor.snapshot()
   img.lens_corr(1.8) # strength of 1.8 is good for the 2.8mm lens.
   for code in img.find_qrcodes():
      img.draw_rectangle(code.rect(), color = (255, 0, 0))
      out += code.payload()

   print(out)
   uart.write(out.encode())




while(1):
   a = uart.readline()
   if a is not None:
      tmp += a.decode()


   if tmp == "image_classification":
      print("Read QR Code")
      tmp =""
      image_classification()


