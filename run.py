import os
import app
from app import db
from werkzeug.security import generate_password_hash

os.environ["PI_USERNAME"] = 'pi'
os.environ["PI_PASSWORD"] = generate_password_hash("pi")

app = app.create_app({
    "ENV": 'development',
    "DEBUG": True,
    "TESTING": True
})

if __name__ == "__main__":
    app.run()