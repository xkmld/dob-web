from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Configure Chrome options
options = Options()
print("HOLA");
options.headless = True  # Enable headless mode
options.add_argument("--window-size=1920,1200")  # Set the window size

print("HOLA");
DRIVER_PATH = 'utils/chromedriver'

print("HOLA");
# Initialize the Chrome driver with the specified options
service = Service(executable_path=r'./utils/chromedriver')
#driver = webdriver.Chrome(executable_path="./utils/chromedriver");

# Your code here to interact with the page
# ...
print("HOLA");
driver = webdriver.Chrome(service=service)

# It's a good practice to close the driver when you're finished
driver.quit()
