class Dog:
    def _init_(self, nombre, edad, ladrido):
        self.nombre=nombre
        self.edad=edad
        self.ladrido=ladrido
    def salute(self):
        print(f"guau, edad {self.edad}")

tilin = Dog("tilin",35,"guau"*5)
tilin.saludo()