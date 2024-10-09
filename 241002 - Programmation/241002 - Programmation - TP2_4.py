pressure = 2
volume = 7

p_treshold = 2.3
v_treshold = 7.41

if pressure > p_treshold and volume > v_treshold:
    print("Turn off the plant!")
elif pressure > p_treshold and volume < v_treshold:
    print("Augment the volume")
elif pressure < p_treshold and volume > v_treshold:
    print("Deminish the volume")
else:
    print("Everything is going well")