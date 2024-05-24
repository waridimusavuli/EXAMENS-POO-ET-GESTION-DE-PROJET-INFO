from abc import ABC 
class notes(ABC):
    def somme(self,note):
        self.note = note

class calcul(notes):
    def somme(self):
        notes=[]
        i=0
        somme=0
        while i<9:
            note = int(input(f"taper la note numero {i+1}: "))
            notes.append(note)
            i=i+1
       