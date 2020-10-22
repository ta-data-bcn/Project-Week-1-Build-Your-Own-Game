<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Encryption & Decryption program
*[Yago Mougán]*

*[BCN Data Analytics, January 2020]*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
The project consist in the coding of encryption and decryption programs. 
The encryption system will be Caesar Cipher, and it´s done in a way that allows the same program both to encrypt and decrypt any message, given a number of jumps.

## Rules
To modify a message the user will write it down, and then select the number of displacements. 

## Workflow
Firstly I tested trivial systems to codify numbers through calculations, so I could get used to the basic nature of the game. Once I started to elaborate the complete system, my first thought was to use a dictionary, but this proved to be needlessly hard as soon as realized I could just take advantage from the index of any list.
The list to get the characters was firstly string.printable, but the whitelist including line jumps and tabulations makes the outputs look chaotic, and the position of the digits match their positions in the list, which could make the encryptions somehow more obvious, so finally I decided to make a complete list myself from general "string." libraries, without the whitelist (but adding space as an independent string) and the digits in a central position. 
The initial encryption system was with a permanent and very low number of steps, and the same number with opposite sign for the decryption code. Since one of both codes should be positive, the input of the last elements on the list will make an 'out of range' error, so whatever code included the positive steps should have a different list, with the first elements copied at the end, so it avoids the error and creates the effect of going from the end to the start of the list.
This fulfills the project requirements, but permanent number of steps and avoiding the 'out of range' in a so artificial way was unpleasent, so I started to explore the idea of modifying the access to the lists, which would allow any number of steps, which would allow the user to decide this number. To do this, I had to create and modify the input for the steps, to convert any integer into an equivalent displacement inside the list´s range. This resulted in four 'if' situations: positives inside range, negatives inside range, positives out of range, and negatives out of range. Working in the number of steps allowed to use always the same list, so both encryption and decryption can be done now through the same program.
The final steps was fixing several problems with the calculations and polishing the string messages for user.

## Organization
I used the kanban board in trello and handwrite notes.

## Links

[Repository](https://github.com/Yaguit/Project-Week-1-Build-Your-Own-Game)  
[Slides](https://slides.com/)  
[Trello](https://trello.com/b/Su4C6MTj/byog-encryptiondecryption)  
