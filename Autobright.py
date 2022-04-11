#!/usr/bin/env python
import time
import argparse
# import rpi_backlight as bl
from rpi_backlight import Backlight

#bl = Backlight("/sys/class/backlight/10-0045")
bl=Backlight()

parser = argparse.ArgumentParser(description="Autobright!")
parser.add_argument("-m", default="0630", help="Morning time starts (HHMM) (0700 default)")
parser.add_argument("-n", default="1830", help="Night time starts (HHMM) (2000 default)")
parser.add_argument("-f", default="30", help="Fade time (minutes) (30 default)")
parser.add_argument("-d", default="15", help="Dark level (0-255, 15 default)")
parser.add_argument("-b", default="100", help="Bright level (0-255, 255 default)")

args = parser.parse_args()
morningStarts = int(args.m)
nightStarts = int(args.n)
fadeTime = int(args.f)
darkLevel = int(args.d)
brightLevel = int(args.b)

duskEnds = nightStarts + fadeTime
dawnEnds = morningStarts + fadeTime

bl.fade_duration = 30

while(1):
	# t = time.localtime()
	currentTime = int(time.strftime("%H%M"))
	
	print("Now:", currentTime, "\nMorning:", morningStarts, "\nDawn Ends:", dawnEnds, "\nNight:", nightStarts, "\nDusk ends:", duskEnds, "\nFade:", fadeTime)
	
	if currentTime <= morningStarts or currentTime >= duskEnds:
		print("Night")
		bl.brightness = darkLevel
		# night
	
	elif currentTime <= dawnEnds:
		print("Morning fade")
		brightnessPerMinute = ((brightLevel - darkLevel) / fadeTime )
		currentBrightness = brightnessPerMinute * (dawnEnds - currentTime)
		print("dawn current brightness:", currentBrightness)
		bl.brightness = currentBrightness
		# morning fade
	
	elif currentTime >= nightStarts and currentTime < duskEnds:
		print("Night fade")
		brightnessPerMinute = ((brightLevel - darkLevel) / fadeTime )
		currentBrightness = brightnessPerMinute * (duskEnds - currentTime)
		print("dusk current brightness:", currentBrightness)
		bl.brightness = currentBrightness
		# night fade
	
	elif currentTime >= dawnEnds and currentTime < nightStarts:
		print("Daytime")
		bl.brightness = brightLevel
		# daytime
	time.sleep(30)
