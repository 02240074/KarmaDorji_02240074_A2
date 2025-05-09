import random

class GuessNumberGame:
    def __init__(self):
        self.score = 0
        self.guesses = 0
    
    def play(self):
        print("\n--- Guess Number Game ---")
        print("I'm thinking of a number between 1 and 20. Can you guess it?")
        
        number = random.randint(1,20)
        self.guesses = 0
        
        while True:
            try:
                guess = int(input("Enter your guess (1-20): "))
                self.guesses += 1
                
                if guess < 1 or guess > 20:
                    print("Please enter a number between 1 and 20.")
                    continue
                
                if guess < number:
                    print("Too low! Try again.")
                elif guess > number:
                    print("Too high! Try again.")
                else:
                    self.score = max(0, 20 - self.guesses * 10)
                    print(f"Congratulations! You guessed it in {self.guesses} tries.")
                    print(f"Your score: {self.score}")
                    break
            except ValueError:
                print("Please enter a valid number.")

class RockPaperScissorsGame:
    """Class for the Rock Paper Scissors game"""
    def __init__(self):
        self.wins = 0
        self.choices = ['rock', 'paper', 'scissors']
    
    def play(self):
        print("\n--- Rock Paper Scissors Game ---")
        print("Enter 'rock', 'paper', or 'scissors'")
        
        while True:
            user_choice = input("Your choice (or 'quit' to end): ").lower()
            
            if user_choice == 'quit':
                print(f"Game over. You won {self.wins} times.")
                break
            elif user_choice not in self.choices:
                print("Invalid choice. Please try again.")
                continue
            
            computer_choice = random.choice(self.choices)
            print(f"Computer chose: {computer_choice}")
            
            if user_choice == computer_choice:
                print("It's a tie!")
            elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                 (user_choice == 'paper' and computer_choice == 'rock') or \
                 (user_choice == 'scissors' and computer_choice == 'paper'):
                self.wins += 1
                print("You win!")
            else:
                print("You lose!")

class TriviaGame:
    """Class for the Trivia Pursuit game"""
    def __init__(self):
        self.score = 0
        self.questions = {
            "Science": [
                {"question": "What is the chemical symbol for gold?", "options": ["A. Go", "B. Au", "C. Gd", "D. Ag"], "answer": "B"},
                {"question": "How many bones are in the human body?", "options": ["A. 106", "B. 206", "C. 306", "D. 406"], "answer": "B"}
            ],
            "History": [
                {"question": "In which year did World War II end?", "options": ["A. 1943", "B. 1945", "C. 1947", "D. 1950"], "answer": "B"},
                {"question": " When did Bhutan join the United Nations??", "options": ["A. 1949", "B. 1907", "C. 1971", "D. 1975"], "answer": "C"}
            ]
        }
    
    def play(self):
        print("\n--- Trivia Pursuit Game ---")
        print("Choose a category:")
        
        for i, category in enumerate(self.questions.keys(), 1):
            print(f"{i}. {category}")
        
        try:
            cat_choice = int(input("Enter category number: ")) - 1
            selected_category = list(self.questions.keys())[cat_choice]
            
            for question in self.questions[selected_category]:
                print(f"\n{question['question']}")
                for option in question['options']:
                    print(option)
                
                user_answer = input("Your answer (A/B/C/D): ").upper()
                if user_answer == question['answer']:
                    self.score += 1
                    print("Correct!")
                else:
                    print(f"Wrong! The correct answer is {question['answer']}.")
            
            print(f"\nYour score: {self.score}/{len(self.questions[selected_category])}")
        except (ValueError, IndexError):
            print("Invalid category selection.")

class GameCollection:
    """Main class to manage the game collection"""
    def __init__(self):
        self.guess_game = GuessNumberGame()
        self.rps_game = RockPaperScissorsGame()
        self.trivia_game = TriviaGame()
        self.pokemon_binder = None 
        self.overall_scores = {
            "Guess Number": 0,
            "Rock Paper Scissors": 0,
            "Trivia": 0,
            "Pokemon Cards": 0
        }
    
    def show_scores(self):
        print("\n--- Overall Scores ---")
        for game, score in self.overall_scores.items():
            print(f"{game}: {score}")
    
    def run(self):
        while True:
            print("\nSelect a game:")
            print("1. Guess Number game")
            print("2. Rock Paper Scissors game")
            print("3. Trivia Pursuit Game")
            print("4. Pokemon Card Binder Manager")
            print("5. Check Current Overall score")
            print("6. Exit program")
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == "1":
                self.guess_game.play()
                self.overall_scores["Guess Number"] = self.guess_game.score
            elif choice == "2":
                self.rps_game.play()
                self.overall_scores["Rock Paper Scissors"] = self.rps_game.wins
            elif choice == "3":
                self.trivia_game.play()
                self.overall_scores["Trivia"] = self.trivia_game.score
            elif choice == "4":
                print("Linking to Pokemon Card Binder Manager...")
                from KarmaDorji_02240074_A2_PB import PokemonBinder
                Game = PokemonBinder()
                Game.run()
            elif choice == "5":
                self.show_scores()
            elif choice == "6":
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please enter a number 1-6.")

if __name__ == "__main__":
    games = GameCollection()
    games.run()