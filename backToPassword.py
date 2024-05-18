import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.edge.options import Options as EdgeOptions




option = EdgeOptions()
option.add_argument("start-maximized")

driver = webdriver.Edge(options = option)
driver.get("https://myuserauth.accenture.com")

time.sleep(6)
os.system('cls')
timeout = 25
print("enter the EID to fix (without the @domain)\n")
userToFix = input()

try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/body/div/app-tapservices/mat-tab-group/mat-tab-header/div/div/div/div[3]')))
    tapButton = driver.find_element(By.XPATH, '/html/body/app-root/body/div/app-tapservices/mat-tab-group/mat-tab-header/div/div/div/div[3]')
    tapButton.click()
except TimeoutException:
    print("TAP SITE FAILED. RUN SCRIPT AGAIN")
    print("possible user account syntax error or web issue")


try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/body/div/app-tapservices/mat-tab-group/div/mat-tab-body[3]/div/app-temporary-access-pass/div/form/div[2]/mat-form-field/div[1]/div/div[2]/textarea')))
    eidField = driver.find_element(By.XPATH, '/html/body/app-root/body/div/app-tapservices/mat-tab-group/div/mat-tab-body[3]/div/app-temporary-access-pass/div/form/div[2]/mat-form-field/div[1]/div/div[2]/textarea')
    eidField.send_keys(userToFix)
except TimeoutException:
    print("TAP SITE FAILED. RUN SCRIPT AGAIN")
    print("possible user account syntax error or web issue")


try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/body/div/app-tapservices/mat-tab-group/div/mat-tab-body[3]/div/app-temporary-access-pass/div/form/div[4]/div[2]/div[1]/mat-radio-button')))
    fullLaptopButton = driver.find_element(By.XPATH, '/html/body/app-root/body/div/app-tapservices/mat-tab-group/div/mat-tab-body[3]/div/app-temporary-access-pass/div/form/div[4]/div[2]/div[1]/mat-radio-button')
    fullLaptopButton.click()
except TimeoutException:
    print("TAP SITE FAILED. RUN SCRIPT AGAIN")
    print("possible user account syntax error or web issue")



driver.execute_script("window.scrollTo(5,document.body.scrollHeight)")
time.sleep(1)


try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/body/div/app-tapservices/mat-tab-group/div/mat-tab-body[3]/div/app-temporary-access-pass/div/div/button')))
    createButton = driver.find_element(By.XPATH, '/html/body/app-root/body/div/app-tapservices/mat-tab-group/div/mat-tab-body[3]/div/app-temporary-access-pass/div/div/button')
    createButton.click()
except TimeoutException:
    print("TAP SITE FAILED. RUN SCRIPT AGAIN")
    print("possible user account syntax error or web issue")



try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-pop-up-modal/form/div/button[1]")))
    confirmButton = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-pop-up-modal/form/div/button[1]")
    confirmButton.click()
except TimeoutException:
    print("TAP SITE FAILED. RUN SCRIPT AGAIN")
    print("possible user account syntax error or web issue")
print("\ncreating TAP... ")

try:
    WebDriverWait(driver,timeout).until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/app-root/body/div/app-tapservices/mat-tab-group/div/mat-tab-body[3]/div/app-temporary-access-pass/div/div[2]/mat-form-field/div[1]/div/div[2]/textarea'), userToFix))
    resultInfo = driver.find_element(By.XPATH, "/html/body/app-root/body/div/app-tapservices/mat-tab-group/div/mat-tab-body[3]/div/app-temporary-access-pass/div/div[2]/mat-form-field/div[1]/div/div[2]/textarea")
    if resultInfo.text[len(userToFix)+ 2] != 'S':
        sys.exit("user dont found. make sure to enter the user EID correctly")
except TimeoutException:
    print("TAP FAILED. RUN SCRIPT AGAIN")


TAPItem = resultInfo.text
TAPSize = len(TAPItem)

invTap = ""
TAP = ""
i = 0

while  TAPItem[i]  != ' ':
    invTap += TAPItem[i]
    z = 0
    z = z + 1
    i = i - 1

i = 1
z = -1
lenTap = len(invTap)

while i < lenTap:
    TAP += invTap[z]
    i  = i + 1
    z = z - 1
print ("TAP created --> " + TAP)

option = EdgeOptions()
option.add_argument("start-maximized")
option.add_argument("inprivate")
driver = webdriver.Edge(options = option)
driver.get("https://mypasswordless.accenture.com")

try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]")))
    userField = driver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]")
except TimeoutException:
    print("PASSWORDLESS SITE FAILED. RUN SCRIPT AGAIN")

userField.send_keys(userToFix + "@accenture.com")


driver.execute_script("window.scrollTo(5,document.body.scrollHeight)")

try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input")))
    submitButton = driver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input")
    submitButton.click()
except  TimeoutException:
    print("PASSWORDLESS SITE FAILED. RUN SCRIPT AGAIN")
time.sleep(2)

try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[2]/input")))
    TAPField = driver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[2]/input")
    TAPField.send_keys(TAP)
except TimeoutException:
    print("PASSWORDLESS SITE FAILED. RUN SCRIPT AGAIN")

time.sleep(2)
try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div/div/div/div/input")))
    signInButton = driver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div/div/div/div/input")
except TimeoutException:
    print("PASSWORDLESS SITE FAILED. RUN SCRIPT AGAIN")

time.sleep(1)
signInButton.click()
os.system('cls')
print("setting back password config... ")
print("...")

try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-homepage/div[2]/div[2]/div[2]/div/div[3]/div[2]/button")))
    GPRButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-homepage/div[2]/div[2]/div[2]/div/div[3]/div[2]/button")
    GPRButton.click()
except TimeoutException:
    print("PASSWORDLESS SITE FAILED. RUN SCRIPT AGAIN")
time.sleep(1)
try:
    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-scril-go-passwordless/form/div[4]/input[2]")))
    print("USER IS ALREADY PASSWORD OK")
    sys.exit("bye")

except TimeoutException:
        print("Applying passwordless config...")
time.sleep(1)
try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-scril-reason/div[3]/div[2]/div[2]/mat-form-field/div[1]/div/div[2]/mat-select/div/div[1]")))
    reasonButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-scril-reason/div[3]/div[2]/div[2]/mat-form-field/div[1]/div/div[2]/mat-select/div/div[1]")
    reasonButton.click()                           
except TimeoutException:
    print("PASSWORDLESS SITE FAILED. RUN SCRIPT AGAIN")
    sys.exit("bye")


time.sleep(1)
try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[2]/div/div/mat-option[5]")))
    helloIssue = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/mat-option[5]")
    helloIssue.click()
except TimeoutException:
    print("PASSWORDLESS SITE FAILED. RUN SCRIPT AGAIN")

driver.execute_script("window.scrollTo(5,document.body.scrollHeight)")
time.sleep(1)

try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-scril-reason/div[3]/div[2]/div[3]/div[1]/mat-form-field/div[1]/div/div[2]/mat-select/div/div[1]")))
    pinIssue = driver.find_element(By.XPATH, "/html/body/app-root/div/app-scril-reason/div[3]/div[2]/div[3]/div[1]/mat-form-field/div[1]/div/div[2]/mat-select/div/div[1]")
    pinIssue.click()
except TimeoutException:
    print("PASSWORDLESS SITE FAILED. RUN SCRIPT AGAIN")


time.sleep(1)
pulsePin = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/mat-option[2]")
pulsePin.click()

driver.execute_script("window.scrollTo(5,document.body.scrollHeight)")
time.sleep(1)

try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-scril-reason/div[3]/div[2]/div[3]/div[1]/div/mat-form-field/div[1]/div/div[2]")))
    describeButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-scril-reason/div[3]/div[2]/div[3]/div[1]/div/mat-form-field/div[1]/div/div[2]")
    describeButton.click()
except TimeoutException:
    print("PASSWORDLESS SITE FAILED. RUN SCRIPT AGAIN")
time.sleep(1)
try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[2]/div/div/mat-option[3]")))
    otherButton = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/mat-option[3]")
    otherButton.click()
except TimeoutException:
    print("PASSWORDLESS SITE FAILED. RUN SCRIPT AGAIN")

driver.execute_script("window.scrollTo(5,document.body.scrollHeight)")
time.sleep(1)

try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-scril-reason/div[3]/div[2]/div[3]/div[1]/div/div/mat-form-field/div[1]/div/div[2]/textarea")))
    reasonText = driver.find_element(By.XPATH, "/html/body/app-root/div/app-scril-reason/div[3]/div[2]/div[3]/div[1]/div/div/mat-form-field/div[1]/div/div[2]/textarea")
    reasonText.send_keys (userToFix + " don't have PIN configured")
except TimeoutException:
    print("PASSWORDLESS SITE FAILED. RUN SCRIPT AGAIN")
time.sleep(1)
try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-scril-reason/div[3]/div[2]/div[3]/div[2]/button")))
    enableButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-scril-reason/div[3]/div[2]/div[3]/div[2]/button")
    enableButton.click()
except TimeoutException:
    print("PASSWORDLESS SITE FAILED. RUN SCRIPT AGAIN")

os.system('cls')
print("setting back password config... ")
time.sleep(15)
print("...")
print("waiting to " + userToFix + " password settings impact in domain")
time.sleep(30) #espera 1 minuto a que saque de passwordless e impacte en el dominio
print("...")
time.sleep(15)

option = EdgeOptions()
option.add_argument("start-maximized")
driver = webdriver.Edge(options = option)


driver.get("https://directory.accenture.com/ResetPassword/Home")

time.sleep(3)
os.system('cls')
print("setting one use password...")

try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/button")))
    cookiesButton = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/button")
    cookiesButton.click()
except TimeoutException:
    print("RESET PASSWORD SITE FAILED")
    print("the user is no longer passwordless. reset the password from another window")
time.sleep(2)

try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located(((By.XPATH, "/html/body/article/div[4]/div[1]/div/form/div/div[3]/div[2]/div[1]/div[2]/input"))))
    userArea = driver.find_element(By.XPATH, "/html/body/article/div[4]/div[1]/div/form/div/div[3]/div[2]/div[1]/div[2]/input")
    userArea.send_keys(userToFix)
except TimeoutException:
    print("RESET PASSWORD SITE FAILED")
    print("the user is no longer passwordless. reset the password from another window")

time.sleep(1)
try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/article/div[4]/div[1]/div/form/div/div[3]/div[2]/div[2]/div[2]/input[1]")))
    dirButton = driver.find_element(By.XPATH, "/html/body/article/div[4]/div[1]/div/form/div/div[3]/div[2]/div[2]/div[2]/input[1]")
    dirButton.click()
except TimeoutException:
    print("RESET PASSWORD SITE FAILED")
    print("the user is no longer passwordless. reset the password from another window")
time.sleep(1)


try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/article/div[4]/div[1]/div/form/div/div[4]/div/input[1]")))
    resetPaswdButton = driver.find_element(By.XPATH, "/html/body/article/div[4]/div[1]/div/form/div/div[4]/div/input[1]")
    resetPaswdButton.click()
except TimeoutException:
    print("the passwordless request don't impact in the domain yet")
    print("the user is no longer passwordless. reset the password from another window")

time.sleep(1)

try:
    driver.implicitly_wait(7)
    WebDriverWait(driver,timeout).until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/article/div[4]/div[1]/div/form/div/div[6]/div[2]/p"), "-"))
    pswdItem = driver.find_element(By.XPATH, "/html/body/article/div[4]/div[1]/div/form/div/div[6]/div[2]/p")
    os.system('cls')
    print(userToFix + " ************************\n")

    print("TAP -->  " + TAP)
    print("\nSINGLE USE PASSWORD: \n")

    print(pswdItem.text + "\n")
    print("****************************************")

except TimeoutException:
    print("RESET PASSWORD SITE FAILED")
    print("the user is no longer passwordless. reset the password from another window")

















