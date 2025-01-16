from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.python.org')

element_id = driver.find_element_by_id('submit')
print(element_id)

element_name = driver.find_element_by_id('submit')
print(element_name)

element_xpath = driver.find_element_by_xpath("/html/body/div/header/div/h1/a/img")
print(element_xpath)

element_class_name = driver.find_element_by_class_name('search-button')
print(element_class_name)

driver.close()
