# superhero.py

# Base class
class Superhero:
    def __init__(self, name, alias, origin_story, power_rating, weakness):
        self.name = name
        self.alias = alias
        self.origin_story = origin_story  # A brief story of how they became a superhero
        self.power_rating = power_rating  # Numeric value representing overall power
        self.weakness = weakness  # A unique vulnerability

    def display_identity(self):
        return (
            f"{self.alias}, known as {self.name}, has an origin story:\n"
            f"{self.origin_story}"
        )

    def show_power_rating(self):
        return f"{self.alias}'s power rating is {self.power_rating}/100."

    def reveal_weakness(self):
        return f"{self.alias}'s weakness is {self.weakness}!"


# Derived class: Mystical Superhero
class MysticalSuperhero(Superhero):
    def __init__(self, name, alias, origin_story, power_rating, weakness, magic_type):
        super().__init__(name, alias, origin_story, power_rating, weakness)
        self.magic_type = magic_type  # Type of magic they specialize in

    def cast_spell(self):
        return f"{self.alias} casts a powerful {self.magic_type} spell!"

    def display_identity(self):
        return (
            super().display_identity()
            + f"\nSpecializes in {self.magic_type} magic."
        )


# Derived class: Tech-Based Superhero
class TechSuperhero(Superhero):
    def __init__(self, name, alias, origin_story, power_rating, weakness, gadgets):
        super().__init__(name, alias, origin_story, power_rating, weakness)
        self.gadgets = gadgets  # List of high-tech gadgets they use

    def use_gadget(self):
        if self.gadgets:
            return f"{self.alias} uses their {self.gadgets[0]}!"
        return f"{self.alias} has no gadgets available right now."

    def display_identity(self):
        return (
            super().display_identity()
            + f"\nKnown for their high-tech gadgets: {', '.join(self.gadgets)}."
        )


# Test the classes
# Base class
hero1 = Superhero(
    "Jane Doe", 
    "Shadow Whisperer", 
    "Born in a land of eternal night, she gained powers after a shadow storm.", 
    72, 
    "Bright light"
)
print(hero1.display_identity())
print(hero1.show_power_rating())
print(hero1.reveal_weakness())

# Mystical superhero
hero2 = MysticalSuperhero(
    "Ezekiel Frost", 
    "Frost Sorcerer", 
    "A traveler cursed with icy powers after touching a cursed artifact.", 
    85, 
    "High temperatures", 
    "Cryomancy"
)
print(hero2.display_identity())
print(hero2.cast_spell())
print(hero2.reveal_weakness())

# Tech-based superhero
hero3 = TechSuperhero(
    "Ava Lin", 
    "Cyber Phantom", 
    "A genius engineer who merged with AI after a failed experiment.", 
    90, 
    "Electromagnetic pulses", 
    ["Holo-shield", "Plasma Rifle", "Jet Boots"]
)
print(hero3.display_identity())
print(hero3.use_gadget())
print(hero3.reveal_weakness())
