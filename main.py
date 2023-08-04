import selenium as se
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from PIL import Image
# text recognition
import time
import cv2
import pytesseract
driver = webdriver.Chrome()
driver.get("https://student.srmap.edu.in/srmapstudentcorner/HRDSystem")
image=driver.find_elements(By.TAG_NAME,"img")
x=691
y=463
width=122
height=35
print(x,y,x+width,y+height)
driver.save_screenshot("screenshot.png")
im=Image.open("screenshot.png")
im=im.crop((int(x),int(y),int(x+width),int(y+height)))
im.save("captcha.png")
img=cv2.imread("captcha.png")
result=pytesseract.image_to_string(img)
print(result)
username="AP21110010091"
password="Saiguptha@2003"
input_username=driver.find_element(By.ID,"UserName")
input_password=driver.find_element(By.ID,"AuthKey")
input_captcha=driver.find_element(By.ID,"ccode")
input_username.send_keys(username)
input_password.send_keys(password)
input_captcha.send_keys(result)
time.sleep(1000)