# Sistema de Votación - Backend API

Backend en Python con Flask y MySQL para un sistema de votación con 3 APIs principales.

## Requisitos

- Python 3.7+
- MySQL Server
- Paquetes: Flask, mysql-connector-python, flask-cors

## Instalación y Configuración

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configurar base de datos MySQL:**
   - Crear base de datos `votacion`
   - Ejecutar script de setup:
     ```bash
     python db_setup.py
     ```

3. **Configurar credenciales** en `app.py`:
   ```python
   db_config = {
       'host': 'localhost',
       'user': 'tu_usuario_mysql',
       'password': 'tu_password_mysql',
       'database': 'votacion'
   }
   ```

## Ejecutar

```bash
python app.py
```

Servidor en: `http://localhost:5000`

## 🟢 API 1: Registrar Voto (GET)

**Endpoint:** `GET /vote/{id}`  
**Función:** Registra un voto para el nominado especificado

### Input
- ID del nominado (01-15)

### Output
- Código error / OK con mensaje de confirmación

### Ejemplos
```bash
# Voto válido
curl http://localhost:5000/vote/01
# {"status": "OK", "code": 200, "message": "Voto registrado para nominado 01", "candidate_id": "01"}

# ID inválido (fuera de rango)
curl http://localhost:5000/vote/20
# {"status": "error", "code": 400, "message": "ID de nominado invalido"}

# ID no numérico
curl http://localhost:5000/vote/abc
# {"status": "error", "code": 400, "message": "ID debe ser numerico"}
```

## 🔴 API 2: Registrar Voto (POST JSON)

**Endpoint:** `POST /api/votes`  
**Función:** Registra un nuevo voto enviando datos JSON

### Input
```json
{
  "option": "02"
}
```

### Output
```json
{
  "message": "Voto registrado exitosamente",
  "option": "02"
}
```

### Ejemplo
```bash
curl -X POST http://localhost:5000/api/votes \
  -H "Content-Type: application/json" \
  -d '{"option": "02"}'
```

## 🔵 API 3: Obtener Resultados

**Endpoint:** `GET /votes`  
**Función:** Obtiene lista de votaciones por nominado

### Input
- Ninguno

### Output
```json
[
  {
    "nominado": "01",
    "votos": 5
  },
  {
    "nominado": "02",
    "votos": 3
  }
]
```

### Ejemplo
```bash
curl http://localhost:5000/votes
```

## Notas 

- **IDs válidos:** 01-15 (nominados disponibles)
- **CORS:** Habilitado para frontend
- **Modo debug:** Activado para desarrollo
- **Puerto:** 5000 (configurable en app.py)




