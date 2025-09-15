# check_metadata.py
import sys, os
from importlib import import_module

# Ajusta la ruta al package 'backend'
sys.path.append(os.path.join(os.path.dirname(__file__), "backend"))

from backend.app.db.base import Base

print("Base metadata tables BEFORE importing models:", list(Base.metadata.tables.keys()))

# Intenta importar el modelo explícitamente
try:
    import_module("backend.app.models.users.userModel")
    print("Imported userModel OK")
except Exception as e:
    print("Error importing userModel:", e)

print("Base metadata tables AFTER importing userModel:", list(Base.metadata.tables.keys()))
