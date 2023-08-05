class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @property
    def flour_type(self):
        return self._flour_type

    @flour_type.setter
    def flour_type(self, value):
        if value == "":
            raise ValueError("The flour type cannot be an empty string")
        self._flour_type = value

