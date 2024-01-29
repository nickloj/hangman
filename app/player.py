class Player:

    def __init__(self, max_attempts=7):
        self.guessed_letters = set()
        self.attempts_left = max_attempts

    def make_guess(self):
        guess = input("Guess a letter: ").lower()
        while not (guess.isalpha() and len(guess) == 1) or guess in self.guessed_letters:
            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid input. Please enter a single letter.")
            else:
                print("You have already guessed that letter. Try a different one.")
            guess = input("Guess a letter: ").lower()
        self.guessed_letters.add(guess)
        return guess

    def update_attempts(self, is_correct_guess):
        if not is_correct_guess:
            self.attempts_left -= 1
