#! python

import time 
import playsound
import threading

def display_text_in_center_of_screen(text):
    print("\033[2J\033[1;1H")
    print(text.center(80))

def pretty_display_time(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

def pretty_duration(start):
    end = time.time()
    return pretty_display_time(end - start)

def beep(is_inhale: bool):
    sound_path = f'/System/Library/Sounds/{"Blow" if is_inhale else "Submarine"}.aiff'
    t = threading.Thread(target = lambda: playsound.playsound(sound_path))
    t.start()

def do_inhales(start: float):
    beep(is_inhale = True)
    for _ in range(4):
        display_text_in_center_of_screen(f"Inhale: {pretty_duration(start = start)}")
        time.sleep(1)
    display_text_in_center_of_screen(f"Inhale: {pretty_duration(start = start)}")
    time.sleep(0.8)

def do_exhales(start: float):
    beep(is_inhale=False)
    for _ in range(7):
        display_text_in_center_of_screen(f"Exhale {pretty_duration(start = start)}")
        time.sleep(1)
    display_text_in_center_of_screen(f"Exhale {pretty_duration(start = start)}")
    time.sleep(0.2)

def do_a_breathing_round(start: float):
    do_inhales(start = start)
    do_exhales(start = start)

def main():
    start = time.time()
    while True:
        do_a_breathing_round(start = start)

if __name__ == "__main__":
    main()