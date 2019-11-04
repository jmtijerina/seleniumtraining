from selenium import webdriver
#initialization of a new webdriver
driver = webdriver.Chrome()
driver.get('https://google.com')

#verify we are in the correct website
assert driver.title == 'Google'

#display page's title
page_title = driver.title
print("Title: " + page_title)

#close the browser
driver.quit()