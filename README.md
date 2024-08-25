Game Center: Tic-Tac-Toe and Hangman
Welcome to the Game Center, a Python-based application that allows you to play two classic games: Tic-Tac-Toe and Hangman. This project provides a simple and interactive way to enjoy these games directly from your terminal.

Features
Tic-Tac-Toe: Play against the computer in a classic game of Tic-Tac-Toe. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.
Hangman: Try to guess the word chosen by the computer one letter at a time. You have a limited number of guesses before you lose.
Main Menu: A simple interface that allows you to select which game to play or to exit the program.
Requirements
Python 3.x
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/sivapriya87/game_center.git
cd game_center
Run the Game

Simply execute the Python script to start the game center.

bash
Copy code
python game_center.py
How to Play
Tic-Tac-Toe
Select "Play Tic-Tac-Toe" from the main menu.
The game board is represented as a 3x3 grid with positions numbered 1 to 9.
Player Move: Enter the number corresponding to the position where you want to place your 'X'.
Computer Move: The computer will randomly select an empty position to place its 'O'.
The first player to get three marks in a row (horizontally, vertically, or diagonally) wins.
If all positions are filled without a winner, the game ends in a draw.
Hangman
Select "Play Hangman" from the main menu.
A random word is selected, and you have to guess it one letter at a time.
You are allowed a maximum of 6 incorrect guesses.
For every correct guess, the letter is revealed in the word.
If you guess all the letters correctly before running out of attempts, you win.
If you run out of attempts without guessing the word, you lose.
Main Menu
After completing a game, you are returned to the main menu where you can choose to play again or exit.
Contributing
Contributions are welcome! If you have any suggestions, feel free to open an issue or submit a pull request.

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a pull request

Acknowledgments
Python documentation and community for their extensive resources and support.
Enjoy playing Tic-Tac-Toe and Hangman!
