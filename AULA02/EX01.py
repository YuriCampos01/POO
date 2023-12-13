class Animal:
    def emitir_som(self):
        pass

    def mover(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"

    def mover(self):
        return "Correndo"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

    def mover(self):
        return "Andando furtivamente"

class Passaro(Animal):
    def emitir_som(self):
        return "Piu piu!"

    def mover(self):
        return "Voando"

# Exemplos de uso
cachorro = Cachorro()
print("Cachorro:", cachorro.emitir_som(), "-", cachorro.mover())

gato = Gato()
print("Gato:", gato.emitir_som(), "-", gato.mover())

passaro = Passaro()
print("Pássaro:", pa
