from .Question import Question

class MultipleChoiceQuestion(Question):
  """
  Class for multiple choice questions.
  """
  def construct(self) -> None:
    """
    Secondary constructor of ~Question for ~MultipleChoiceQuestion.
    """
    self.options = ["Option 1"]
