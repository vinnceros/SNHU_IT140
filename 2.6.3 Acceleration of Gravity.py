G = 6.673e-11
M = 5.98e24
accel_gravity = 0.0

dist_center = float(input())

accel_gravity = (G * M) / (dist_center**2)

print('Acceleration of gravity: {:.2f}'.format(accel_gravity))