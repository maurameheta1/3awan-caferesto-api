from flask import jsonify, request
from config.database import SessionLocal
from models.menu_model import Menu

def get_all_menus():
    db = SessionLocal()
    try:
        search = request.args.get("search")
        category = request.args.get("category")

        query = db.query(Menu)
        if search:
            query = query.filter(Menu.name.ilike(f"%{search}%"))
        if category:
            query = query.filter(Menu.category.ilike(f"%{category}%"))

        menus = query.all()
        return jsonify([
            {
                "id": m.id,
                "name": m.name,
                "price": m.price,
                "category": m.category,
                "description": m.description, 
                "image_url": m.image_url
            }
            for m in menus
        ])
    finally:
        db.close()


def get_menu(id):
    db = SessionLocal()
    try:
        m = db.query(Menu).get(id)
        if not m:
            return jsonify({"message": "Menu not found"}), 404
        return jsonify({
            "id": m.id,
            "name": m.name,
            "price": m.price,
            "category": m.category,
            "description": m.description,
            "image_url": m.image_url
        })
    finally:
        db.close()


def add_menu():
    db = SessionLocal()
    try:
        data = request.get_json(force=True)
        new_menu = Menu(
            name=data.get("name"),
            price=data.get("price"),
            category=data.get("category"),
            image_url=data.get("image_url")
        )
        db.add(new_menu)
        db.commit()
        db.refresh(new_menu)
        return jsonify({"message": "Menu added", "id": new_menu.id}), 201
    finally:
        db.close()


def update_menu(id):
    db = SessionLocal()
    try:
        menu = db.query(Menu).get(id)
        if not menu:
            return jsonify({"message": "Menu not found"}), 404
        data = request.get_json(force=True)
        menu.name = data.get("name", menu.name)
        menu.price = data.get("price", menu.price)
        menu.category = data.get("category", menu.category)
        menu.description = data.get("description", menu.description)
        menu.image_url = data.get("image_url", menu.image_url)
        db.commit()
        db.refresh(menu)
        return jsonify({"message": "Menu updated", "id": menu.id})
    finally:
        db.close()


def delete_menu(id):
    db = SessionLocal()
    try:
        menu = db.query(Menu).get(id)
        if not menu:
            return jsonify({"message": "Menu not found"}), 404
        db.delete(menu)
        db.commit()
        return jsonify({"message": "Menu deleted"})
    finally:
        db.close()
