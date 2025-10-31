from config.database import engine
from sqlalchemy import text

def column_exists(table_name, column_name):
    """Cek apakah kolom sudah ada di tabel"""
    query = text("""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = :table_name AND column_name = :column_name
    """)
    with engine.connect() as conn:
        result = conn.execute(query, {"table_name": table_name, "column_name": column_name})
        return result.first() is not None


def add_column_if_not_exists(table_name, column_name, column_type, default=None):
    """Tambah kolom ke tabel jika belum ada"""
    if not column_exists(table_name, column_name):
        alter_query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}"
        if default is not None:
            alter_query += f" DEFAULT {default}"
        alter_query += ";"
        with engine.connect() as conn:
            conn.execute(text(alter_query))
            conn.commit()
        print(f"✅ Kolom '{column_name}' berhasil ditambahkan ke tabel '{table_name}'")
    else:
        print(f"✔️ Kolom '{column_name}' sudah ada di tabel '{table_name}'")


def sync_database():
    print("🔄 Sinkronisasi struktur database Railway dimulai...\n")

    # ================== TABLE MENUS ==================
    add_column_if_not_exists("menus", "description", "TEXT")

    # ================== TABLE ORDERS ==================
    add_column_if_not_exists("orders", "created_at", "TIMESTAMP", "NOW()")

    # ================== TABLE ORDER_ITEMS ==================
    add_column_if_not_exists("order_items", "price", "FLOAT", "0")
    add_column_if_not_exists("order_items", "subtotal", "FLOAT", "0")

    print("\n🎯 Sinkronisasi database selesai tanpa error!\n")


if __name__ == "__main__":
    sync_database()
