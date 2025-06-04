import time
from selenium import webdriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expected_list= ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver= webdriver.Chrome(options=opts)
driver.implicitly_wait(5)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
time.sleep(2)

driver.find_element('xpath', '//input[@type="search"]').send_keys('ber')
time.sleep(2)

results = driver.find_elements('xpath', '//div[@class="products"]/div')
count = len(results)
assert count>0

for result in results:
    actualList.append(result.find_element('xpath', "h4").text)
    result.find_element('xpath', 'div/button').click()
    time.sleep(1)

print(actualList)

assert expected_list == actualList

driver.find_element('xpath', '//img[@alt="Cart"]').click()
time.sleep(2)

driver.find_element('xpath', '//button[text()="PROCEED TO CHECKOUT"]').click()
time.sleep(2)

# sum validaton
prices = driver.find_elements('css selector', 'tr td:nth-child(5) p')

sum=0
for price in prices:
    sum += int(price.text)
print(sum)

totalAmount = int(driver.find_element('xpath', '//span[@class="totAmt"]').text)

assert sum == totalAmount

driver.find_element('xpath', '//input[@class="promoCode"]').send_keys('rahulshettyacademy')
time.sleep(2)

driver.find_element('xpath', '//button[@class="promoBtn"]').click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located (('css selector', 'span[class="promoInfo"]')))
print(driver.find_element('css selector', 'span[class="promoInfo"]').text)

totalAfterDiscount = float(driver.find_element('xpath', '//span[@class="discountAmt"]').text)
print(totalAfterDiscount)

assert totalAfterDiscount<totalAmount
driver.close()