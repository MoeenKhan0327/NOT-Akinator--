import random
from util import yes_no_question, question_sanitizer

class Game_Session:
  def __init__(self, mode='user_guesses', category='Persons', difficulty='medium'):
    self.mode = mode
    self.category = category
    self.difficulty = difficulty
    self.open_question_limit = self.set_difficulty(difficulty)
    self.open_question_count = 0
    self.history = []
    self.answer = self.pick_random_entity()

  def set_difficulty(self, level):
    if level == 'easy':
      return 5
    elif level == 'hard':
      return 1
    else:
      return 3 # medium difficulty be default
  def pick_random_entity(self):
    #Temporary static entity for now, use wikipedia fetch later
    random_entity = {
      "Person": "Allama Iqbal",
      "Place": "Changa Manga",
      "Thing": "Pen"
    }
    return random_entity.get(self.category, "Mystery")

  def ask_question(question):
    question = question_sanitizer(question)
    self.history.append(question)
    if not yes_no_question(question):
      self.open_question_count += 1
      if self.open_question_count > self.open_question_limit:
        return {
          "valid": False,
          "game_over": True,
          "message": f"Too many open-ended questions! You were allowed only {self.open_question_limit}"
        }
      return {
        "valid": False,
        "game_over": True,
        "message": "Please ask only yes or no questions.
      }
      #Placeholder yes no answer for now
      answer = random.choice(['yes', 'no'])
      return {
        "valid": True,
        "game_over": False,
        "message": answer
      }
  def get_history(self):
    return self.history


























