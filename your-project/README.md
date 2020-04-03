<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Title of Your Project
*[Javier Hita]*

*[Data Analytics, Barcelona & April]*

## Content

- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description

The project consists on building a 21 Blackjack game. I choose this game because I have always been interested on it and it's always nice to be on the dealers side.

## Rules

In this 21 Blackjack the rules a quite simple:
Each participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21
In case of a draw betwwen a player and the dealer, the dealer always wins
It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its pip value
Each player will be given 2 cards at the begining of the hand
The player to the left goes first and must decide whether to "stand" (not ask for another card) or "hit" (ask for another card in an attempt to get closer to a count of 21. Thus, a player may stand on the two cards originally dealt to them, or they may ask the dealer for additional cards, one at a time, until deciding to stand on the total (if it is 21 or under), or goes "bust


## Workflow

The steps of the workflow are quite straight forward because in Blackjack the workflow if always the same.
I tried to make as many functions as I could in order to make it as structured as possible.
First of all, I created a dictionary with all the players names (input) as keys and their values was a list composed by their cards and their current score, which starts as 0. Secondly, I create a deck where all cards can be found as weel as their value. We can no begin the game! Once the game starts, each players receives 2 cards and it's current score is printed. Secondly, each player is asked if the want to hit or stand. Keep looping until the player stands, goes bust or scores 21.
Once each players turn has finished, it's time to compare the players score with the dealers score, and show each player their result.
Ask the players want to keep playing and reset the players dictionary.


## Organization

I developed my project in 4 steps:
First I created a text file, where I wrote how I was going to structure the whole program (functions to create, workflow, variables, etc) but without coding. Secondly, I created a trello board with all the tasks that I had to carry out and it's status. Thirdly, I wrote in another text file with pseudocode in order to have crystal clear how it was going to look like. Finally, I created my jupyter file and starting coding.

My jupyter file is divided in 2 sections. The first one is where I defined all the functions I was going to use for the program. The second one is the program, which is composed by a workflow (while and for loops, basically) of all the functions.

## Links

[Repository](https://https://github.com/Javierhvb/Project-Week-1-Build-Your-Own-Game)
[Slides](https://drive.google.com/file/d/1iTdE_kqWFu6Wy00sk0jf1AHbzfel-KSK/view?usp=sharing)
[Trello](https://trello.com/b/iAXEngpb/blackjack-project)  
