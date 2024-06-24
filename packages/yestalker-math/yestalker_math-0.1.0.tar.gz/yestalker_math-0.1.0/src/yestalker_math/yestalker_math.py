class Math:
    def __init__(self):
        pass
    def jam(self, *numbers:float):
        result = 0
        for number in numbers:
            result += number
        return result
    def tafriq(self, *numbers:float):
        result = numbers[0]
        for number in numbers:
            result -= number
        return result
    def zarb(self, *numbers:float):
        result = numbers[0]
        for number in numbers:
            result *= number
        return result
    def taqsim(self, *numbers:float):
        result = numbers[0]
        for number in numbers:
            result /= number
        return result
    def tavan(self, *numbers:float):
        result = numbers[0]
        for number in numbers:
            result **= number
        return result