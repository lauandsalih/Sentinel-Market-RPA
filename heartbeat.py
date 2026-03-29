import sys
import os

print(f"1. Python Version: {sys.version}")
print(f"2. Current Folder: {os.getcwd()}")
print("3. Attempting to import pandas...")
import pandas as pd
print("4. Pandas imported successfully!")
print("5. Attempting to import playwright...")
from playwright.async_api import async_playwright
print("6. Playwright imported successfully!")
print("--- ALL SYSTEMS GO ---")