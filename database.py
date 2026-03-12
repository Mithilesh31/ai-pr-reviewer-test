def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return db.execute(query)

def get_product(product_id):
    sql = f"SELECT * FROM products WHERE id = {product_id}"
    return db.execute(sql)
