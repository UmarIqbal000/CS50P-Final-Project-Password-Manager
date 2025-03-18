from flask import Flask, request, jsonify, render_template
from database import init_db, store_password_db, get_password_db, get_all_passwords_db
from password_generator import generate_secure_password
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Initialize database
init_db()

# Add route for the main page
@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/store', methods=['POST'])
def store_password():
    """Store a new password entry"""
    try:
        data = request.get_json()
        website = data.get('website')
        username = data.get('username')
        password = data.get('password')
        
        if not all([website, username, password]):
            return jsonify({'error': 'Missing required fields'}), 400
            
        store_password_db(website, username, password)
        return jsonify({'message': 'Password stored successfully'})
        
    except sqlite3.Error as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/retrieve', methods=['GET'])
def retrieve_password():
    """Retrieve password for a website"""
    try:
        website = request.args.get('website')
        if not website:
            return jsonify({'error': 'Website parameter is required'}), 400
            
        password_entry = get_password_db(website)
        if password_entry:
            return jsonify(password_entry)
        return jsonify({'error': 'No password found for this website'}), 404
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/generate', methods=['GET'])
def generate_password():
    """Generate a secure random password"""
    try:
        length = int(request.args.get('length', 12))
        include_numbers = request.args.get('numbers', 'true').lower() == 'true'
        include_symbols = request.args.get('symbols', 'true').lower() == 'true'
        
        password = generate_secure_password(
            length=length,
            include_numbers=include_numbers,
            include_symbols=include_symbols
        )
        return jsonify({'password': password})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/passwords', methods=['GET'])
def get_all_passwords():
    """Get all stored passwords"""
    try:
        passwords = get_all_passwords_db()
        return jsonify(passwords)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 