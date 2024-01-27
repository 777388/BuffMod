import sys
class First:
    def __init__(self, firsts, seconds):
        self.firsts = firsts
        self.seconds = seconds

    def attributemod(self):
        attributeamount = self.firsts
        attributemod = self.seconds
        return attributeamount % attributemod
    
    def attributebuff(self):
        attributeamount = self.firsts
        attributebuff = self.seconds
        return attributeamount ** attributebuff
    
class Second(First):
    def __init__(self, firsts, seconds):
        super(Second, self).__init__(int(firsts), int(seconds))
third = Second(int(sys.argv[1]), int(sys.argv[2]))
if sys.argv[3] == "buff":
    print(third.attributebuff())
if sys.argv[3] == "mod":
    print(third.attributemod())