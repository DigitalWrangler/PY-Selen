import os
from dotenv import load_dotenv

load_dotenv()
print("Chromedriver path:", os.getenv("CHROMEDRIVER_PATH"))
print("Chromium binary path:", os.getenv("CHROMIUM_BINARY"))
