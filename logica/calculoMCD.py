class MCDCalculator:
    @staticmethod
    def calcular_mcd(num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1