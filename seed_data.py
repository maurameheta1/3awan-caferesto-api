from config.database import SessionLocal
from models.menu_model import Menu

def seed():
    db = SessionLocal()
    sample = [
        {"name": "Nasi Goreng Spesial", "price": 25000, "category": "makanan", "image_url": "https://i.imgur.com/3awan1.jpg"},
        {"name": "Ayam Geprek", "price": 27000, "category": "makanan", "image_url": "https://i.imgur.com/3awan2.jpg"},
        {"name": "Cappuccino", "price": 18000, "category": "minuman", "image_url": "https://i.imgur.com/3awan3.jpg"},
        {"name": "Es Teh Manis", "price": 8000, "category": "minuman", "image_url": "https://i.imgur.com/3awan4.jpg"}
    ]
    for m in sample:
        db.add(Menu(**m))
    db.commit()
    db.close()
    print("✅ Data menu berhasil dimasukkan!")

if __name__ == "__main__":
    seed()
