[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18836417&assignment_repo_type=AssignmentRepo)
# Project #4 Make Some Flash Cards

## Requirements

Create 20 flashcards. Each card has:
* a text prompt that will be displayed to the user
* a correct answer that can by typed in
  
Show the flashcards in a random order
* get user's response
* check if the response is correct

Use file I/O to keep track of user performance, e.g.
* How many questions did the user get right vs wrong
* Which questions did the user get right vs wrong

Use the user input data (performance or other text input) to change the way you show the flashcards. Each time the user runs the program, the behavior of your flashcards program should change. Here are some ideas:
* Show flashcards that a user got wrong more frequently than the ones they got right
* Stop showing a flashcard once the user gets it right a certain number of times
* Implement the The Leitner System (look it up on Wikipedia or ask Ms Paley if you're interested in this)
* Let the user answer questions about how many flashcards they want to see, or which flashcards they want to see more frequently

After each run of the program, print out statistics
* Include information about *this* time the user is running the program AND
* Include a summary of the user's past performance

Extra credit options:
* Allow a user to "login" with a specific username, so different people can use your system and keep track of their results separately.
* Let the user choose from different flashcard decks
* Let the user choose how many times they want to see each flash card, or what difficulty they want
* EXTRA-extra-credit option: make a visual interface. Try exploring tkinter.
