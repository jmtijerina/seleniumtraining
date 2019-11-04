from selenium import webdriver

driver = webdriver.Safari()
driver.get('https://python.org')
driver.execute_script('$(window.open(''))')
driver.switch_to.window(driver.window_handles[1])
driver.get('https://perl.org')
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.quit()