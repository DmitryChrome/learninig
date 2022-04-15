"""Guess the number game.
The computer itself makes a guess and guesses the number"""
import numpy as np
def random_predict(number:int=1) -> int:
    """_summary_

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        number attempt
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return count
print(f'Count attempt: {random_predict()}')

def score_game(random_predict) ->int:
    """mean count 1000 attempt

    Args:
        random_predict (_type_): function predict

    Returns:
        int: mean count
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'mean count: {score} attempt')
    return score

if __name__ == '__main__':
score_game(random_predict)