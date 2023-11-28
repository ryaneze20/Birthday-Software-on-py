import datetime
import sched
import time

class BirthdayApp:
    def __init__(self):
        self.birthdays = {}

    def add_birthday(self, name, date):
        self.birthdays[name] = {"date": date, "age": 0}

    def start_reminders(self):
        s = sched.scheduler(time.time, time.sleep)
        for name, info in self.birthdays.items():
            birthday_date = datetime.datetime.strptime(info["date"], "%Y-%m-%d").date()
            age = self.calculate_age(birthday_date)
            self.birthdays[name]["age"] = age

            reminder_date = birthday_date - datetime.timedelta(days=30)  # 1 month before
            s.enterabs(time.mktime(reminder_date.timetuple()), 1, self.reminder, argument=(name,))
        
        s.run()

    def calculate_age(self, birthdate):
        today = datetime.date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    def reminder(self, name):
        age = self.birthdays[name]["age"]
        print(f"{name} turns {age} years old soon. Click now to get them the perfect gift!")
        response = input("Do you want to take a survey for gift suggestions? (yes/no): ").lower()

        if response == "yes":
            interests = self.take_survey()
            gift = self.suggest_gift(interests)
            location = input("Enter your location (city): ")
            self.suggest_store(gift, location)
        else:
            print("Suggesting a generic gift.")
            print("Redirecting to amazon.com for purchase.")

    def take_survey(self):
        print("Survey: Answer the following questions to determine the interests of the celebrant.")
        interests = []

        questions = [
            "Hobby in one word",
            "Favourite book/movie or show",
            "Gadget on their wishlist right now",
            "Fashion interest in one word",
            "Bucket list plan",
        ]

        for i, question in enumerate(questions, start=1):
            while True:
                answer = input(f"Question {i}: {question} (max 30 characters): ").strip()

                if len(answer) <= 30:
                    interests.append(answer)
                    break
                else:
                    print("Uh oh! Input only one answer per question and limit your answer to 30 characters.")

        return interests

    def suggest_gift(self, interests):
        # Implement your logic to suggest a gift based on the survey answers
        # For simplicity, let's assume a generic gift for now
        return "Generic Gift"

    def suggest_store(self, gift, location):
        # Implement logic to suggest nearby stores based on location
        # For simplicity, let's assume an online store (Amazon) for now
        print(f"Suggesting online store: {gift} - Amazon.com")

def main():
    birthday_app = BirthdayApp()

    # Example: Adding birthdays
    birthday_app.add_birthday("John Doe", "2023-05-15")
    birthday_app.add_birthday("Jane Smith", "2023-07-20")

    # Start reminders
    birthday_app.start_reminders()

if __name__ == "__main__":
    main()


