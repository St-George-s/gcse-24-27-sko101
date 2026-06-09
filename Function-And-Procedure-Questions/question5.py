import math

def volumeOfSphere(radius):
    volume = 4/3 * math.pi * (radius ** 3)
    return volume

volume = volumeOfSphere(5)
print(volume)