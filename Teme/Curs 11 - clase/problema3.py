class Util:
    nr_obiecte = []

    def __init__(self, name='Ghita'):
        self.name = name
        self.nr_obiecte.append({'nume': self.name})

    def __str__(self):
        return "Utilizatorul are numele: `{}` ".format(self.name)


class Izatori(Util):

    def __init__(self, name, user, password):
        super().__init__(name)
        self.user = user
        self.password = password
        # for i in self.nr_obiecte:
        #     try:
        #         if i['password'] == self.password:
        #             if i['nume'] == self.name:
        #                 i['user'] = self.user
        #                 i['password'] = self.password
        #             else:
        #                 self.nr_obiecte.append({
        #                     'nume': self.name,
        #                     'user': self.user,
        #                     'password': self.password})
        #         else:
        #             continue
        #     except KeyError:
        #         continue
        self.nr_obiecte.append({
            'nume': self.name,
            'user': self.user,
            'password': self.password
        })


    def __str__(self):
        return "Utilizatorul: `{0.name}` are userul: `{0.user}` si parola: `{0.password}`".format(self)


class Utilizatori(Izatori, Util):

    def __init__(self, name, user, password):
        super().__init__(name, user, password)

    @classmethod
    def _parole(cls):
        parole_useri = []
        for i in cls.nr_obiecte:
            try:
                if i['password']:
                    parole_useri.append(i['password'])
            except KeyError:
                pass
        return set(parole_useri)

    @classmethod
    def _useri(cls):
        users = []
        for i in cls.nr_obiecte:
            try:
                if i['user']:
                    users.append(i['user'])
            except KeyError:
                pass
        return set(users)

    def __str__(self):
        return "Utilizatorul: `{0.name}` are userul: `{0.user}` si parola: `{0.password}`".format(self)


ionut = Util("Ionut")
liviu = Izatori('Liviu', "liviu", "parola_liviu")
stefan = Utilizatori("Stefan", "stefan", "parola_stefan")
george = Utilizatori("George", "george", "parola_george")
# print(ionut)
# print(liviu)
# print(stefan)
# print(george)
# print(Util.nr_obiecte)
# print(Izatori.nr_obiecte)
# print(Utilizatori.nr_obiecte)

# Am rezilvat cu classmethod
useri = Utilizatori._useri()
print(useri)

parole = Utilizatori._parole()
print(parole)
