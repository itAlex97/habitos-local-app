import uuid

class Habit:
    def __init__(self, name, frequency, status="pendiente"):
        # Generamos un ID único para cada hábito.
        self._id = str(uuid.uuid4())
        self.name = name
        self.frequency = frequency
        self.status = status

    def to_dict(self):
        """
        Convierte el objeto a un diccionario.
        Esto será muy útil para guardar los datos en Redis.
        """
        return {
            "_id": self._id,
            "name": self.name,
            "frequency": self.frequency,
            "status": self.status,
        }

    def __repr__(self):
        """Representación en string para facilitar la depuración."""
        return f"<Habit(name='{self.name}', status='{self.status}')>"