# Space Catch!
This is a game where the players try to catch more stars than asteroids. The one to get 10 or more first wins! Why would a ship catch stars? How massive are these ships?? Never mind all that and beat your opponent in some old-school competitive action.
# Game Controls
Player 1 uses WASD keys to move, player 2 uses IJKL. You both use the same keyboard-- keep in mind that pinching your opponent in real life or pushing their hand away is considered bad manners in most cultures. The little "v" next to the ship (AKA "The Claw") is the only part of your ship that can catch stars or asteroids so be careful!

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.

```
python3 cycle 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- space_catch               (source code for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (general values that are referenced through the classes)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Kelley Robertson (Managed to properly set up the game over screen)
* Shanny López (Creator of repository, set up the "skeleton" of the project)
* Cristian Avendaño (Set up the ships, cleaned up code at different parts)