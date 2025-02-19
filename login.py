import os
import pickle
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Load environment variables
load_dotenv()

# Get paths and URL
chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
BASE_URL = os.getenv("BASE_URL")  # URL from .env
cookie_dir = "cookie-keychain"  # Directory to store cookies

# Ensure directories exist
os.makedirs(cookie_dir, exist_ok=True)

# Validate environment variables
if not chromedriver_path:
    raise ValueError("CHROMEDRIVER_PATH is not set in the .env file")
if not BASE_URL:
    raise ValueError("BASE_URL is not set in the .env file")

# Generate a unique cookie file for the URL
cookie_filename = os.path.join(cookie_dir, BASE_URL.replace("https://", "").replace("/", "_") + ".pkl")

# Configure Chrome options
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection as a bot

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

# Open the URL
driver.get(BASE_URL)

# Try loading cookies if they exist
if os.path.exists(cookie_filename):
    with open(cookie_filename, "rb") as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
    print(f"Loaded cookies from {cookie_filename}")
    driver.refresh()  # Refresh after adding cookies

# Ask user to log in manually if needed
print("Please log in manually if necessary. Press ENTER after logging in.")
input("Press ENTER to continue when logged in.")

# Wait for login to complete
time.sleep(5)

# Save new cookies
cookies = driver.get_cookies()
with open(cookie_filename, "wb") as f:
    pickle.dump(cookies, f)
print(f"Cookies saved to {cookie_filename}")

# Keep the browser open until user decides to close it
input("Press ENTER to close the browser when you're done.")
driver.quit()
