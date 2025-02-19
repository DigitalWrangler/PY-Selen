# pySELENIUM 🚀  

A Python project using **Selenium** with **Chromium** for web automation.  
This setup is pre-configured to download and run `chromedriver` using the `webdriver-manager` library.

## Features  
- **Selenium Automation**: Use Selenium WebDriver with Chromium for browser automation.  
- **Chromium Compatibility**: Set up to work with Chromium for lightweight browser automation.  
- **Driver Management**: Automatically download `chromedriver` using `webdriver-manager`.  
- **Environment Configuration**: Store paths like `chromedriver`, `chromium`, and URLs in `.env` for easy setup.  
- **Cookie Management**: Saves and reuses login cookies per website in `cookie-keychain/`.

---

## Setup  

### Prerequisites  
Ensure you have the following installed:  
- [Python 3.8+](https://www.python.org/downloads/)  
- [pip3](https://pip.pypa.io/en/stable/installation/)  
- Chromium installed on your system.

### Clone the Repository  
```sh
git clone https://github.com/DigitalWrangler/pySELENIUM.git
cd pySELENIUM

### Create a Virtual Environment

python3 -m venv .venv
source .venv/bin/activate  # On Linux/macOS
.venv/bin/activate.fish    # On Fish Shell

### Install Dependencies

pip3 install --upgrade pip
pip3 install selenium python-dotenv webdriver-manager


### Configuration

Create a `.env` File inside the project folder with these settings:

CHROMEDRIVER_PATH=/path/to/chromedriver  
CHROMIUM_BINARY=/path/to/chromium  
BASE_URL=https://example.com  # Target website URL  

Replace `/path/to/chromedriver` and `/path/to/chromium` with actual paths.

### Running the Script

Start `login.py`:

python3 login.py

On first use, enter credentials manually. Subsequent runs will use stored cookies.

### How It Works

1. Opens browser using Selenium.
2. Loads saved cookies for the website.
3. If no cookies exist, manual login is prompted.
4. Stores login session in `cookie-keychain/`.
5. Repeated visits use cached cookies.

---

## Customization

- Modify `BASE_URL` in `.env` to target a different site.
- Adjust script logic based on automation needs.
