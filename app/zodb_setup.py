import ZODB.FileStorage
import transaction

try:
    # 1. Define dónde se guardará el archivo de la base de datos.
    storage_path = 'zodb-data/Habitos.fs'
    storage = ZODB.FileStorage.FileStorage(storage_path)
    db = ZODB.DB(storage)
    connection = db.open()

    # 2. Obtiene el objeto 'raíz' de la base de datos.
    root = connection.root()

    # 3. Crea una entrada inicial si no existe.
    if 'habitos' not in root:
        root['habitos'] = [] # Creamos una lista para guardar los hábitos
        transaction.commit()
        print("Base de datos ZODB inicializada con éxito.")
        print(f"Archivo de datos creado en: {storage_path}")
    else:
        print("Conexión a ZODB exitosa. Base de datos ya existente.")

    # 4. Cierra la conexión.
    connection.close()

except Exception as e:
    print(f"Error al inicializar ZODB: {e}")