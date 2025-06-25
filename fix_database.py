import sqlite3
import os

def fix_database():
    # Path to your SQLite database
    db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
    
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if the image column already exists
        cursor.execute("PRAGMA table_info(menus_dailymenu)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'image' not in columns:
            # Add the image column to the menus_dailymenu table
            print("Adding 'image' column to menus_dailymenu table...")
            cursor.execute('''
                ALTER TABLE menus_dailymenu
                ADD COLUMN image VARCHAR(100) NULL;
            ''')
            conn.commit()
            print("Successfully added 'image' column.")
        else:
            print("'image' column already exists in menus_dailymenu table.")
            
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    fix_database()
