from selenium import webdriver
import time

web = webdriver.Chrome('D:/chromedriver.exe')


web.get('https://httpbin.org/basic-auth/user/pass')

time.sleep(2)


radioButtonElement = web.find_element_by_xpath('//*[@id="i5"]/div[3]/div')
radioButtonElement.click()

reason = "You are too ugly"

reasonElement = web.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')

reasonElement.send_keys(reason)


submitButtonElement = web.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
submitButtonElement.click()


getConfirmationDivText = web.find_element_by_css_selector(
    '.freebirdFormviewerViewResponseConfirmationMessage')
print(getConfirmationDivText.text)
