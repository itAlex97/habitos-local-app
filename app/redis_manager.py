# app/redis_manager.py
import redis

# Creamos una instancia del cliente de Redis.
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def save_habit(habit_dict):
    """Guarda un hábito en Redis usando un Hash."""
    habit_id = habit_dict['_id']
    key = f"habit:{habit_id}"
    # hmset (ahora hset) guarda el diccionario como un hash en Redis.
    r.hset(key, mapping=habit_dict)
    print(f"Hábito '{habit_dict['name']}' guardado en Redis.")

def update_habit_status(habit_id, new_status):
    """Actualiza el estado de un hábito en Redis."""
    key = f"habit:{habit_id}"
    # hset actualiza un campo específico del hash.
    r.hset(key, "status", new_status)
    print(f"Estado del hábito {habit_id} actualizado a '{new_status}' en Redis.")