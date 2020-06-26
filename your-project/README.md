<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Title of Your Project
*Javier Pradera*

*Data Analytics Bootcamp - Ironhack Barcelona - June 2020*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
This project consists of a simplified simulation of the game Blackjack. It consists of a 1 vs. 1 version in which the player (user) plays against the dealer (CPU).
## Rules
The blackjack rules included in this simulation are the following:
- **Card values**: It is up to the player if an ace is worth 1 or 11. Face cards are 10 and any other card is its number value.
- **Betting**: The player chooses an initial amount of money with which he wants to play. In each round, he/she must decide how much he/she wants to bet. The game ends when the player runs out of money or  when he/she decides to bet 0 in a specific round.
- **The deal**: When a round starts, the dealer gives two faced up cards to the player and two cards to the dealer: one faced up and the other one faced down.
- **Blackjack**: If the player has a blackjack, the dealer’s faced down card is faced up. If the dealer has a blackjack, it is a tie. If not, the player wins and collects double of its bet.
- **Player’s play**: if the player does not have a blackjack, he/she can decide if the wants another card (“Hit”) or no more cards (“Stand”) as long as its total score is under or equal to 21. If he/she goes “bust” (over 21) he/she loses automatically.  If the player stands under 21, it is the dealer’s turn.
- **Dealer’s play**: the dealer’s play is automatic. The dealer must “Hit” if its score is under or equal to 16 and must “Stand” if its score is equal or greater than 17.
- **Doubling down**: if the player's two first cards add up 9, 10 or 11, he/she is given the opportunity to double its current bet
## Workflow
In order to develop the game, I went through the following stages:
- **Main inputs**: I started introducing the game's main inputs: the deck of cards and their values and the player's initial amount of money.
- **Main function**: Once I had the game's main inputs, I started coding the main function of the game, with its inputs and auxiliary functions (e.g. the player's bet for each round).
- **Error testing and solving**: I then tested the game several times and solved the errors that appeared before moving on to the addition of new features.
- **Additional features**: Once I had a basic version that worked properly, I added new rules, such as the possibility of counting the As as a 1 or the possibility to double the player's bet.
- **Preparation of presentation**: I finally prepared the presentation

## Organization
I organized my work using Trello, with a dashboard made up of the following stages:
- **Research on game rules**
- **Coding of the basic version**
- **Basic version testing**
- **Error solving**
- **Addition of new features**

The repository is composed of the following files and folders:
- **README.md**: detailed explanation of the project.
- **Blackjack.ipynb**: Jupyter notebook file in which the user can play Blackjack.
- **Code**: folder with the code of the game inside:
    - **Blackjack.py**: python file with the code of the game that is imported as a module in "Blackjack.ipynb"


## Links
Include links to your repository, slides and kanban board. Feel free to include any other links associated with your project.

[Repository](https://github.com/javier-pradera/Project-Week-1-Build-Your-Own-Game)  
[Slides](https://slides.com/jpradera/deck/live)  
[Trello](https://trello.com/b/XL6EguFr/ironhack-project-1-blackjack)  
