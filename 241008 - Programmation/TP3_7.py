nb_frames = 23
nb_beehives = 60
nb_sheetswax = 24

beehive_cost = 150 + 1.5 * nb_frames + 0.5 * nb_sheetswax

if nb_frames > 6 and nb_sheetswax == nb_frames:
    beehive_cost -=0.5 * (nb_frames - 6)

if nb_beehives > 10:
    beehive_cost -= beehive_cost * 0.1

total_cost = beehive_cost * nb_beehives