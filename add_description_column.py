from config.database import engine
from sqlalchemy import text

def add_description_column():
    with engine.connect() as conn:
        conn.execute(text("ALTER TABLE menus ADD COLUMN IF NOT EXISTS description TEXT;"))
        conn.commit()
        print("✅ Kolom 'description' berhasil ditambahkan ke tabel menus!")

if __name__ == "__main__":
    add_description_column()
