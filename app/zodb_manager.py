# app/zodb_manager.py
import ZODB.FileStorage
import transaction
from .habit_model import Habit

# --- Configuración de la Conexión ---
STORAGE_PATH = 'zodb-data/Habitos.fs'
storage = ZODB.FileStorage.FileStorage(STORAGE_PATH)
db = ZODB.DB(storage)
# ------------------------------------

def save_habit(habit_object):
    connection = db.open()
    try:
        root = connection.root()

        # --- INICIO DE LA CORRECCIÓN ---
        # Primero, verificamos si el "cajón" de hábitos existe.
        if 'habitos' not in root:
            # Si no existe, lo creamos como una lista vacía.
            root['habitos'] = []
        # --- FIN DE LA CORRECCIÓN ---

        # Ahora podemos agregar el hábito con seguridad.
        root['habitos'].append(habit_object)
        transaction.commit()
        print(f"Hábito '{habit_object.name}' guardado en ZODB.")
    finally:
        connection.close()

def get_all_habits():
    """Devuelve todos los objetos Hábito guardados en ZODB."""
    connection = db.open()
    try:
        root = connection.root()
        # .get() es más seguro por si la lista 'habitos' no existiera.
        return list(root.get('habitos', []))
    finally:
        connection.close()

def update_habit_status(habit_id, new_status):
    """Busca un hábito por su ID y actualiza su estado."""
    connection = db.open()
    try:
        root = connection.root()
        habitos = root.get('habitos', [])

        # Buscamos el hábito que coincida con el ID
        habit_found = False
        for habit in habitos:
            if habit._id == habit_id:
                habit.status = new_status # Modificamos el objeto directamente
                habit_found = True
                break

        if habit_found:
            transaction.commit()
            print(f"Estado del hábito {habit_id} actualizado a '{new_status}' en ZODB.")
        else:
            print(f"Hábito con id {habit_id} no encontrado en ZODB.")
    finally:
        connection.close()

def close_db():
    """Cierra la conexión principal a la base de datos."""
    db.close()
    print("Base de datos ZODB cerrada correctamente.")