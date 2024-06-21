class AIOMath:
    def __init__(self, value:int) -> None:
        self.value = value
    def factorial(self) -> int:
        if self.value == 0:
            return 1
        else:
            return self.value * AIOMath(self.value - 1).factorial()