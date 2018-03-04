# calculadora_humana

This program implements a mathematical game that ask you simple arithmetical calculations:
sum, difference, multiplication and divison, where each result is the first number for the next calculation,
in a way similar that does the spanish television program "Saber y Ganar", **La Calculadora Humana**.

# How to play

The game mechanics its very simple:
Run in a terminal:
```
python calculadora_humana.py 10
```
and the game will start asking you questions until 10.
To give a response, simply type the integer number you want and press enter.
If you fail the response, you'll have infinite hints.

When you finish the test, the program will show to you a report of the time needed to answer and the number of fails.

The calculations are completely random

# Difficulty levels
By the moment, the game has just one dificulty level.

You will find only positive integers, not greater than 200.

The results will be always in this range and you won't be asked to divide
a number by other if the result is not an integer.

## To be implemented

In the future I want to implement new dificulty levels, for example:
- Very fast game: small integer values to practice real metal and visual agility
- With negatives: incluiding values under 0
- Big numbers:
- Powers, square roots...
