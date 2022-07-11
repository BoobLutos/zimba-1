import keyboard
#keyboard.write('This is a bad attempt')
recorded = keyboard.record(until='esc')
played = keyboard.play(recorded, speed_factor=3)
#print(played)
