import os
import sys

def apply_migrations():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodcampuspro.settings')
    import django
    django.setup()
    
    from django.core.management import call_command
    
    print("Applying migrations...")
    call_command('migrate', 'menus', interactive=False)
    print("Migrations applied successfully!")

if __name__ == "__main__":
    apply_migrations()
