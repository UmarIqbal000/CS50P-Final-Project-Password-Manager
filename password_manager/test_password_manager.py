import pytest
import sqlite3
from database import init_db, store_password_db, get_password_db
from password_generator import generate_secure_password

@pytest.fixture
def setup_database():
    """Setup test database"""
    init_db()
    yield
    # Cleanup database after tests
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM passwords')
    conn.commit()
    conn.close()

def test_store_and_retrieve_password(setup_database):
    """Test storing and retrieving a password"""
    website = "test.com"
    username = "testuser"
    password = "testpass123"
    
    # Store password
    store_password_db(website, username, password)
    
    # Retrieve password
    result = get_password_db(website)
    
    assert result is not None
    assert result['website'] == website
    assert result['username'] == username
    assert result['password'] == password

def test_generate_password():
    """Test password generator"""
    # Test default parameters
    password = generate_secure_password()
    assert len(password) == 12
    assert any(c.isdigit() for c in password)
    assert any(c in '!@#$%^&*()' for c in password)
    
    # Test custom length
    password = generate_secure_password(length=16)
    assert len(password) == 16
    
    # Test without numbers
    password = generate_secure_password(include_numbers=False)
    assert not any(c.isdigit() for c in password)
    
    # Test without symbols
    password = generate_secure_password(include_symbols=False)
    assert not any(c in '!@#$%^&*()' for c in password)

def test_invalid_password_length():
    """Test password generator with invalid length"""
    with pytest.raises(ValueError):
        generate_secure_password(length=5)

def test_retrieve_nonexistent_password(setup_database):
    """Test retrieving a non-existent password"""
    result = get_password_db("nonexistent.com")
    assert result is None 