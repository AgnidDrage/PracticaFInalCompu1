class TemaMusical:
    def __init__(self, codigo=None, nombre=None, duracion=0, interprete=None):
        self.codigo = codigo
        self.nombre = nombre
        self.duracion = duracion
        self.interprete = interprete

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        if codigo == '':
            raise EmptyError('El código no puede estar vacío')
        self._codigo = codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if nombre == '':
            raise EmptyError('El nombre no puede estar vacío')
        self._nombre = nombre

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, duracion):
        if duracion < 0:
            raise ValueError('La duración no puede ser negativa')
        self._duracion = duracion

    @property
    def interprete(self):
        return self._interprete

    @interprete.setter
    def interprete(self, interprete):
        if interprete == '':
            raise EmptyError('El interprete no puede estar vacío')
        self._interprete = interprete

    def input(self, state=False):
        if state is False:
            self.codigo = input('Agregue un codigo')
            self.nombre = input('Agregue un nombre')
            self.duracion = int(input('Agregue una duracion'))
            self.interprete = input('Agregue un interprete')
            return TemaMusical(self.codigo, self.nombre, self.duracion, self.interprete)
        else:
            self.nombre = input('Agregue un nombre')
            self.duracion = int(input('Agregue una duracion'))
            self.interprete = input('Agregue un interprete')
            return TemaMusical(self.codigo, self.nombre, self.duracion, self.interprete)

    def __str__(self):
        return 'codigo: {}\n\tnombre: {}\n\tduracion: {}\n\tinterprete: {}\n'.format(self._codigo, self._nombre, self._duracion, self._interprete)


class EmptyError(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)
