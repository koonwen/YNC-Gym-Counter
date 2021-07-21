import app
from app import db

app = app.create_app({
    "ENV": 'development',
    "DEBUG": True,
    "TESTING": True
})

if __name__ == "__main__":
    app.run()