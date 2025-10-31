from flask import jsonify, request
from config.database import SessionLocal
from models.order_model import Order
from models.order_item_model import OrderItem

def add_order():
    db = SessionLocal()
    try:
        data = request.get_json(force=True)
        customer_name = data.get("customer_name", "Guest")
        items = data.get("items", [])

        total_price = 0
        for it in items:
            qty = int(it.get("quantity", 1))
            subtotal = float(it.get("subtotal", 0))
            total_price += subtotal

        new_order = Order(customer_name=customer_name, total_price=total_price)
        db.add(new_order)
        db.commit()
        db.refresh(new_order)

        for it in items:
            db.add(OrderItem(
                order_id=new_order.id,
                menu_id=it.get("menu_id"),
                quantity=int(it.get("quantity", 1)),
                price=float(it.get("price", 0)),
                subtotal=float(it.get("subtotal", 0))
            ))

        db.commit()
        return jsonify({"message": "Order created", "order_id": new_order.id}), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()


def get_all_orders():
    db = SessionLocal()
    try:
        orders = db.query(Order).order_by(Order.id.desc()).all()
        return jsonify([
            {
                "id": o.id,
                "customer_name": o.customer_name,
                "total_price": o.total_price,
                "created_at": o.created_at
            }
            for o in orders
        ])
    finally:
        db.close()
