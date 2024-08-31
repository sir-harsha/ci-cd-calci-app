class SimpleCalculator:
    def __init__(self):
        pass
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return abs(a - b)
    
    def multiply(self, a, b):
        return a * b

    def display_menu(self):
        print('Enter your choice:')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiplication')

    def get_choice(self):
        try:
            choice = int(input())
            if choice not in [1, 2, 3]:
                print('Invalid choice. Please choose between 1 and 3.')
                return None
            return choice
        except ValueError:
            print('Invalid input. Please enter a number.')
            return None

    def get_number(self, prompt):
        try:
            return int(input(prompt))
        except ValueError:
            print('Invalid input. Please enter an integer.')
            return None

    def execute(self):
        self.display_menu()
        choice = self.get_choice()
        if choice is None:
            return

        num1 = self.get_number("Enter the first number: ")
        num2 = self.get_number("Enter the second number: ")
        if num1 is None or num2 is None:
            return

        if choice == 1:
            result = self.add(num1, num2)
            print(f"Result: {result}")
        elif choice == 2:
            result = self.subtract(num1, num2)
            print(f"Result: {result}")
        elif choice == 3:
            result = self.multiply(num1, num2)
            print(f"Result: {result}")

if __name__ == '__main__':
    calc = SimpleCalculator()
    calc.execute()
