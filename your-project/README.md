<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Mastermind
*[Elliott Coyne]*

*[Data, BCN, October 2019]*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
The aim of this project is to create a game of Mastermind. In this version of the game, the user will be guessing the computer.

## Rules
- One player (computer) selects a secret combination of coloured pegs. They can use the same colour more than once
- The second player (user) needs to guess that combination
- Feedback is provided after each guess
    - For each correct colour that appears in the code but incorrect position 1 WHITE peg awarded
    - For each correct colour and position combination 1 BLACK peg awarded
- The feedback from the prior guess should help inform the next guess
- Second player only has a fixed number of guesses


## Workflow
- Welcome the player to the game and explain how it works

- Computer to generate the ‘code’ of 3 numbers from a choice of 5.
    - Represents 3 colours from choice of 5, repeats are allowed

- Ask the user to input the colour guess of their first position
    - Repeat for 2nd and 3rd positions
    - Colours translated into numbers

- After all guesses inputted, the player’s guess will be compared to the CPU’s code

- Assess current guess and provide feedback
    - If the user guess matches computer generated code then we have a winner (and stop game)

- If exact match not found then user asked to enter their next guess
    - Repeats for 5 rounds


## Organization
This basic project currently has a flat file structer with the Python file stored in the 'your-code' folder.

## Links
[Background Info on Game](https://www.wikihow.com/Play-Mastermind)  
[Repository](https://github.com/tristar82/Project-Week-1-Build-Your-Own-Game)  
[Slides](https://www.dropbox.com/s/5n55ofqgwygjqoc/EC%20Matermind%20Preso.pdf?dl=0)  
[Trello](https://trello.com/b/cMcIsQ6v/mastermind-project1)  
