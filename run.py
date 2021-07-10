import app

app = app.create_app({
    "ENV": 'development',
    "DEBUG": True,
    "TESTING": True
})

if __name__ == "__main__":
    app.run()