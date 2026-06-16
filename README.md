# 📚 CuentaCuentos – AI Story Generator

<div align="center">

<img width="200" src="https://cdn-icons-png.flaticon.com/512/3771/3771518.png" />

### Plataforma de generación inteligente de relatos con IA 🚀

<p align="center">
  <b>CuentaCuentos</b> es un pipeline de inteligencia artificial que genera, valida y selecciona relatos breves automáticamente, creando también una imagen representativa basada en el texto final.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-IA-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/OpenAI-Text%20Generation-black?style=for-the-badge">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/AI-Pipeline-green?style=for-the-badge">
</p>

<p align="center">
  <a href="#-flujo-de-trabajo">Flujo</a> •
  <a href="#-tecnologías-sugeridas">Tecnologías</a> •
  <a href="#-estructura">Estructura</a> •
  <a href="#-cómo-funciona">Ejecución</a>
</p>

</div>

---

# 🌌 Acerca de CuentaCuentos

**CuentaCuentos** es un sistema automatizado de generación de historias mediante inteligencia artificial.

El sistema recibe parámetros como tema, nombre y longitud del relato, y ejecuta un pipeline completo que:

- Genera múltiples versiones del mismo relato
- Valida coherencia, formato y calidad
- Selecciona la mejor historia
- Genera una imagen representativa
- Exporta el resultado final

---

# 🧩 Flujo de trabajo

## 🔄 Pipeline de generación

- 📥 Recepción de datos (JSON de entrada)
- 🧹 Procesamiento y validación de parámetros
- ✍️ Creación de prompt optimizado
- 🤖 Generación de 5 relatos con IA
- ✅ Validación de formato
- 🧠 Evaluación de coherencia
- 🏆 Selección del mejor relato
- 🎨 Generación de imagen ilustrativa
- 📦 Exportación final del resultado

---

# 🛠️ Tecnologías utilizadas

<p align="center">
  <img src="https://skillicons.dev/icons?i=python" />
</p>

- Python 3.10+
- OpenAI API / Transformers
- Pydantic (validación de datos)
- Pillow / Stable Diffusion (generación de imágenes)
- Pytest (testing)
- JSON / YAML (manejo de datos)
- Streamlit (interfaz opcional)

---

# 📂 Estructura del proyecto

```bash
PlataformaWebRelatos/
│
├── src/
│   ├── main.py
│   ├── prompt_generator.py
│   ├── text_validator.py
│   ├── image_generator.py
│   └── utils/
│       └── data_processing.py
│
├── tests/
│   ├── test_prompt_generator.py
│   ├── test_text_validator.py
│
├── assets/
│   └── diagrams/
│       └── workflow.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚡ Cómo ejecutar el proyecto

## 1️⃣ Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate
# Windows: venv\Scripts\activate
```

## 2️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

## 3️⃣ Ejecutar la aplicación
```bash
streamlit run src/main.py
```

---

# 🧠 ¿Qué hace este proyecto?

- 🧩 Pipeline modular de IA
- ✍️ Generación de texto inteligente
- 🔍 Validación automática de calidad
- 🎨 Generación de imágenes
- ⚙️ Arquitectura escalable
- 🧪 Preparado para testing

---

# 📈 Estructura lógica del sistema

El sistema sigue este flujo:

```
Input → Processing → Prompt → Generation → Validation → Selection → Image → Export
```

---

# 🚀 Objetivo del proyecto

Crear un sistema capaz de:

- Automatizar la escritura creativa
- Evaluar calidad de contenido con IA
- Generar experiencias visuales
- Simular un pipeline de producción real de contenido

---

# 🤝 Contribuciones

Las contribuciones son bienvenidas ❤️

1. Fork del repositorio
2. Crear rama
```bash
git checkout -b feature/nueva-funcion
```
3. Commit de cambios
```bash
git commit -m "✨ mejora en pipeline"
```
4. Pull Request 🚀

---

# 👨‍💻 Autor

<div align="center">

<img width="120" src="https://github.com/isairey.png" style="border-radius:50%" />

## Isai Reyes — AI & Full Stack Developer
 
</div>

---

# 🌟 Proyecto de IA Creativa

Sistema diseñado para explorar el potencial de la inteligencia artificial en la generación automática de contenido narrativo y visual.
