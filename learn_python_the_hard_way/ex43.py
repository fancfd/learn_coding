from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):
    quips = [
            "You died, You kinda suck at this.",
            "Your mom would be proud...if she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this."
        ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]


class CentralCorridor(Scene):

    def enter(self):
        print "You are in central corridor"

        action = raw_input("> ")

        if action == "shoot!":
            print "You enter shoot!"
            return 'death'

        elif action == "dodge!":
            print "You enter dodge!"
            return 'death'

        elif action == "tell a joke":
            print "You tell a joke!"
            return 'Laser_weapn_armory'

        else:
            print "DOES NOT COMPUTE!"
            return "central_corridor"

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass


class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
