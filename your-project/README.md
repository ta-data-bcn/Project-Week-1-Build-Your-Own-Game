<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Title of Your Project
*[Andreu Carreño Mateu]*

*[Data Science, Barcelona, 03/04/20]*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
This project was pretty straight forward. As the name says, I had to create a program capable of generating strong passwords.

## Rules
It's not a game so it doesn't have 'rules' per se, but I've taken the needed parameters are a manner or rules, so the password:

- Had be at least 15 characters long
- It must contain at least one 'uppercase letter'
- It must contain at least one 'lowercase letter'
- It must contain at least one number
- It must contain at least one Sybmol 
- It won't be any word in the dictionary
- It won't be a keyboard pattern
- It won't be the users name 
- It won't be the users birth date



## Workflow
First I thought about the problem as a whole to see which parts would be the most problematic.
After doing some rough calculations I saw the the last 4 'Rules' are far too little of a possibility that I've decided to treat them as insignificant.
Then I created a function that interacts with the user to ask the number of characters they want their password to have.
In the function I added some error handling so that the user can't type anything but a number in between 15 and 20 which is a fair length for a strong passord
Then after trying to do the random generation in for loops I remembered the choice funcion build in the random library (that I used in the prework) could do the trick much easier, so I went with it.
Then I tested several times that the output of my program were indeed strong passwords and I attached an external link so the users can check it up by themselves and feel sae with the result.
(I realize I could've made this a bit more interactive or more restricting, but I think this solution work for now)

## Organization
This project is not so long so I didn't need to use any specific tool to organize it, nevertheless I started using the trello board below so I can start getting use to it before the war begins.
In my repository you'll only find the main program and the readme file along with the .gitignore file.


## Links
Include links to your repository, slides and kanban board. Feel free to include any other links associated with your project.

[Repository](https://github.com/andreuCM11/Project-Week-1-Build-Your-Own-Game)  
[Slides](https://docs.google.com/presentation/d/1f-UU6WsoFg7gzFugpmdS-K6kju1m4wkyjrEQ7RhiSJ0/edit#slide=id.g7296d4b67b_0_6)  
[Trello](https://trello.com/b/XXx62eKN/project1)  
