from src import create_app
from src.accounts.users.urls import users_bp
from src.accounts.products.urls import products_bp

app = create_app()
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(products_bp, url_prefix="/products")


if __name__ == "__main__":
    app.run()