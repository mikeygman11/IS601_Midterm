from calculator import Calculator  # Import Calculator using a relative import

class App:
    def __init__(self):
        self.calculator = Calculator()

    def start(self):
        print("Welcome to the Calculator REPL!")
        print("Supported commands: add, subtract, multiply, divide")
        print("Type 'exit' at any prompt to quit.")

        while True:
            command = input("Enter command: ").strip().lower()
            if command == "exit":
                print("Goodbye!")
                break
            if command not in ("add", "subtract", "multiply", "divide"):
                print("Unknown command. Supported commands are: add, subtract, multiply, divide.")
                continue
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            result = self.execute_operation(command, num1, num2)
            print("Result:", result)


    def execute_operation(self, command, num1, num2):
        # Delegate arithmetic to the Calculator module
        if command == "add":
            return self.calculator.add(num1, num2)
        elif command == "subtract":
            return self.calculator.subtract(num1, num2)
        elif command == "multiply":
            return self.calculator.multiply(num1, num2)
        elif command == "divide":
            return self.calculator.divide(num1, num2)
        else:
            # Raise an error if the command is unknown
            print("Unknown command. Supported commands are: add, subtract, multiply, divide.")
            exit()

if __name__ == "__main__":
    App().start()