import argparse
import sys
import traceback
import time

from RPi import GPIO

def blink(pin, sleep_seconds=1.0):
    """ Blink a pin for sleep_seconds.

    @param pin Target pin
    @param sleep_seconds Number of seconds to sleep (floating)"""
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(sleep_seconds)
    GPIO.output(pin, GPIO.LOW)

def setup_and_parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--times", "-t", default=0, type=int,
        help="Times to blink through the LED colors (default: 0, infinite)")
    parser.add_argument("--on-for", default=1, type=float,
        help="Number of seconds (floats accepted) each color stays on for")
    parser.add_argument("--red-pin", "-r", default=17, type=int,
        help="The red pin number (default: 17)")
    parser.add_argument("--green-pin", "-g", default=27, type=int,
        help="The green pin number (default: 27)")
    parser.add_argument("--blue-pin", "-b", default=22, type=int,
        help="The blue pin number (default: 22)")
    return parser.parse_args()

def main():
    args = setup_and_parse_arguments()

    # Create a list of our target GPIO pins.
    rgb = [args.red_pin, args.green_pin, args.blue_pin]

    # Setup RPi.GPIO for BCM numbering.
    GPIO.setmode(GPIO.BCM)

    # Setup our rgb pins for output mode.
    GPIO.setwarnings(False)
    GPIO.setup(rgb, GPIO.OUT)
    GPIO.setwarnings(True)

    # Write a LOW value to all of our rgb pins.
    GPIO.output(rgb, GPIO.LOW)

    if not args.times:
        # If args.times is 0, we blink the colors indefinitely.
        while True:
            for pin in rgb:
                blink(pin, args.on_for)
    else:
        # Otherwise, we just do a blink rotation args.times number of times.
        for i in range(args.times):
            for pin in rgb:
                blink(pin, args.on_for)

    return 0

if __name__ == "__main__":
    e = 1

    try:
        e = main()
    except Exception as exc:
        traceback.print_exc()

    sys.exit(e)
