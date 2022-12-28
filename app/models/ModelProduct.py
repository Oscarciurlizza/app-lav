from .entities.Product import Product


class ModelProduct():
    @classmethod
    def list_products(self, cursor):
        try:
            sql = """SELECT nombre, descripcion, precioventa FROM producto"""
            cursor.execute(sql)
            data = cursor.fetchall()
            products = []
            for row in data:
                product = Product(row[0], row[1], row[2])
                products.append(product)
            return products
        except Exception as ex:
            raise Exception(ex)
