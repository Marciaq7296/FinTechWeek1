class Dbz:
    count = 0
    def __init__(self, name, character, powerMove, ss, level):
        self.name = name
        self.character = character
        self.powerMove = powerMove
        self.ss = ss
        self.level = level
        Dbz.count += 1
        
    def levelUp(self):
        self.level += 1
        
### Here are the elements that take on the variables in the
#######  def __int__ -- function 
goku = Dbz("Goku", "main", "kamehameha", "super saiyan blue", 0)
print(goku.level)
goku.levelUp()
print(goku.level)
