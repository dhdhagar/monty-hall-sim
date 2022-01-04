# The Monty Hall Problem Simulator

A simulation to showcase the results of applying various strategies to the Monty Hall problem and to empirically establish the dominance of the Always-Switch strategy.

## Usage
```
usage: play.py [-h] [--iters ITERS] [--seed SEED]

optional arguments:
  -h, --help     show this help message and exit
  --iters ITERS  Number of iterations of the game
  --seed SEED    Seed of the random number generator
```

## Background
*(From [Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem))* The Monty Hall problem is a brain teaser, in the form of a probability puzzle, loosely based on the American television game show Let's Make a Deal and named after its original host, Monty Hall. The problem was originally posed (and solved) in a letter by Steve Selvin to the American Statistician in 1975. It became famous as a question from a reader's letter quoted in Marilyn vos Savant's "Ask Marilyn" column in Parade magazine in 1990:  
&nbsp;  
*Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?*

## What's happening?
Bayes' theorem! The following post provides a great explanation of the mathematical validity of this seemingly counter-intuitive result: https://mixtape.scunning.com/probability-and-regression.html#monty-hall-example. (Thanks to [Dr. Garima Agarwal](https://sites.google.com/view/garima-agarwal) for sharing!)
