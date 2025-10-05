# **🛠️ App de Hábitos 100% Local 🛠️**

Este proyecto es una aplicación de consola para el seguimiento de hábitos personales, desarrollada con el objetivo de funcionar de manera **100% local**, sin depender de ningún servicio en la nube.

La aplicación guarda cada hábito de forma simultánea en **dos bases de datos NoSQL diferentes** instaladas y configuradas localmente: una de tipo clave-valor (Redis) y una orientada a objetos (ZODB).

## **✨ Características Principales**

* **Creación de Hábitos:** Permite al usuario definir un nuevo hábito con nombre y frecuencia.  
* **Visualización de Hábitos:** Muestra una lista numerada de todos los hábitos registrados, junto con su estado actual.  
* **Actualización de Estado:** Permite marcar un hábito como "completado" de forma sencilla a través de un menú interactivo.  
* **Persistencia Dual:** Cada operación de escritura se realiza en ambas bases de datos al mismo tiempo.  
* **Funcionamiento Offline:** La aplicación es completamente funcional sin conexión a internet.  
* **Privacidad Garantizada:** Todos los datos del usuario se almacenan exclusivamente en su máquina local.

## **💻 Tech Stack**

| Tecnología | Propósito |
| :---- | :---- |
| **Python 3.10** 🐍 | Lenguaje principal de la aplicación. |
| **Redis** 💾 | Base de datos NoSQL clave-valor para almacenamiento rápido. |
| **ZODB** 🗃️ | Base de datos NoSQL orientada a objetos para persistencia nativa de objetos Python. |
| **WSL (Ubuntu)** 🐧 | Entorno para correr el servidor de Redis en Windows. |
| **Git y GitHub** 🐙 | Control de versiones y alojamiento del código fuente. |

## **📂 Estructura del Proyecto**

/habitos-local-app/  
├── .gitignore          \# Archivos y carpetas a ignorar por Git  
├── app/                \# Módulos de la aplicación  
│   ├── \_\_init\_\_.py  
│   ├── habit\_model.py  \# Modelo de datos del Hábito  
│   ├── main.py         \# Lógica principal y UI de la consola  
│   ├── redis\_manager.py\# Gestor para la conexión con Redis  
│   └── zodb\_manager.py \# Gestor para la conexión con ZODB  
├── screenshots/        \# Capturas de pantalla de la instalación y ejecución  
├── zodb-data/          \# Archivos de la base de datos ZODB (.fs)  
├── logs.txt            \# Diario de desarrollo y solución de errores  
├── README.md           \# Este archivo  
└── requirements.txt    \# Dependencias de Python

## **🚀 Instalación y Ejecución**

Sigue estos pasos para poner en marcha el proyecto en tu máquina local.

### **1\. Prerrequisitos**

* Tener instalado [Git](https://git-scm.com/).  
* Tener instalado [Python 3.10+](https://www.python.org/).  
* Si usas Windows, tener instalado [WSL (Ubuntu)](https://ubuntu.com/wsl).

### **2\. Clonar el Repositorio**

git clone \[https://github.com/\](https://github.com/)\[TU\_USUARIO\]/habitos-local-app.git  
cd habitos-local-app

### **3\. Configurar el Entorno Virtual**

\# Crear el entorno virtual  
python \-m venv venv

\# Activar el entorno (Git Bash en Windows)  
source venv/Scripts/activate

### **4\. Instalar Dependencias**

Con el entorno virtual activado, instala las librerías necesarias.

pip install \-r requirements.txt

### **5\. Iniciar el Servidor de Redis**

Abre una **primera terminal (WSL)** para iniciar Redis.

\# Instalar Redis si no lo has hecho  
\# sudo apt update && sudo apt install redis-server

\# Iniciar el servidor usando el archivo de configuración  
\# (Asegúrate de que la persistencia y el puerto estén bien configurados)  
redis-server /etc/redis/redis.conf

Deja esta terminal abierta.

### **6\. Ejecutar la Aplicación**

Abre una **segunda terminal** en la raíz del proyecto.

\# Asegúrate de tener el entorno virtual activado  
\# source venv/Scripts/activate

\# Ejecutar el script principal  
python \-m app.main

¡Listo\! La aplicación debería estar corriendo y mostrando el menú principal.

## **🐛 Desafíos Superados y Aprendizajes Clave**

Durante el desarrollo se encontraron y solucionaron varios desafíos técnicos que fueron cruciales para el aprendizaje:

* **Conflicto de Puertos en Redis:** Se solucionó identificando y deteniendo procesos preexistentes con lsof y kill, y estandarizando el uso del archivo redis.conf.  
* **Persistencia en ZODB:** Se resolvió el problema de los datos que no se guardaban implementando una función db.close() que se llama explícitamente al salir de la app.  
* **Errores de KeyError:** Se corrigió un error que ocurría al guardar el primer hábito en una base de datos ZODB vacía, añadiendo una verificación para inicializar la lista de hábitos si no existía.  
* **Experiencia de Usuario (UUIDs):** Se mejoró la interfaz de actualización para usar un sistema de índices numéricos \[1\], \[2\], ... en lugar de requerir que el usuario copie y pegue los complejos IDs de los hábitos.

**Autor:** \[Tu Nombre\]