import sqlite3
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db():
    """Initialize the SQLite database"""
    try:
        conn = sqlite3.connect('passwords.db')
        cursor = conn.cursor()
        
        # Create passwords table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                website TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        logger.info("Database initialized successfully")
        
    except sqlite3.Error as e:
        logger.error(f"Database initialization error: {e}")
        raise
    finally:
        conn.close()

def store_password_db(website: str, username: str, password: str) -> None:
    """Store a password entry in the database"""
    try:
        conn = sqlite3.connect('passwords.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO passwords (website, username, password)
            VALUES (?, ?, ?)
        ''', (website, username, password))
        
        conn.commit()
        logger.info(f"Password stored for website: {website}")
        
    except sqlite3.Error as e:
        logger.error(f"Error storing password: {e}")
        raise
    finally:
        conn.close()

def get_password_db(website: str) -> Optional[Dict]:
    """Retrieve password entry for a website"""
    try:
        conn = sqlite3.connect('passwords.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT website, username, password
            FROM passwords
            WHERE website = ?
        ''', (website,))
        
        result = cursor.fetchone()
        if result:
            return {
                'website': result[0],
                'username': result[1],
                'password': result[2]
            }
        return None
        
    except sqlite3.Error as e:
        logger.error(f"Error retrieving password: {e}")
        raise
    finally:
        conn.close()

def get_all_passwords_db() -> List[Dict]:
    """Retrieve all password entries"""
    try:
        conn = sqlite3.connect('passwords.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT website, username, password
            FROM passwords
            ORDER BY created_at DESC
        ''')
        
        results = cursor.fetchall()
        return [{
            'website': row[0],
            'username': row[1],
            'password': row[2]
        } for row in results]
        
    except sqlite3.Error as e:
        logger.error(f"Error retrieving passwords: {e}")
        raise
    finally:
        conn.close() 