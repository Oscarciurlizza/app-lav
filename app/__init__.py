from flask import Flask, render_template
from config import cursor

from .models.ModelCustomer import ModelCustomer
from .models.ModelProduct import ModelProduct


app = Flask(__name__)


@app.route("/")
def home():
    try:
        customers = ModelCustomer.list_customers(cursor)
        data = {
            "title": "Customers",
            "customers": customers
        }
        return render_template("list_customers.html", data=data)
    except Exception as ex:
        raise Exception(ex)


@app.route("/products")
def list_products():
    try:
        products = ModelProduct.list_products(cursor)
        data = {
            "title": "Products",
            "products": products
        }
        return render_template("list_products.html", data=data)

    except Exception as ex:
        raise Exception(ex)


def init_app(config):
    app.config.from_object(config)
    return app
