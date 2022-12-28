from .entities.Customer import Customer

class ModelCustomer():
    @classmethod
    def list_customers(self, cursor):
        try:
            sql = """SELECT idcliente, dni, nombre FROM cliente"""
            cursor.execute(sql)
            data = cursor.fetchall()
            customers = []
            for row in data:
                customer = Customer(row[0], row[1], row[2])
                customers.append(customer)
            return customers
        except Exception as ex:
            raise Exception(ex)
