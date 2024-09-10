import random

def get_player_move():
    while True:
        try:
            move = input("Enter your move (r)ock, (p)aper, (s)cissors, or (q)uit: ").lower()
            if move in ('r', 'p', 's', 'q'):
                return move
            print("Invalid input. Please enter r, p, s, or q.")
        except ValueError:
            print("Invalid input. Please enter a letter.")

def get_computer_move():
    return random.choice('rps')

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    elif (player_move == 'r' and computer_move == 's') or \
         (player_move == 'p' and computer_move == 'r') or \
         (player_move == 's' and computer_move == 'p'):
        return "win"
    else:
        return "lose"

def print_scoreboard(wins, losses, ties):
    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")

def main():
    wins = 0
    losses = 0
    ties = 0

    while True:
        print_scoreboard(wins, losses, ties)
        player_move = get_player_move()

        if player_move == 'q':
            break

        computer_move = get_computer_move()

        print(f"{player_move} vs. {computer_move}")

        result = determine_winner(player_move, computer_move)

        if result == "tie":
            print("It's a tie!")
            ties += 1
        elif result == "win":
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1

if __name__ == "__main__":
    main()