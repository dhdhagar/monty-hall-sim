import sys
import argparse
from montyhall import montyhall

if __name__ == '__main__':
    # print(parser.format_help())
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--iters', help='Number of iterations of the game', type=int, default=10000)
    parser.add_argument(
        '--seed', help='Seed of the random number generator', type=int)
    args = parser.parse_args()

    iters, seed = args.iters, args.seed
    wins = {'stay': 0, 'switch': 0, 'randomize': 0}
    game = montyhall(seed)
    for i in range(iters):
        game.generateGame()
        result = game.playGame()
        wins['stay'] += result['stay']
        wins['switch'] += result['switch']
        wins['randomize'] += result['randomize']

    print(
        f'\nGame Iterations = {iters}\n\nWins per Strategy:\n  Always Switch = {round(wins["switch"]/iters*100, 3)}% ({wins["switch"]})\n  Always Stay = {round(wins["stay"]/iters*100, 3)}% ({wins["stay"]})\n  Randomize = {round(wins["randomize"]/iters*100, 3)}% ({wins["randomize"]})\n')
