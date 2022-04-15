from itertools import count
import numpy as np

number = np.random.randint(1, 101)
count = 0
while True:
    predict_number = int(input('Predict number by 1 to 100: '))
    count += 1
    if predict_number > number:
        print('the number must be less than')
    elif predict_number < number:
        print('the number must be greater then')
    else:
        print(f'You predict the number. That namber {number} for {count} attempts')
        break