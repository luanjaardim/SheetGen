class ElementData:
    class Material:
        def __init__(self, name: str, description: str):
            self.name = name
            self.description = description
            self.quantity = 0
            self.price = 0.0

        def totalPrice(self) -> float:
            return self.quantity * self.price

    def __init__(self, name: str, materials: list[Material] = []):
        self.name = name
        self.materials = materials
