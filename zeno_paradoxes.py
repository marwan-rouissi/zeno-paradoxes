import time

class Paradoxe:
    def __init__(self, object_pos, object_speed, target_pos, target_speed):
        self.object_pos = object_pos
        self.object_speed = object_speed
        self.target_pos = target_pos
        self.target_speed = target_speed

    def achille_vs_turtoise(self):
        print("Etape 0")
        print("Achille est à la position", self.object_pos, "et la Tortue est à la position", self.target_pos)
        # programme principal
        step = 0
        while step < 10:
            distance = self.target_pos - self.object_pos
            delta =  distance / self.object_speed
            self.object_pos = self.target_pos
            self.target_pos = self.object_pos + self.target_speed * delta
            print("Etape", step+1)
            print("Achille est à la position", self.object_pos, "et la Tortue est à la position", self.target_pos)
            step += 1
            time.sleep(0.5)
    
    def dichotomie(self):
        print("Etape 0")
        print("La pierre est à la position", self.object_pos, "et l'arbre est à la position", self.target_pos)
        # programme principal
        step = 0
        while self.object_pos < self.target_pos:
            self.object_pos += (self.target_pos - self.object_pos) / 2
            print("Etape", step+1)
            print("La pierre est à la position", self.object_pos, "et l'arbre est à la position", self.target_pos)
            step += 1
            time.sleep(0.5)
    
    def flying_arrow(self):
        print("Etape 0")
        print("La flèche est à la position", self.object_pos, "et la cible est à la position", self.target_pos)
        # programme principal
        step = 0
        while self.object_pos < self.target_pos:
            temps = 1
            self.object_pos += temps * self.object_speed
            print("Etape", step+1)
            print("A la seconde", temps, "la flèche est à la position", self.object_pos, "et la cible est à la position", self.target_pos)
            step += 1
            temps += 1
            time.sleep(0.5)


paradoxe_1 = Paradoxe(0, 10, 100, 2)
paradoxe_1.achille_vs_turtoise()

paradoxe_2 = Paradoxe(0, 0, 100, 100)
paradoxe_2.dichotomie()

paradoxe_3 = Paradoxe(0, 50, 500, 0)
paradoxe_3.flying_arrow()