class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Member(Person):
    def __init__(self, name, age, membership_type):
        super().__init__(name, age)
        self.membership_type = membership_type

    def update_membership(self, new_membership_type):
        self.membership_type = new_membership_type
        print(f"{self.name}'s membership has been updated to {self.membership_type}.")

    def display_info(self):
        print(f"Member Name: {self.name}, Age: {self.age}, Membership Type: {self.membership_type}")

class Trainer(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def display_info(self):
        print(f"Trainer Name: {self.name}, Age: {self.age}, Specialization: {self.specialization}")

class GymManagementSystem:
    def __init__(self):
        self.members = []
        self.trainers = []

    def add_member(self, member):
        self.members.append(member)
        print(f"{member.name} has been added as a member.")

    def add_trainer(self, trainer):
        self.trainers.append(trainer)
        print(f"{trainer.name} has been added as a trainer.")

    def display_members(self):
        print("Gym Members:")
        for member in self.members:
            member.display_info()

    def display_trainers(self):
        print("Gym Trainers:")
        for trainer in self.trainers:
            trainer.display_info()

# Example usage
gym_system = GymManagementSystem()

# Adding members
member1 = Member("John Doe", 30, "Gold")
member2 = Member("Jane Doe", 25, "Silver")
gym_system.add_member(member1)
gym_system.add_member(member2)

# Adding trainers
trainer1 = Trainer("Mike Tyson", 45, "Boxing")
trainer2 = Trainer("Arnold Schwarzenegger", 70, "Bodybuilding")
gym_system.add_trainer(trainer1)
gym_system.add_trainer(trainer2)

# Display members and trainers
gym_system.display_members()
gym_system.display_trainers()

# Update a member's membership
member1.update_membership("Platinum")
gym_system.display_members()
