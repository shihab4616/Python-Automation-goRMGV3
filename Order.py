# Importing necessary libraries
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from fpdf import FPDF
import time
from datetime import datetime

# Path to chrome driver executable file
CHROME_DRIVER_PATH = "D:\Shihab Ahmed\Automation with Python\Driver\chromedriver-win64\chromedriver.exe"

# URL of the login page
LOGIN_PAGE_URL = "https://gormg-v3-staging.skylarksoft.net/"

# Valid USER_ID and PASSWORD
USER_ID = "shihab@skylarksoft.com"
PASSWORD = "shihab"

# INVALID USER_ID and PASSWORD
INVALID_USER_ID = "abd@skylarksoft.com"
INVALID_PASSWORD = "123456789"

# Initialize Chrome driver
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

# Function to simulate typing with delay
def type_with_delay(element, text, delay=0.1):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

# Initialize test results list
test_results = []

# Function to log test results
def log_test_result(test_name, status, details=""):
    result = {
        "test_name": test_name,
        "status": "Passed" if status else "Failed",
        "details": details,
    }
    test_results.append(result)

# Perform tests
try:
    driver.get(LOGIN_PAGE_URL)
    
    # Test 1: Login without credentials
    login_button = driver.find_element(By.XPATH, '//*[@id="login"]')
    login_button.click()
    time.sleep(2)
    if "login" in driver.current_url:
        log_test_result("Test 1: Login without credentials", True, "Login failed as expected.")
    else:
        log_test_result("Test 1: Login without credentials", False, "Login succeeded unexpectedly.")
    
    # Test 2: Login with invalid credentials
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    email_field.clear()
    password_field.clear()
    type_with_delay(email_field, INVALID_USER_ID)
    type_with_delay(password_field, INVALID_PASSWORD)
    login_button = driver.find_element(By.XPATH, '//*[@id="login"]')
    login_button.click()
    time.sleep(2)
    if "login" in driver.current_url:
        log_test_result("Test 2: Login with invalid credentials", True, "Login failed as expected.")
    else:
        log_test_result("Test 2: Login with invalid credentials", False, "Login succeeded unexpectedly.")

    # Test 3: Login with valid credentials
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    email_field.clear()
    password_field.clear()
    type_with_delay(email_field, USER_ID)
    type_with_delay(password_field, PASSWORD)
    login_button = driver.find_element(By.XPATH, '//*[@id="login"]')
    login_button.click()
    time.sleep(3)
    if "login" not in driver.current_url:
        log_test_result("Test 3: Login with valid credentials", True, "Login succeeded as expected.")
    else:
        log_test_result("Test 3: Login with valid credentials", False, "Login failed unexpectedly.")
    
    # Test 4: Click sidebar button
    sidebar_button = driver.find_element(By.XPATH, '//*[@id="menuScroll"]/ul/li[3]/a/span[3]')
    sidebar_button.click()
    time.sleep(3)
    log_test_result("Test 4: Click sidebar button", True, "Sidebar button clicked successfully.")
    
    # Test 5: Navigate to order entry page
    order_page_url = "https://gormg-v3-staging.skylarksoft.net/merchandising/orders/create"
    driver.get(order_page_url)
    time.sleep(5)
    if "orders/create" in driver.current_url:
        log_test_result("Test 5: Navigate to order entry page", True, "Order entry page loaded successfully.")
    else:
        log_test_result("Test 5: Navigate to order entry page", False, "Failed to load order entry page.")
    
    # Select dropdown and select an item from the unit dropdown
    try:
        # Clicking in the dropdown box  
        dropdown = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "select2-unit-container"))
        )
        dropdown.click()
        time.sleep(2)  

        # Searching in the searchbar for the desired item
        search_bar = WebDriverWait(driver, 10).until(
               EC.presence_of_element_located((By.XPATH, "/html/body/span/span/span[1]/input"))
        )
        search_text = "ABC Unit"
        search_bar.clear()  
        for char in search_text:
            search_bar.send_keys(char) 
            time.sleep(0.2)  

        time.sleep(3) 

        # Select the desired item in the filtered dropdown
        option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//li[contains(text(),'{search_text}')]"))
        )
        time.sleep(2)  
        option.click()  
        time.sleep(2) 

        log_test_result("Test 6: Select unit dropdown with search", True, "Search bar and selection worked successfully.")
    except Exception as e:
        log_test_result("Test 6: Select unit dropdown with search", False, str(e))
       
    # Select dropdown and select an item from the data source dropdown
    try:
        # Clicking in the dropdown box
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "select2-data_source-container"))
        )
        dropdown.click()
        time.sleep(2)
        
        # Selecting desired item from the dropdown
        option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[text()='Repeat Order']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(option).click().perform()
        time.sleep(3)
        
        log_test_result("Test 7: Select data source dropdown items", True, "Dropdown and selection worked successfully.")
    except Exception as e:
        log_test_result("Test 7: Select data source dropdown items", False, str(e))

    # Select dropdown and select an Style  from the Style  dropdown
    try:
        # Clicking in the dropdown box
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "select2-style_name-container"))
        )
        dropdown.click()
        time.sleep(2)

        # Selecting desired Style  from the dropdown
        option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[text()='Auora-895']"))
            
        
        )
        actions = ActionChains(driver)
        actions.move_to_element(option).click().perform()
        time.sleep(3)
        
        log_test_result("Test 8: Select data source dropdown items", True, "Dropdown and selection worked successfully.")
    except Exception as e:
        log_test_result("Test 8: Select data source dropdown items", False, str(e))

    
     # Click Populate previous data 

    try: 
        #Clicking Populate data 
        PopulateData = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(By.XPATH, "//*[@id='view']/div[1]/div/section/div/div[2]/div[1]/ul/li/div/div/div[5]/div/button")
        )
        PopulateData.click()
        time.sleep(2)
        

        log_test_result("Test 8: Select data source dropdown items", True, "Dropdown and selection worked successfully.")
    except Exception as e:
        log_test_result("Test 8: Select data source dropdown items", False, str(e))
 


    # Select dropdown and select  ID  from the Sample Requisition ID dropdown
    try:
        # Clicking in the dropdown box
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "select2-sample_requisition_id-container"))
        )
        dropdown.click()
        time.sleep(2)

        # Selecting desired ID  from the dropdown
        option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[text()='PN-SRE-24-000020']"))
            
        
        )
        actions = ActionChains(driver)
        actions.move_to_element(option).click().perform()
        time.sleep(3)
        
        log_test_result("Test 8: Select data source dropdown items", True, "Dropdown and selection worked successfully.")
    except Exception as e:
        log_test_result("Test 8: Select data source dropdown items", False, str(e))




         # Select dropdown and select  Category  from the Garments Category dropdown
    try:
        # Clicking in the dropdown box
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "select2-garments_category_id-container"))
        )
        dropdown.click()
        time.sleep(2)

        # Selecting desired Category tatus from the dropdown
        option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[text()='POLO1']"))
            
        
        )
        actions = ActionChains(driver)
        actions.move_to_element(option).click().perform()
        time.sleep(3)
        
        log_test_result("Test 8: Select data source dropdown items", True, "Dropdown and selection worked successfully.")
    except Exception as e:
        log_test_result("Test 8: Select data source dropdown items", False, str(e))




finally:
    # Close the browser window and quit the driver
    driver.quit()

# PDF Generation
class PDF(FPDF):
    # pdf header text 
    def header(self):
        self.set_font("Arial", size=12, style="B")
        self.cell(0, 10, "Automated Test Results Report", ln=True, align="C")
        self.ln(10)
    # Page numbering
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", size=10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")
    # Test results 
    def add_test_result(self, test_name, status, details):
        self.set_font("Arial", size=12)
        self.cell(0, 10, f"Test: {test_name}", ln=True)
        self.set_font("Arial", size=10)
        self.cell(0, 10, f"Status: {status}", ln=True)
        self.multi_cell(0, 10, f"Details: {details}")
        self.ln(5)


# Function to generate PDF report from test results list
def generate_pdf(pdf_file_path, test_results):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    for result in test_results:
        pdf.add_test_result(result["test_name"], result["status"], result["details"])

    pdf.output(pdf_file_path)

# Saving the PDF report
pdf_file_path = "D:\\Shihab Ahmed\\Automation with Python\\goRMG_Order\\Test_Reports.pdf"
generate_pdf(pdf_file_path, test_results)
print(f"\nPDF report saved to {pdf_file_path}")

