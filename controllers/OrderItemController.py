from flask import jsonify, request
from config.database import SessionLocal
from models.order_item_model import OrderItem
from models.order_model import Order

def add_order_item():
    db = SessionLocal()
    try:
        data = request.get_json(force=True)
        order_id = data.get("order_id")
        menu_id = data.get("menu_id")
        quantity = int(data.get("quantity", 1))
        price = float(data.get("price", 0))
        subtotal = price * quantity

        if not order_id or not menu_id:
            return jsonify({"error": "order_id dan menu_id wajib diisi"}), 400

        new_item = OrderItem(
            order_id=order_id,
            menu_id=menu_id,
            quantity=quantity,
            price=price,
            subtotal=subtotal
        )
        db.add(new_item)

        order = db.query(Order).filter(Order.id == order_id).first()
        if order:
            order.total_price = (order.total_price or 0) + subtotal

        db.commit()
        return jsonify({"message": "Item pesanan ditambahkan", "subtotal": subtotal}), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()
