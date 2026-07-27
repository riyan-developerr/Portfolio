import time
import datetime
import pygame

def alarm_clock(timer):
    file_path = "song.mp3"
    print(f"Your Alarm time is set to {timer}")
    is_running = True
    
    while is_running:
        current_time =datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if timer == current_time:
            print(f"WAKE UP 😫")
            is_running = False
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)
                
        time.sleep(1)


if __name__ == "__main__":
    timer = input("Enter an alarm time (HH:MM:SS): ")
    alarm_clock(timer)