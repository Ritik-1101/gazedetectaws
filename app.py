import os
import sys

print("Current working directory:", os.getcwd())
print("Python path:", sys.path)

from app import create_app

print("Import succeeded")

app = create_app()

print("App instance created")

if __name__ == '__main__':
    print("Running app")
    app.run(debug=True, host='0.0.0.0')
