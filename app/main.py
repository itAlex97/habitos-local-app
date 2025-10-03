# app/main.py
from . import redis_manager
from . import zodb_manager
from .habit_model import Habit

def create_habit():
    # Pide datos al usuario y guarda el nuevo hábito en AMBAS bases de datos."""
    print("\n--- Crear Nuevo Hábito ---")
    name = input("Nombre del hábito (ej: Beber 2L de agua): ")
    frequency = input("Frecuencia (ej: Diario, Lunes y Miércoles): ")

    new_habit_obj = Habit(name=name, frequency=frequency)
    habit_dict = new_habit_obj.to_dict()

    print("-" * 20)
    zodb_manager.save_habit(new_habit_obj)
    redis_manager.save_habit(habit_dict)
    print("-" * 20)
    print("¡Hábito creado con éxito en ambas bases de datos!")

def view_habits():
    """Muestra todos los hábitos. Los leeremos desde ZODB."""
    print("\n--- Mis Hábitos ---")
    habits = zodb_manager.get_all_habits()
    if not habits:
        print("No tienes hábitos registrados.")
        return None # <-- CAMBIO: Devolvemos None si no hay hábitos
    else:
        # <-- CAMBIO: Usamos enumerate para obtener un índice (empezando en 1)
        for i, habit in enumerate(habits, 1):
            print(f"[{i}] Hábito: {habit.name}") # <-- CAMBIO: Mostramos el número
            print(f"    Frecuencia: {habit.frequency}")
            print(f"    Estado: {habit.status}")
            print(f"    (ID: {habit._id})") # Dejamos el ID por si lo necesitas ver
            print("-" * 20)
        return habits # <-- CAMBIO: Devolvemos la lista de hábitos para usarla después

def update_habit():
    """Actualiza el estado de un hábito a 'completado'."""
    print("\n--- Actualizar Hábito ---")

    # <-- CAMBIO: Obtenemos la lista de hábitos para poder seleccionarla
    habits = view_habits()

    # Si no hay hábitos, no continuamos
    if not habits:
        return

    try:
        choice_num = int(input("Ingresa el NÚMERO del hábito que quieres marcar como 'completado': "))

        # Verificamos que el número esté en el rango correcto
        if 1 <= choice_num <= len(habits):
            # Obtenemos el hábito seleccionado (restando 1 porque las listas empiezan en 0)
            habit_to_update = habits[choice_num - 1]
            habit_id = habit_to_update._id
            new_status = "completado"

            print("-" * 20)
            zodb_manager.update_habit_status(habit_id, new_status)
            redis_manager.update_habit_status(habit_id, new_status)
            print("-" * 20)
            print("¡Hábito actualizado con éxito en ambas bases de datos!")
        else:
            print("Número fuera de rango. Inténtalo de nuevo.")

    except ValueError:
        print("Entrada no válida. Por favor, ingresa solo un número.")


def main():
    """Función principal que muestra el menú y gestiona el flujo."""
    while True:
        print("\n===== App de Hábitos Personales =====")
        print("1. Crear nuevo hábito")
        print("2. Ver mis hábitos")
        print("3. Marcar hábito como completado")
        print("4. Salir")
        choice = input("Elige una opción: ")

        if choice == '1':
            create_habit()
        elif choice == '2':
            view_habits()
        elif choice == '3':
            update_habit()
        elif choice == '4':
            print("¡Hasta pronto!")
            zodb_manager.close_db()
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()