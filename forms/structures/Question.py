class Question:
  """
  Base class for all question content.
  """
  def __init__(self) -> None:
    """
    Primary base constructor
    """
    self.question = "Question"
    self.required = False
    self.construct()
  def construct(self) -> None:
    """
    Secondary constructor, to be filled in for subclasses
    """
  def edit_question(self, question) -> None:
    """
    Edit the question content.
    """
    self.question = question
  def toggle_required(self) -> None:
    """
    Toggle whether or not the question is required.
    """
    if self.required:
      self.required = False
    else:
      self.required = True
