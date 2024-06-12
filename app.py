print("Importing create_app from app")
from project.main import create_app

print("Creating app instance")
app = create_app()

print("App instance created")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
