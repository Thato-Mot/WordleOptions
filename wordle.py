class WordleSolver:
    def __init__(self, word_list_file, past_answers_file):
        with open(word_list_file, "r") as f:
            self.possible_words = set(word.strip().lower() for word in f if len(word.strip()) == 5)
        
        with open(past_answers_file, "r") as f:
            line = f.read()
            self.past_answers = line.split()
            self.past_answers = [word.lower() for word in self.past_answers]

        

        self.known_letters = ["_"] * 5  # Tracks correct letters in correct positions
        self.present_letters = set()  # Tracks known letters (position unknown)
        self.absent_letters = set()  # Tracks letters that are not in the word
        self.invalid_positions = {}
    
    def update_known_letters(self, pattern):
        pattern = pattern.lower()
        if len(pattern) == 5 and all(c.isalpha() or c == "_" for c in pattern):
            self.known_letters = list(pattern)
            self.filter_words()
        else:
            print("Invalid pattern. Use a 5-letter word with underscores for unknown letters.")
    
    def update_present_letter(self, letter):
        for l in letter: 
          self.present_letters.add(l.lower())
        self.filter_words()
    
    def update_absent_letter(self, letter):
        for l in letter:
          self.absent_letters.add(l.lower())
        self.filter_words()
    
    def update_invalid_position(self, letter, positions):
        letter = letter.lower()
        if letter not in self.invalid_positions:
            self.invalid_positions[letter] = set()
        self.invalid_positions[letter].update(positions)
        self.filter_words()

    def filter_words(self):
        self.possible_words = {word for word in self.possible_words if self.is_valid_word(word)}
    
    def is_valid_word(self, word):
        # Ensure the word does not match past answers
        word = word.lower()
        if word in self.past_answers:
            return False
        
        # Check known letters (must match exactly at given positions)
        for i, letter in enumerate(self.known_letters):
            if letter != "_" and word[i] != letter:
                return False
        
        # Check absent letters (must not appear in the word)
        if any(letter in word for letter in self.absent_letters):
            return False
        
        # Check present letters (must be in the word but not in exact known positions)
        if not all(letter in word for letter in self.present_letters):
            return False
        
        for letter in self.present_letters:
            if letter not in word:
                return False

        for letter, bad_positions in self.invalid_positions.items():
            for i in bad_positions:
                if word[i] == letter:
                    return False
        
        return True
    
    def get_suggestions(self):
        return sorted(self.possible_words)[:90]  # Return up to 10 possible words
    
    def display_progress(self):
        print("Current word: ", "".join(self.known_letters))
        print("Present letters: ", self.present_letters)
        print("Absent letters: ", self.absent_letters)
        print("Suggestions: ", self.get_suggestions())
    
    def add_invalid_position(letter_invalids, letter, positions):
        """
        Adds positions to the set of invalid positions for a given letter.

        Parameters:
        - letter_invalids (dict): Dictionary mapping letters to sets of invalid positions.
        - letter (str): The letter being checked.
        - positions (list or set of int): Positions where the letter is *not* allowed.
        """
        if letter not in letter_invalids:
            letter_invalids[letter] = set()
        letter_invalids[letter].update(positions)
    
    

# Example usage:
solver = WordleSolver("words.txt", "past_words.txt")
solver.update_absent_letter('udioste')
solver.update_present_letter('ar')
solver.update_invalid_position('a', [0,3])
solver.update_invalid_position('r', [4])
# solver.update_invalid_position('a', [1,3])
# solver.update_invalid_position('s', [0,4])


solver.update_known_letters("_____")
solver.display_progress()
