import random

# --- Tic-Tac-Toe Functions ---

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print('---------')
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print('| ' + ' | '.join(row) + ' |')
    print('---------')

def check_winner(board, player):
    """Checks if the given player has won."""
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]             # diagonals

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    """Checks if the game is a draw."""
    return ' ' not in board

def player_move(board):
    """Handles player's move."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("This position is already taken.")
        except (ValueError, IndexError):
            print("Please enter a valid move (1-9).")

def computer_move(board):
    """Handles computer's move using a random strategy."""
    while True:
        move = random.randint(0, 8)
        if board[move] == ' ':
            board[move] = 'O'
            break

def tic_tac_toe():
    """Main game loop for Tic-Tac-Toe."""
    board = [' ' for _ in range(9)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        computer_move(board)
        print("Computer's move:")
        print_board(board)
        if check_winner(board, 'O'):
            print("Computer wins! Better luck next time.")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

# --- Hangman Functions ---

def get_random_word():
    """Selects a random word from the list."""
    word_list = ["python", "development", "hangman", "programming", "computer"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Displays the word with guessed letters and underscores for missing ones."""
    displayed_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"Word: {displayed_word}")

def hangman():
    """Main game loop for Hangman."""
    print("Welcome to Hangman!")
    word = get_random_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        display_word(word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! The letter '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word '{word}' correctly!")
                break
        else:
            attempts -= 1
            print(f"Wrong guess! The letter '{guess}' is not in the word. Attempts remaining: {attempts}")
            guessed_letters.add(guess)

        if attempts == 0:
            print(f"Sorry, you lost! The word was '{word}'.")

# --- Main Menu ---

def main():
    while True:
        print("\nWelcome to the Game Center!")
        print("1. Play Tic-Tac-Toe")
        print("2. Play Hangman")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            tic_tac_toe()
        elif choice == '2':
            hangman()
        elif choice == '3':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
