import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Load environment variables
load_dotenv()

# Get paths from .env
chromium_binary = os.getenv("CHROMIUM_BINARY")
driver_path = os.getenv("CHROMEDRIVER_PATH")

# Configure Selenium to use Chromium
options = webdriver.ChromeOptions()
options.binary_location = chromium_binary  # Use Chromium instead of Chrome

# Start Selenium with the correct driver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Test the browser
driver.get("https://www.google.com")
print("Chromium launched successfully!")

# Close the driver
driver.quit()
