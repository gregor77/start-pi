import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

SW = 7
LED = 11

GPIO.setup(LED, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(SW, GPIO.IN)

try:
  while 1:
    key_in = GPIO.input(SW)
    if key_in == 0:
      print('switch on')
      GPIO.output(LED, GPIO.HIGH)
    else:
      print('switch off')
      GPIO.output(LED, GPIO.LOW)
except KeyboardInterrupt:
  pass

GPIO.cleanup()
