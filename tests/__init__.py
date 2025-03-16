"""
Test package initialization to ensure modules are importable.
"""
import sys
import os

# Add the project root directory to sys.path to allow module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
