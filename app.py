print("Importing create_app from app")
from app import create_app

print("Creating app instance")
app = create_app()

print("App instance created")

if __name__ == '__main__':
    print("Running app")
    app.run(debug=True, host='0.0.0.0')
