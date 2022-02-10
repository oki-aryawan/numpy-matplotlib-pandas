'''

Play coin game

'''

import numpy as np
coin = []
choose_back = str(input('Who choose back?: '))
choose_head = str(input('Who choose head?: '))
rept = int(input('How many repetition?: '))
for x in range(rept):
    result = []
    throw_coin = np.random.randint(0, 2)
    if throw_coin == 0:
        result = 'Head'
    else:
        result = 'Back'
    coin.append(result)
back = coin.count('Back')
head = coin.count('Head')
back_win_rate = round((back / rept * 100), 2)
head_win_rate = round((head / rept * 100), 2)

print(coin)
if back_win_rate > 50:
    print(f'{choose_back} win, Back: {back}, win rate: {back_win_rate}%')
elif back_win_rate == 50:
    print(f'Draw, Back: {back_win_rate}%, Head {head_win_rate}%')
else:
    print(f'{choose_head} win, Head: {head}, , win rate: {head_win_rate}%')
