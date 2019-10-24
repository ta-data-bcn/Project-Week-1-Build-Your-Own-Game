<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

## Soldier and Dice: Risk  
*Ana Recio de Mur*

*[Data Analytics, Ironhack Barcelona, October 2019]*

## Content
- [Project Description](#project)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
The project consists of the coding of the game Risk. I chose it because I played recently and thought it followed a logical pattern I wanted to code.

## Rules
    1. Player chooses total soldiers from territory. 
    2. Player chooses number of soldiers to attack with. The number of soldiers attacking can't be higher than 3 and there always has to be one soldier remaining in the territory i.e. if I have 5 soldiers I can attack with 1, 2 or 3, however, if I have 2, I can only attack with 1.  
    3. The opponent chooses the number of soldiers to defend with. The maximum number of soldiers to defend with is 2 and the defendant can defend only with 1 soldier. 
    4. For the battle each dice represents one soldier. Each player throws their corresponding dices simultaneously. 
    5. The dices are compared, the maximum number of the attacker is compared with the maximum number of the defendant. The looser after the comparison, looses one soldier. In case the defendant is defending with 2 soldiers, the second maximum number of the attacker is compared with the second maximum number of the defendant. The looser of this comparison looses one soldier. 
    6. The battle keeps going until the defendant has no soldiers or the attacker only has one soldier left, since with one soldier you can't attack. 

## Workflow
1. Importing RegExp library and random library
2. Defining functions to check if the user input is correct according to the game rules, limiting the possible answers via RegExp
3. Ask the user to choose the soldiers 
4. Creating a while loop so that the battle continues as long as the attacker has more than one soldier left and the defendant has soldiers. The following steps happen in the while loop. 
5. Generating a list per player with the corresponding dice results 
6. Comparing the maximum elements of the generated lists and removing a soldier from the loser.
7. Removing the previous maximum elements from the lists, comparing the remaining maximum values per list and removing a soldier from the loser, until there are no more elements to compare. 


## Organization 

I used notion to organise my work. Stating each step with a sentence. 

Folder: Project-Week-1-Build-Your-Own-Game
Inside the folder: .ipynb .README.md


## Links
Repo: https://github.com/anarmcm/Project-Week-1-Build-Your-Own-Game

[Repository](https://github.com/)  
[Slides](https://slides.com/)  
[Trello](https://trello.com/en)  
