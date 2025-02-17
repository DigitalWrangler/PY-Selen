# pySELENIUM

A Python project using **Selenium** with **Chromium** for web automation.  
This setup is pre-configured to download and run `chromedriver` using the `webdriver-manager` library.  

## Features
- **Selenium Automation**: Use Selenium WebDriver with Chromium for browser automation.
- **Chromium Compatibility**: Set up to work with Chromium for lightweight browser automation.
- **Driver Management**: Automatically download `chromedriver` using `webdriver-manager`.
- **Environment Configuration**: Store sensitive paths like `chromedriver` and `chromium` in `.env` for easy configuration.

## Setup

### Prerequisites
Make sure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- Chromium installed on your system.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pySELENIUM.git
    cd pySELENIUM
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate  # On Linux/macOS
    .venv/bin/activate.fish    # On Fish Shell (use this if you prefer Fish Shell)
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create the `.env` file in the root directory and add the following:
    ```dotenv
    CHROMEDRIVER_PATH=/path/to/your/driver
    CHROMIUM_BINARY=/path/to/your/chromium
    ```

    Replace `/path/to/your/driver` and `/path/to/your/chromium` with your actual paths.  
    For example:
    ```dotenv
    CHROMEDRIVER_PATH=/usr/bin/chromedriver
    CHROMIUM_BINARY=/usr/bin/chromium
    ```

5. Run the project:
    ```sh
    python your_selenium_script.py
    ```

---

## Usage Example

Here's a simple usage example to get you started with Selenium and Chromium:

```python
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

# Navigate to Google
driver.get("https://www.google.com")
print("Chromium launched successfully!")

# Close the driver
driver.quit()
