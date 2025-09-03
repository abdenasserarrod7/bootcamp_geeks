# ------ Exercise 1

class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        """Simulates a call between two phones."""
        call_record = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_record)
        self.call_history.append(call_record)

    def show_call_history(self):
        """Prints call history of this phone."""
        print("Call History:")
        for call in self.call_history:
            print(call)

    def send_message(self, other_phone, content):
        """Sends a message to another phone."""
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append(message)  # deliver to recipient

    def show_outgoing_messages(self):
        """Prints all messages sent from this phone."""
        print("Outgoing Messages:")
        for msg in self.messages:
            if msg["from"] == self.phone_number:
                print(msg)

    def show_incoming_messages(self):
        """Prints all messages received by this phone."""
        print("Incoming Messages:")
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(msg)

    def show_messages_from(self, number):
        """Prints all messages received from a specific number."""
        print(f"Messages from {number}:")
        for msg in self.messages:
            if msg["from"] == number and msg["to"] == self.phone_number:
                print(msg)


# --------- TESTING ---------
phone1 = Phone("123-456")
phone2 = Phone("987-654")

# Calls
phone1.call(phone2)
phone1.call(phone2)
phone1.show_call_history()

# Messages
phone1.send_message(phone2, "Hello, how are you?")
phone2.send_message(phone1, "I'm good, thanks!")
phone1.send_message(phone2, "Great to hear!")

print("\n--- Phone1 Outgoing ---")
phone1.show_outgoing_messages()

print("\n--- Phone2 Incoming ---")
phone2.show_incoming_messages()

print("\n--- Messages from Phone1 to Phone2 ---")
phone2.show_messages_from("123-456")


# ------ Exercise 2

# ------ Exercise 3

# ------ Exercise 4

# ------ Exercise 5

# ------ Exercise 6

# ------ Exercise 7

# ------ Exercise 8
