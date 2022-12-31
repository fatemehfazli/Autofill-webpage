# from selenium import webdriver
# # from selenium.webdriver.common.by import By
# By = webdriver.common.by.By
# import time

# web = webdriver.Chrome()
# web.get('https://docs.google.com/forms/d/e/1FAIpQLSek4lvyKCkjeKHJwRRSUdsNb4WCIohFNlog7YjeWVzmEr3DQQ/viewform')

# web.maximize_window()
# time.sleep(2)

# LastName = "Farahmand"
# last = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
# last.send_keys(LastName)

# time.sleep(2)
# FirstName = "Sarah"
# first = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
# first.send_keys(FirstName)
# time.sleep(2)

# RadioButtonPeriod = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
# RadioButtonPeriod.click()
# time.sleep(2)

# Submit = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
# Submit.click()
# time.sleep(2)






from selenium import webdriver
# from selenium.webdriver.common.by import By
By = webdriver.common.by.By
import time

web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSek4lvyKCkjeKHJwRRSUdsNb4WCIohFNlog7YjeWVzmEr3DQQ/viewform')

web.maximize_window()
time.sleep(2)


LastName = "Farahmand"
last = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
for char in LastName:
    last.send_keys(char)
    time.sleep(.5)
time.sleep(2)


FirstName = "Sarah"
first = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
for char in FirstName:
    first.send_keys(char)
    time.sleep(.5)
time.sleep(2)


RadioButtonPeriod = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
RadioButtonPeriod.click()
time.sleep(2)

Submit = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
Submit.click()
time.sleep(2)





# from selenium import webdriver
# # from selenium.webdriver.common.by import By
# By = webdriver.common.by.By
# import time

# web = webdriver.Chrome()
# web.get('https://realpython.com/account/signup/?intent=continue_reading&utm_source=rp&utm_medium=web&utm_campaign=rwn&utm_content=v1&next=%2Fflask-by-example-part-1-project-setup%2F')

# web.maximize_window()
# time.sleep(2)


# LastName = "fatq4a845856i@gmail.com"
# last = web.find_element(By.XPATH,'//*[@id="id_email"]')
# for char in LastName:
#     last.send_keys(char)
#     time.sleep(.5)
# time.sleep(2)


# FirstName = "@r123sA4scu4"
# first = web.find_element(By.XPATH,'//*[@id="id_password1"]')
# for char in FirstName:
#     first.send_keys(char)
#     time.sleep(.5)
# time.sleep(2)


# Submit = web.find_element(By.XPATH,'//*[@id="signup_form"]/div[4]/button')

# Submit.click()
# time.sleep(2)






