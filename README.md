<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Mastermind
*[Erik Termes]*

*[Data analytics, Barcelona, 23/10/2020]*

## Content
- [Project Description]
- [Rules]
- [Workflow]
- [Organization]
- [Links]

## Project Description
The game I created is Mastermind. The game is about guessing four random colours based on the feedback you get on each try.
I chose Mastermind because it is a challenging game to program that taught me how to work under different conditions and to loop different items on a list.

## Rules
The machine chooses 4 colors out of 8, at random.
In order to win at Mastermind, you must guess which are the 4 colors the machine chose in each position.
After selecting your colors, which at first will be a random choice out of 8, the computer will tell you how many colors you got correct, how many of your 
colors are in the solution but in a different order, and how many colors you got wrong.
based on that information, you will try to deduce which colors are correct.
The player has up to 10 tries.

## Workflow
At the start of the project, first I researched the Mastermind ruleset and the parameters needed to play a full game.

After learning about the process, I established the random colors for the machine, and then the four inputs the player will select out of the 8 colors.

The first step was to create a loop which would check which of the player choices are in the machine choices, then I tuned it so it would detect if the
color is in the exact position, or if it's wrong, and added a counter to each result so the player would know how many they got correct, wrong or in wrong positions.
After that I solved an issue where the counters would not reset, the player would get the accumulated feedback, which we don't want, instead of the counters of how
many they got correct on that try.

Once that initial loop was established, I could move on to the bigger scope of the entire loop, which would ask the player for inputs, and stop the player at 10 tries (the maximum) or 
when the player wins.

After this process we have a fully functional game, that will need some tuning to the code in order to clean up the printed text, and how each try is shown to the player.

When I was done with the full setup, I decided to add a fully functional storyline to the game. The storyline would give the player context, interact with different voicelines or
sentences when the player performed certain actions, and give context to the entire game to make the player experience more engaging. The storyline process required working me to 
pay attention to detail at when to add each feedback line and customize it for each situation. I also added a few images for better visibility and interaction with the player.

After the final touchups, we can play mastermind!

## Organization
I used trello to organize different tasks. The main tasks I organized though Trello are the bigger objectives of the project, like creating the slides, researching the ruleset of 
the game and testing the game. I also used it to track some code blockers I found along the way.

My repository has a folder with the working code, a folder for the images that complement the project, and 

## Links

[Repository](https://github.com/ErikTermes/Project-Week-1-Build-Your-Own-Game)  
[Slides](https://docs.google.com/presentation/d/1yzIZKWm85i4ZCXG2nRUiO_cu-XVuI-1N9M-2h9ukpdk/edit?usp=sharing)  
[Trello](https://trello.com/b/dbkP6AOd/project-1-mastermind)  
