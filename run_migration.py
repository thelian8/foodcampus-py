import os
import django

def apply_migration():
    # Set up Django environment
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodcampuspro.settings')
    django.setup()
    
    from django.db import connection
    
    # SQL to add the image column if it doesn't exist
    sql = """
    PRAGMA table_info(menus_dailymenu);
    """
    
    with connection.cursor() as cursor:
        # Check if the column exists
        cursor.execute("PRAGMA table_info(menus_dailymenu)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'image' not in columns:
            print("Adding 'image' column to menus_dailymenu table...")
            try:
                cursor.execute('''
                    ALTER TABLE menus_dailymenu
                    ADD COLUMN image VARCHAR(100) NULL;
                ''')
                print("Successfully added 'image' column.")
            except Exception as e:
                print(f"Error adding column: {e}")
        else:
            print("'image' column already exists in menus_dailymenu table.")

if __name__ == "__main__":
    apply_migration()
