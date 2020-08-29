from selenium import webdriver

driver = webdriver.Chrome(r'C:\\Users\Dell\Desktop\chromedriver_win32\chromedriver.exe')
driver.get('https://www.amazon.com/b/?node=16225006011&pf_rd_r=MRR7XG1PX5YFGWBH3Q57&pf_rd_p=4a5ac24a-2f14-4296-8a03-0c034c0a7904')

items = driver.find_elements_by_xpath('//h2[@class ="a-size-base s-inline s-access-title a-text-normal"]')
prices = driver.find_elements_by_xpath('//span[@class = "a-size-base a-color-base"]')
print(len(items))

number1 = len(items)
number2 = len(prices)

with open("amazone.txt","w") as f:
    for i in range(1, number1):
         f.write(items[i].text + " is available in amazon for " + prices[i].text + "\n")

driver.close()



