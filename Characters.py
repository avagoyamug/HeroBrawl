class Character:
    class_Name = ''
    charCount = 0
    maxHealth = 3
    health = maxHealth
    dash = 0
    push = 0
    swap = False
    objects = {}

    def __init__(self, number):
        self.number = number
        Character.objects[self.number] = self
        Character.charCount += 1

class Dwarf(Character):
    def __init__(self, number):
        self.class_Name = 'Dwarf'
        self.maxHealth = 4
        self.health = self.maxHealth
        self.damage = 1
        self.image = 'hero_dwarf.png'
        Character.charCount += 1
        self.push = 1

class Elf(Character):
    def __init__(self, number):
        self.class_Name = 'Elf'
        self.maxHealth = 3
        self.health = self.maxHealth
        self.damage = 2
        self.image = 'hero_elf.png'
        Character.charCount += 1
        self.push = -1

class Daemon(Character):
    def __init__(self, number):
        self.class_Name = 'Daemon'
        self.maxHealth = 2
        self.health = self.maxHealth
        self.damage = 3
        self.image = 'hero_daemon.png'
        Character.charCount += 1
        self.swap = True

class Berserk(Character):
    def __init__(self, number):
        self.class_Name = 'Berserk'
        self.maxHealth = 3
        self.health = self.maxHealth
        self.damage = 2
        self.image = 'hero_berserk.png'
        Character.charCount += 1
        self.dash = 2