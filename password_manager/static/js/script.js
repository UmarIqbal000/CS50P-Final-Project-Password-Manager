document.addEventListener('DOMContentLoaded', function() {
    // Store password form submission
    document.getElementById('storeForm').addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const data = {
            website: document.getElementById('website').value,
            username: document.getElementById('username').value,
            password: document.getElementById('password').value
        };
        
        try {
            const response = await fetch('/api/store', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            
            const result = await response.json();
            
            if (response.ok) {
                showMessage('Password stored successfully!', 'success');
                this.reset();
            } else {
                showMessage(result.error, 'error');
            }
        } catch (error) {
            showMessage('Failed to store password', 'error');
        }
    });
    
    // Generate password
    document.getElementById('generateBtn').addEventListener('click', async function() {
        const length = document.getElementById('passwordLength').value;
        const includeNumbers = document.getElementById('includeNumbers').checked;
        const includeSymbols = document.getElementById('includeSymbols').checked;
        
        try {
            const response = await fetch(
                `/api/generate?length=${length}&numbers=${includeNumbers}&symbols=${includeSymbols}`
            );
            const data = await response.json();
            
            if (response.ok) {
                document.getElementById('generatedPassword').value = data.password;
            } else {
                showMessage(data.error, 'error');
            }
        } catch (error) {
            showMessage('Failed to generate password', 'error');
        }
    });
    
    // Search password
    document.getElementById('searchBtn').addEventListener('click', async function() {
        const website = document.getElementById('searchWebsite').value;
        
        try {
            const response = await fetch(`/api/retrieve?website=${encodeURIComponent(website)}`);
            const data = await response.json();
            
            const resultsDiv = document.getElementById('searchResults');
            
            if (response.ok) {
                resultsDiv.innerHTML = `
                    <div class="password-entry">
                        <p><strong>Website:</strong> ${data.website}</p>
                        <p><strong>Username:</strong> ${data.username}</p>
                        <p>
                            <strong>Password:</strong> 
                            <span class="password-text">********</span>
                            <button onclick="togglePassword(this)">Show</button>
                            <button onclick="copyToClipboard('${data.password}')">Copy</button>
                        </p>
                    </div>
                `;
            } else {
                resultsDiv.innerHTML = `<p class="error-message">${data.error}</p>`;
            }
        } catch (error) {
            showMessage('Failed to retrieve password', 'error');
        }
    });
    
    // Copy generated password
    document.getElementById('copyGenerated').addEventListener('click', function() {
        const password = document.getElementById('generatedPassword').value;
        copyToClipboard(password);
    });
    
    // Use generated password
    document.getElementById('useGenerated').addEventListener('click', function() {
        const password = document.getElementById('generatedPassword').value;
        document.getElementById('password').value = password;
    });
});

// Utility functions
function showMessage(message, type) {
    const messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    messageDiv.className = `${type}-message`;
    
    const form = document.getElementById('storeForm');
    form.appendChild(messageDiv);
    
    setTimeout(() => messageDiv.remove(), 3000);
}

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(
        () => showMessage('Copied to clipboard!', 'success'),
        () => showMessage('Failed to copy', 'error')
    );
}

function togglePassword(button) {
    const passwordSpan = button.parentElement.querySelector('.password-text');
    const isHidden = passwordSpan.textContent === '********';
    
    if (isHidden) {
        const passwordEntry = button.closest('.password-entry');
        const website = passwordEntry.querySelector('p:first-child').textContent.split(': ')[1];
        
        fetch(`/api/retrieve?website=${encodeURIComponent(website)}`)
            .then(response => response.json())
            .then(data => {
                passwordSpan.textContent = data.password;
                button.textContent = 'Hide';
            })
            .catch(() => showMessage('Failed to reveal password', 'error'));
    } else {
        passwordSpan.textContent = '********';
        button.textContent = 'Show';
    }
} 