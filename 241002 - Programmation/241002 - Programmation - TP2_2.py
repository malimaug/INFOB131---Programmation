angle1 = 90
angle2 = 45
angle3 = 45

if angle1 + angle2 + angle3 != 180:
    print("Ce n'est pas possible de former un triangle a l'aide de ces angles")

if angle1 == 60 and angle2 == 60:
    print("c'est un triangle équilatéral")

elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:

    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("c'est un triangle rectangle isocèle")
    else:
        print("c'est un triangle isocèle")

elif angle1 == 90 or angle2 == 90 or angle3 == 90:
    print("c'est un triangle rectangle")
else:
    print("c'est un triangle scalène")