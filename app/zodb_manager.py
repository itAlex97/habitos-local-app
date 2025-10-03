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
    """Guarda un objeto Hábito en la base de datos ZODB."""
    connection = db.open()
    try:
        root = connection.root()
        # Añadimos el nuevo objeto a nuestra lista de hábitos
        root['habitos'].append(habit_object)
        # transaction.commit() es lo que realmente guarda los cambios en el archivo.
        transaction.commit()
        print(f"💾 Hábito '{habit_object.name}' guardado en ZODB.")
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
            print(f"🔄 Estado del hábito {habit_id} actualizado a '{new_status}' en ZODB.")
        else:
            print(f"⚠️ Hábito con id {habit_id} no encontrado en ZODB.")
    finally:
        connection.close()