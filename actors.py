import random


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def walk(self):
        print('{} walks around'.format(self.name))

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1,12) * self.level


class Wizard(Creature):
    def attack(self, creature):
        print("The wizard {} attacks {}!".format(
            self.name, creature.name
        ))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print('You roll {}...'.format(my_roll))
        print('{} rolls {}...'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('The wizard has handily triumphed over {}'.format(creature.name))
            return True
        else:
            print('The wizard has been DEFEATED!!!')
            return False


class Dragon(Creature):
    def __init__(self, name, level, scale_thickness, fire_breathing):
        super().__init__(name, level)
        self.scale_thickness = scale_thickness
        self.fire_breathing = fire_breathing

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.fire_breathing else 1
        scale_modifier = self.scale_thickness / 10

        return base_roll * fire_modifier * scale_modifier


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        return super().get_defensive_roll() / 2
