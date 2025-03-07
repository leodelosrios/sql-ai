# 🚀 SQL-AI: Consultas en Lenguaje Natural con IA

![SQL-AI](https://img.shields.io/github/stars/leodelosrios/sql-ai?style=social)
![License](https://img.shields.io/github/license/leodelosrios/sql-ai)
![Issues](https://img.shields.io/github/issues/leodelosrios/sql-ai)

**SQL-AI** es una herramienta impulsada por inteligencia artificial que permite realizar consultas a bases de datos **PostgreSQL** utilizando lenguaje natural. Gracias a la API de **Gemini** de Google, los usuarios pueden obtener respuestas precisas sin necesidad de conocer SQL.

## 📌 Características

✅ Conversión de lenguaje natural a SQL.  
✅ Integración con **PostgreSQL**.  
✅ Uso de **Gemini AI** para la interpretación de texto.  
✅ Fácil de configurar y desplegar.

## 🔧 Instalación y Configuración

### 1️⃣ Clona el repositorio

```bash
git clone https://github.com/leodelosrios/sql-ai.git
cd sql-ai
```

### 2️⃣ Instala dependencias

```bash
pip install -r requirements.txt
```

### 3️⃣ Configura la conexión a PostgreSQL

Crea un archivo `.env` con las API KEYs:

```plaintext
DB_API_KEY=TU_API_KEY
GEMINI_API_KEY=TU_API_KEY
```

### 4️⃣ Ejecuta la aplicación

```bash
python main.py
```

## 🚀 Uso

1. Inicia la aplicación.
2. Ingresa una consulta en lenguaje natural, por ejemplo:
   _"Muéstrame empleados que tengan más de 30 años"_
3. SQL-AI generará la consulta SQL y la ejecutará en PostgreSQL.
4. Verás los resultados en pantalla.

## 🛠 Tecnologías Utilizadas

- **Python** 🐍
- **PostgreSQL** 🐘
- **Gemini AI** 🤖

## 📄 Licencia

Todos los derechos reservados.

## 🌎 Contacto y Soporte

📩 **Autor:** [Leo de los Rios](https://github.com/leodelosrios)  
🐙 **Repositorio:** [GitHub](https://github.com/leodelosrios/sql-ai)  
🚀 **¡Dale una ⭐ al repo si te gusta este proyecto!**
