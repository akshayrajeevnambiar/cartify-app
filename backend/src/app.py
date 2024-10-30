from src import create_app
from src.accounts.users.urls import users_bp
from src.accounts.products.urls import products_bp
from src.accounts.orders.urls import orders_bp


app = create_app()
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(products_bp, url_prefix="/products")
app.register_blueprint(orders_bp, url_prefix="/orders")


if __name__ == "__main__":
    app.run()