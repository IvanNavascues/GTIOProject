import pytest
from unittest.mock import patch, MagicMock
from app import app, get_db_connection


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


# -----------------------------
#  Test: ID válido
# -----------------------------
def test_vote_valid_id(client):
    with patch('app.get_db_connection') as mock_conn:
        mock_db = MagicMock()
        mock_conn.return_value = mock_db

        response = client.get('/vote/5')
        data = response.get_json()

        assert response.status_code == 200
        assert data['status'] == 'OK'
        assert data['candidate_id'] == '5'


# -----------------------------
#  Test: ID fuera de rango
# -----------------------------
def test_vote_invalid_range(client):
    response = client.get('/vote/20')
    data = response.get_json()

    assert response.status_code == 400
    assert data['status'] == 'error'
    assert data['message'] == 'ID de nominado invalido'


# -----------------------------
#  Test: ID no numérico
# -----------------------------
def test_vote_non_numeric(client):
    response = client.get('/vote/abc')
    data = response.get_json()

    assert response.status_code == 400
    assert data['status'] == 'error'
    assert data['message'] == 'ID debe ser numerico'


# -----------------------------
#  Test: Error de conexión a BD
# -----------------------------
def test_vote_db_connection_error(client):
    with patch('app.get_db_connection', return_value=None):
        response = client.get('/vote/3')
        data = response.get_json()

        assert response.status_code == 500
        assert data['status'] == 'error'
        assert data['message'] == 'Error de conexion a base de datos'


# -----------------------------
#  Test: Error SQL en UPDATE
# -----------------------------
def test_vote_sql_error(client):
    with patch('app.get_db_connection') as mock_conn:
        mock_db = MagicMock()
        mock_cursor = MagicMock()

        mock_conn.return_value = mock_db
        mock_db.cursor.return_value = mock_cursor

        # Simular error SQL REAL
        from mysql.connector import Error
        mock_cursor.execute.side_effect = Error("SQL error")

        response = client.get('/vote/4')
        data = response.get_json()

        assert response.status_code == 500
        assert data['status'] == 'error'
        assert "Error en base de datos" in data['message']

