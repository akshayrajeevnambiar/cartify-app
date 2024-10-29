from src import create_app
from src.users.urls import users_bp

app = create_app()
app.register_blueprint(users_bp, url_prefix="/users")

if __name__ == "__main__":
    app.run()