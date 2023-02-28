import numpy as np

def square_err(x, y):
    SE_line = sum((y-x)**2)
    SE_mean = sum((y-y.mean())**2)
    r2 = 1-(SE_line/SE_mean)
    return r2


# Obtained values from the correlation matrix
# each position represent: ripe, green, half-ripe and bakground
# On y_i values, the expected values.
# On x_i values, the actual obtained results.

y1 = np.array([100, 0, 0, 0])
x1 = np.array([78, 0, 12, 10])

y2 = np.array([0, 100, 0, 0])
x2 = np.array([0, 90, 1, 9])

y3 = np.array([0, 0, 100, 0])
x3 = np.array([9, 6, 82, 3])

print('ripe: {}'.format(square_err(x1, y1)))
print('green: {}'.format(square_err(x2, y2)))
print('half: {}'.format(square_err(x3, y3)))