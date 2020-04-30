from selenium import webdriver
browser = webdriver.Chrome()

# Open website
browser.get("https://techstepacademy.com/trial-of-the-stones")
print("The trial of the stones has begun!")

# First trial passwords
browser.find_element_by_id("r1Input").send_keys("rock")
browser.find_element_by_id("r1Btn").click()
password1 = browser.find_element_by_css_selector("div#passwordBanner h4").text
print("First Password: " + password1)
browser.find_element_by_id("r2Input").send_keys(password1)
browser.find_element_by_id("r2Butn").click()
password2 = browser.find_element_by_css_selector("div#successBanner1 h4").text
print("Second Password: " + password2)

# Second trial the merchants

## Wealth of first merchant
jessicasWealth = browser.find_element_by_xpath("//b[text()='Jessica']/../../p").text

## Wealth of second merchant
bernardsWealth = browser.find_element_by_xpath("//b[text()='Bernard']/../../p").text

## Compare the wealth of the merchants
if jessicasWealth > bernardsWealth:
    richestMerchant = "Jessica"
    print("The richest merchant is Jessica with: " + jessicasWealth)
else:
    richestMerchant = "Bernard"
    print("The richest merchant is Bernard with: " + bernardsWealth)

## Set the richest merchant
browser.find_element_by_id("r3Input").send_keys(richestMerchant)
browser.find_element_by_id("r3Butn").click()
secretMessage = browser.find_element_by_css_selector("div#successBanner2 h4").text
print("Secret Message: " + secretMessage)

# Check Answares
browser.find_element_by_id("checkButn").click()
finalMessage = browser.find_element_by_css_selector("div#trialCompleteBanner h4").text
assert finalMessage == "Trial Complete" , "You have failed the trial"
print(finalMessage + "!")

#End Trial
browser.quit()