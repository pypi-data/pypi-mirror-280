class MyMath:
  def __init__(self, value):
    self.value = value

  def factorial(self):
    if self.value == 0:
      return 1
    else:
      return self.value * MyMath(self.value - 1).factorial()
