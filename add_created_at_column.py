from sqlalchemy import create_engine, text

# ⚠️ Ganti dengan URL database PostgreSQL Railway kamu
DATABASE_URL = "postgresql://postgres:iqTFSbEWnJCvydSLiixmeVQfwErRQfhb@shuttle.proxy.rlwy.net:57568/railway"

engine = create_engine(DATABASE_URL)

def seed_menu():
    with engine.connect() as conn:
        conn.execute(text("""
            INSERT INTO menus (name, price, category, description, image_url) VALUES
            ('Nasi Goreng Spesial', 25000, 'makanan', 'Nasi goreng khas 3awan dengan topping ayam dan telur', 'https://i.imgur.com/3awan1.jpg'),
            ('Ayam Geprek', 20000, 'makanan', 'Ayam goreng crispy dengan sambal bawang pedas', 'https://i.imgur.com/3awan2.jpg'),
            ('Cappuccino', 18000, 'minuman', 'Kopi susu dengan aroma khas 3awan', 'https://i.imgur.com/3awan3.jpg'),
            ('Es Teh Manis', 8000, 'minuman', 'Es teh manis segar pelepas dahaga', 'https://i.imgur.com/3awan4.jpg');
        """))
        conn.commit()
        print("✅ Data contoh berhasil dimasukkan ke tabel menus!")

if __name__ == "__main__":
    seed_menu()
