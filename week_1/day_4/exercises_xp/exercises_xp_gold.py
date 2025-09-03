# ------ Exercise 1

class BankAccount:
    def __init__(self, balance=0):
        """Initialize the account with an optional starting balance."""
        self.balance = balance

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Withdraw a positive amount from the account."""
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise Exception("Insufficient funds.")
        self.balance -= amount
        return self.balance


# ------ Exercise 2

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise Exception("Insufficient funds")
        self.balance -= amount

    def __str__(self):
        return f"Account(owner={self.owner}, balance={self.balance})"


class MinimumBalanceAccount(BankAccount):
    def __init__(self, owner, balance=0, minimum_balance=0):
        super().__init__(owner, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.balance - amount < self.minimum_balance:
            raise Exception("Withdrawal would put balance below minimum balance")
        self.balance -= amount


# Example usage:
acct = MinimumBalanceAccount("Alice", balance=500, minimum_balance=100)

print(acct)   # Account(owner=Alice, balance=500)

acct.withdraw(300)   # OK (balance becomes 200)
print(acct)

try:
    acct.withdraw(150)  # ❌ This would put balance at 50, below minimum 100
except Exception as e:
    print("Error:", e)


# ------ Exercise 3

class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False  # default

    def authenticate(self, username, password):
        """Authenticate the user with username and password."""
        if self.username == username and self.password == password:
            self.authenticated = True
            print("Authentication successful.")
        else:
            raise Exception("Invalid username or password")

    def deposit(self, amount):
        """Deposit money if authenticated."""
        if not self.authenticated:
            raise Exception("User not authenticated. Please log in.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """Withdraw money if authenticated."""
        if not self.authenticated:
            raise Exception("User not authenticated. Please log in.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise Exception("Insufficient funds")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")


# Example usage:
acct = BankAccount("john_doe", "secure123", 500)

try:
    acct.deposit(100)  # should raise exception (not authenticated yet)
except Exception as e:
    print(e)

acct.authenticate("john_doe", "secure123")
acct.deposit(100)
acct.withdraw(200)


# ------ Exercise 4

class BankSystem:
    def __init__(self, account_list, try_limit):
        # Validate account_list contains BankAccount or MinimumBalanceAccount
        if not isinstance(account_list, list) or not all(
            isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list
        ):
            raise Exception("account_list must contain BankAccount or MinimumBalanceAccount instances.")
        
        self.account_list = account_list

        # Validate try_limit is a positive number
        if not isinstance(try_limit, int) or try_limit <= 0:
            print("Invalid try_limit, defaulting to 2")
            self.try_limit = 2
        else:
            self.try_limit = try_limit

        self.current_tries = 0

        # Show the main menu
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Log in")
            print("2. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")

    def log_in(self, username, password):
        # Check against all accounts
        for account in self.account_list:
            if account.authenticate(username, password):
                print(f"Welcome {username}!")
                self.show_account_menu(account)
                return
        
        # Failed login
        self.current_tries += 1
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down.")
            exit()
        else:
            print("Invalid username or password. Please try again.")

    def show_account_menu(self, account):
        while True:
            print("\n--- Account Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid choice, try again.")


# Example dummy classes for testing
class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance

    def authenticate(self, username, password):
        return self.username == username and self.password == password

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, min_balance=50):
        super().__init__(username, password, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print("Withdrawal denied. Minimum balance requirement not met.")
        else:
            super().withdraw(amount)


# Example usage
if __name__ == "__main__":
    accounts = [
        BankAccount("alice", "1234", 500),
        MinimumBalanceAccount("bob", "abcd", 300, 50),
    ]

    BankSystem(accounts, try_limit=3)


# ------ Exercise 5

# ------ Exercise 6

# ------ Exercise 7

# ------ Exercise 8
