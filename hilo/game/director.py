from game.shuffler import Shuffler

class Director:
    """Directs the control of the game"""

    def __init__(self):
        """Variables used"""

        self.keep_playing = True
        self.score = 300
        self.old_score = 300
        self.shuffle = Shuffler()
        self.green = '\033[92m'
        self.red = '\033[91m'
        self.color_clear = '\033[0m'

    def start_game(self):
        """Starts the game"""

        print("Hello welcome to HiLo")

        while self.keep_playing:
            # Give user score and last card
            color = self.check_score()
            print(f"{color}Your score: {self.score}{self.color_clear}")
            old_card = self.shuffle.get_card("old")
            print(f"Your last card was: {old_card}")

            # Ask high or low
            user_input = self.get_inputs()
            if user_input == "q":
                self.keep_playing = False
                continue
            
            # Get new card
            self.shuffle.shuffle_deck()
            new_card = self.shuffle.get_card("new")
            print(f"Your new card was: {new_card}")

            # Give back score
            points = self.shuffle.get_points(user_input)
            self.score += points

            # Checks if they can go again
            if self.score <= 0:
                self.keep_playing = False

        print("Thanks for playing")
    
    def check_score(self):
        """Checks your score to return a color"""

        color_picker = self.red

        if self.score - self.old_score >= 0:
            color_picker = self.green
        self.old_score = self.score
        return color_picker

        
    def get_inputs(self):
        """Checks the user input"""

        valid_input = True
        while valid_input:
            user_input = input("Please enter h or l. You may use \"q\" to quit: ")
            if self.quit(user_input): return "q"
            # Clean inputs
            if not self.check_input(user_input): continue
            # Check if high or low and returns boolean
            return self.user_bool(user_input)
    
    def quit(self, user_input):
        """Quits out of the program"""

        if user_input =="q":
            return True
        return False

    def check_input(self, user_input):
        """Checks if input is valid"""

        if user_input in {"h", "H", "l", "L"}:
            return True
        return False
    
    def user_bool(self, user_input):
        """Checks if high or low"""

        if user_input in {"h","H"}:
            return True
        return False
