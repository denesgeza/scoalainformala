class Catalog:

    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        self.absente = 0
        self.materii = {}

    def __str__(self):
        return f'`Nume: {self.nume} {self.prenume}, Absente: {self.absente}, Note: {self.materii}'

    def increment_abs(self):
        self.absente += 1

    def delete_abs(self, numar):
        if self.absente - numar > 0:
            self.absente -= numar
        else:
            pass


class Extensie1(Catalog):
    def __init__(self, nume, prenume):
        super().__init__(nume, prenume)

    def add_materie(self, materie, nota):
        self.materie = self.materii.update({materie: nota})

    def final_grade(self):
        note_finale = {}
        for i, j in self.materii.items():
            if all(isinstance(x, int) for x in j):
                medie = sum(j) / len(j)
            note_finale.update({i: medie})
        return note_finale


student = Extensie1('Roata', 'Ion')
student.increment_abs()
student.increment_abs()
student.increment_abs()
student2 = Extensie1('George', 'Cerc')
student2.increment_abs()
student2.increment_abs()
student2.increment_abs()
student2.increment_abs()
student2.delete_abs(2)
print(f'{student}\n{student2}')

student3 = Extensie1('Veronica', 'Micle')
student3.add_materie('Python', [7, 8, 9])
student2.add_materie('Python', [8, 9, 8])
student3.increment_abs()
print(student3)
print(student2.final_grade())
print(student3.final_grade())

