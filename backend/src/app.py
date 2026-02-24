from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)
CORS(app, origins="*") 

NO_CONN_ERROR = "No se puede conectar a la base de datos"

def get_db_connection():
    """Obtiene una conexión a la base de datos"""
    try:
        return mysql.connector.connect(
            host="mysql-db",
            user="user",
            password="password",
            database="votacion")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario o contraseña no validos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("No existe la BD")
        else:
            print(err)


@app.route('/vote/<id>', methods=['GET'])
def validate_candidate(id):
    """Registra voto para el ID del nominado
    
    INPUT: Id nominado (01-15)
    OUTPUT: Codigo error / OK
    """
    # Validar que sea un ID valido (01-15)
    try:
        id_int = int(id)
        if id_int < 1 or id_int > 15:
            return jsonify({
                'status': 'error',
                'code': 400,
                'message': 'ID de nominado invalido'
            }), 400
    except (ValueError, TypeError):
        return jsonify({
            'status': 'error',
            'code': 400,
            'message': 'ID debe ser numerico'
        }), 400

    # Registrar el voto
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({
                'status': 'error',
                'code': 500,
                'message': 'Error de conexion a base de datos'
            }), 500
        
        cursor = conn.cursor()
        cursor.execute("UPDATE votes SET votes = votes+1 WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({
            'status': 'OK',
            'code': 200,
            'message': f'Voto registrado para nominado {id}',
            'candidate_id': id
        }), 200
        
    except mysql.connector.Error as err:
        return jsonify({
            'status': 'error',
            'code': 500,
            'message': f'Error en base de datos: {str(err)}'
        }), 500

# ==================== API REST ====================

@app.route('/api/votes', methods=['POST'])
def create_vote():
    """Registra un nuevo voto"""
    data = request.get_json()
    
    if not data or 'option' not in data:
        return jsonify({'error': 'Campo "option" es requerido'}), 400
    
    voto = data['option']
    
    # Validar que sea un ID valido (01-15)
    try:
        voto_int = int(voto)
        if voto_int < 1 or voto_int > 15:
            return jsonify({'error': 'Opcion invalida. Solo se aceptan 1-15'}), 400
    except (ValueError, TypeError):
        return jsonify({'error': 'Opcion debe ser numerica'}), 400

    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': NO_CONN_ERROR}), 500
            
        cursor = conn.cursor()
        cursor.execute("INSERT INTO votes (name) VALUES (%s)", (voto,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Voto registrado exitosamente', 'option': voto}), 201
    except mysql.connector.Error as err:
        return jsonify({'error': f'Error en la base de datos: {str(err)}'}), 500

@app.route('/votes', methods=['GET'])
def get_votes():
    """Obtiene la lista de votaciones por nominado"""
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': NO_CONN_ERROR}), 500
            
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT name, votes 
            FROM votes 
            GROUP BY name 
            ORDER BY name
        """)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # Formatear respuesta como lista de objetos
        votes_list = []
        for row in results:
            votes_list.append({
                'nominado': str(row['name']),
                'votos': row['votes']
            })
        
        return jsonify(votes_list), 200
    except mysql.connector.Error as err:
        return jsonify({'error': f'Error en la base de datos: {str(err)}'}), 500

@app.route('/api/votes/<int:option>', methods=['GET'])
def get_vote_by_option(option):
    """Obtiene el conteo para una opcion especifica"""
    try:
        id_int = int(option)
        if id_int < 1 or id_int > 15:
            return jsonify({'error': 'Opcion invalida'}), 400
    except (ValueError, TypeError):
        return jsonify({'error': 'Debe ser numerico'}), 400
        
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': NO_CONN_ERROR}), 500
            
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT COUNT(*) as count FROM votes WHERE name = %s", (option,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        
        return jsonify({
            'option': option,
            'count': result['count'] if result else 0
        }), 200
    except mysql.connector.Error as err:
        return jsonify({'error': f'Error en la base de datos: {str(err)}'}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Verifica el estado de la API y conexion a BD"""
    try:
        conn = get_db_connection()
        if conn:
            conn.close()
            return jsonify({'status': 'healthy', 'database': 'connected'}), 200
        else:
            return jsonify({'status': 'unhealthy', 'database': 'disconnected'}), 503
    except:
        return jsonify({'status': 'unhealthy', 'database': 'error'}), 503

# ==================== RUTAS GENERALES ====================

@app.route('/', methods=['GET'])
def index():
    """3 APIs principales"""
    return jsonify({
        'name': 'Votacion API',
        'version': '1.0',
        'apis': {
            'GET /vote/{id}': 'Registrar voto para nominado (codigo error/OK)',
            'POST /api/votes': 'Registrar voto con JSON',
            'GET /votes': 'Obtener lista de votaciones por nominado'
        }
    }), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint no encontrado'}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': 'Método no permitido'}), 405

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)