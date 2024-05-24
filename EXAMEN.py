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
        print(notes)
        maximum=max(notes)
        minimum=min(notes)
        for i in range(len(notes)):
            somme=somme+notes[i]
        moyenne=somme/9
        resultat = f"parmis le nombre que tu as entre le plus grand est {maximum}, et le minum {minimum} et la moyenne {moyenne} "
        print(resultat)
calcul1 = calcul()
calcul1.somme()