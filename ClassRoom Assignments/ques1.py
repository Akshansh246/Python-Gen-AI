import math

# given
ang = 60
rad = 42

# converting deg to rad
angRad = math.radians(ang)

#finding length of arc
arclength = angRad * rad

# now finding side of sq
side = arclength/4

area = side ** 2;
print(area)