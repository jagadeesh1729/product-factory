from flask import Flask, jsonify, request, abort
from service.models import Product
import logging
from service import status

app = Flask(__name__)
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    """Retrieve a single Product"""
    app.logger.info("Request to Retrieve product with ID [%s]", product_id)
    
    product = Product.find(product_id)
    if not product:
        abort(status.HTTP_404_NOT_FOUND, f"Product with ID '{product_id}' was not found.")
    
    return jsonify(product.serialize()), status.HTTP_200_OK



@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """Update a Product"""
    app.logger.info("Request to Update product with ID [%s]", product_id)

    if not request.is_json:
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, "Content-Type must be application/json")

    product = Product.find(product_id)
    if not product:
        abort(status.HTTP_404_NOT_FOUND, f"Product with ID '{product_id}' was not found.")

    data = request.get_json()
    app.logger.info("Received update data: %s", data)

    product.deserialize(data)
    product.update()

    return jsonify(product.serialize()), status.HTTP_200_OK


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """Delete a Product"""
    app.logger.info("Request to Delete product with ID [%s]", product_id)

    product = Product.find(product_id)
    if product:
        product.delete()

    return jsonify({"message": f"Product {product_id} deleted"}), status.HTTP_204_NO_CONTENT

@app.route("/products", methods=["GET"])
def list_products():
    """List all Products"""
    app.logger.info("Request to List all products")

    products = Product.all()
    return jsonify([product.serialize() for product in products]), status.HTTP_200_OK


@app.route("/products", methods=["GET"])
def find_product_by_name():
    """Find Products by Name"""
    name = request.args.get("name")
    if not name:
        return list_products()  # If no name is provided, return all products

    app.logger.info("Request to Find products by name [%s]", name)

    products = Product.find_by_name(name)
    return jsonify([product.serialize() for product in products]), status.HTTP_200_OK

@app.route("/products", methods=["GET"])
def find_product_by_category():
    """Find Products by Category"""
    category = request.args.get("category")
    if not category:
        return list_products()

    app.logger.info("Request to Find products by category [%s]", category)

    products = Product.find_by_category(category)
    return jsonify([product.serialize() for product in products]), status.HTTP_200_OK



@app.route("/products", methods=["GET"])
def find_product_by_availability():
    """Find Products by Availability"""
    available = request.args.get("available")
    if available is None:
        return list_products()

    available = available.lower() == "true"
    app.logger.info("Request to Find products by availability [%s]", available)

    products = Product.find_by_availability(available)
    return jsonify([product.serialize() for product in products]), status.HTTP_200_OK


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
