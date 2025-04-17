import random

class Astronaut:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.energy = 50
        self.morale = 50
        self.alive = True
        self.day = 1

    def show_status(self):
        print("------")
        print("Day:", self.day)
        print("Health:", self.health)
        print("Energy:", self.energy)
        print("Morale:", self.morale)
        print("------")

    def do_explore(self):
        print("You go exploring...")
        self.energy -= 10
        self.morale += 5
        chance = random.randint(1, 10)
        if chance <= 3:
            damage = random.randint(5, 20)
            self.health -= damage
            print("You got hurt! -", damage, "health")
        else:
            print("Exploration went fine.")

    def do_repair(self):
        print("You repair the base...")
        self.energy -= 15
        self.morale -= 5
        print("Repairs complete.")

    def do_rest(self):
        print("You take a rest...")
        self.energy += 20
        if self.energy > 100:
            self.energy = 100
        self.morale += 3
        print("You feel rested.")

    def do_communicate(self):
        print("You talk to Earth...")
        self.energy -= 5
        self.morale += 10
        print("You feel more connected.")

    def check_alive(self):
        if self.health <= 0 or self.energy <= 0 or self.morale <= 0:
            self.alive = False

def main():
    name = input("Enter your astronaut's name: ")
    astro = Astronaut(name)

    while astro.alive and astro.day <= 365:
        astro.show_status()
        print("Choose action:")
        print("1 - Explore")
        print("2 - Repair")
        print("3 - Rest")
        print("4 - Communicate")

        choice = input("Your action: ")

        if choice == "1":
            astro.do_explore()
        elif choice == "2":
            astro.do_repair()
        elif choice == "3":
            astro.do_rest()
        elif choice == "4":
            astro.do_communicate()
        else:
            print("Invalid choice.")

        astro.check_alive()
        if astro.alive:
            astro.day += 1
        else:
            print("\nAstronaut", astro.name, "did not survive.")

    if astro.alive:
        print("\nCongrats! Astronaut", astro.name, "survived 365 days on Mars!")

main()
