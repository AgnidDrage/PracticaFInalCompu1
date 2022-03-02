
class ListaMusical:
    def __init__(self, temas={}):
        self.temas = temas

    def add(self, tema):
        for k, v in self.temas.items():
            if tema == v:
                raise KeyError
        self.temas[tema.codigo] = tema

    def update(self, tema, codigo):
        if codigo in self.temas:
            self.temas[codigo] = tema
        else:
            raise KeyError

    def delete(self, codigo):
        if codigo in self.temas:
            del self.temas[codigo]
        else:
            raise KeyError

    def find_by_id(self, codigo):
        for k, v in self.temas.items():
            if codigo == k:
                return v
            else:
                raise KeyError

    def find_all(self):
        temas = []
        for k, v in self.temas.items():
            temas.append(v)
        return temas


    def __str__(self):
        return str(self.temas)


