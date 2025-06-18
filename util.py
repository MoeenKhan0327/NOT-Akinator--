import re

def yes_no_question(question: str) -> bool:
  '''
  Returns True if the question is yes or no
  '''
  yes_no_keywords = ['is', 'are', 'was', 'were', 'can', 'could', 'would', 'should', 'do', 'did', 'has', 'had', 'will', 'might']
  return question.strip().lower().split()[0] in yes_no_keywords

def question_sanitizer(question: str) -> str:
  question = question.strip().lower()
  question = re.sub(r'[^\w\s]', ' ', question)
  question = re.sub(r'\s+', ' ', question)
  return question
