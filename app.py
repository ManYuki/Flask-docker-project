from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_docker():
    return "Hello, Docker! The container is running successfully."

if __name__ == '__main__':
    # host='0.0.0.0' is crucial for Docker to expose the app outside the container
    app.run(debug=True, host='0.0.0.0', port=5000)
