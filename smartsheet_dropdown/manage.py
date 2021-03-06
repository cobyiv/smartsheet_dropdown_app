#!C:\Egnyte\Private\cobyvardy\Other_Projects\Python\Smartsheet_Dropdown\smartsheet_dropdown_env\Scripts\python.exe
"""Django's command-line utility for administrative tasks."""
import os
import sys

from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method

secret_key = os.environ.get('DJANGO_SECRET1')


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartsheet_dropdown.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
