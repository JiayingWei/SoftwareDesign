import math

class Bird(object):
    def __init__(self, t, name, noise, speed, age):
        self.t = t #type of birdey
        self.name = name
        self.speed = speed
        self.age = age
        self.noise = noise
        self.pos = [0, 0] # x,y
    
    def __str__(self):
        return "I am a %s, my name is %s, I am %d years old and fly %d (m/s)" % (self.t, self.name, self.age, self.speed)
    
    def fly(self, flaps, direction):
        rad_dir = math.radians(direction)
        self.pos[0] = self.pos[0] + (self.speed * flaps * math.cos(rad_dir))
        self.pos[1] = self.pos[1] + (self.speed * flaps * math.cos(rad_dir))

    def talk(self, times):
        return self.noise * times
    
    def grow_up(self):
        self.age += 1

class Phoenix(Bird):
    """ Create a child class phoenix that inherits from Bird. 
    """
    def __init__(self, name, speed, age = 13):
        self.name = name
        self.speed = speed
        self.age = age
        self.color = "blue"
        super(Phoenix, self).__init__("phoenix", self.name, '', self.speed, self.age)

    def change_colors(self):
        self.color = "silver"

    def talk(self):
        return "I love giving feedback!"


def main():
    """create an instance of both the parent and child class
    call a method with each
    change an attribute for each
    print each instance
    """
    birdy = Bird("generic bird","birdy", "cheep cheep ", 5, 1)
    phoenixy = Phoenix("Oliner", 1)

    print "old bird speed : " + str(birdy.speed)
    print "old phoenix speed : " + str(phoenixy.speed)

    print "birdey says : " + birdy.talk(5)
    print "pheonixy says : " + phoenixy.talk()

    print birdy
    print phoenixy

    birdy.speed = 1337
    phoenixy.speed = 101

    print "new bird speed : " + str(birdy.speed)
    print "new phoenix speed : " + str(phoenixy.speed)

if __name__ == "__main__":
    main()

