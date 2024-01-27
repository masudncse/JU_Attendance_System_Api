from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (in-memory storage)
items = [
    {"id": 1, "name": "Item 1", "description": "Description 1"},
    {"id": 2, "name": "Item 2", "description": "Description 2"},
    {"id": 3, "name": "Item 3", "description": "Description 3"},
]


# CRUD Routes

# Read all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


# Read a specific item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"message": "Item not found"}), 404


# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = {
        "id": len(items) + 1,
        "name": data.get('name'),
        "description": data.get('description')
    }
    items.append(new_item)
    return jsonify(new_item), 201


# Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        data = request.get_json()
        item['name'] = data.get('name', item['name'])
        item['description'] = data.get('description', item['description'])
        return jsonify(item)
    else:
        return jsonify({"message": "Item not found"}), 404


# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
