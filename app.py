from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')

# Serve the homepage
@app.route('/docs/')
def home():
    return send_from_directory('static/html', 'index.html')

# Serve any file from the static directory
@app.route('/docs/<path:path>')
def static_files(path):
    return send_from_directory('static/html', path)

@app.route('/')
def index():
    return send_from_directory('static/landingpage', 'index.html')

@app.route('/about/')
def about():
    return send_from_directory('static/landingpage', 'about.html')

if __name__ == '__main__':
    app.run(debug=True)
