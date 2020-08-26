from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import os
import time

def open_contest():
	
	print("Enter Contest Url")
	url = input()
	
	print("Enter Problem Id")
	problem_id = input()
	
	url = (f"{url}/status/{problem_id}")
	print("Hacking Started")
	get_all_links(url)
	



def get_all_links(url):
	
	driver = webdriver.Firefox()
	driver.get(url)
	
	select_fr = Select(driver.find_element_by_id("programTypeForInvoker"))
	select_fr.select_by_index(5)
	
	driver.find_element_by_xpath("//input[@value ='Apply']").click()

	allLinks = driver.find_elements_by_tag_name("a")
	allLinks = set(allLinks)

	sol_list = []
	
	for link in allLinks:
		try:
			if "submission" in link.get_attribute("href"):
				sol_list.append(link.get_attribute("href"))
		except:
			continue
		
	# driver.close()
	sol_list.reverse()
	for url in sol_list:
		print(f"Scraping Solution From Id {url[-10 : ]}")
		scrape_solution(url, driver)
	
	driver.close()




def scrape_solution(url, driver):

	# driver = webdriver.Firefox()
	driver.get(url)

	solution = driver.find_element_by_id("program-source-text")

	f = open("auto_test.cpp", 'w')
	f.write(solution.text)
	f.close()

	print(f"Solution Scraped Successfully")
	print(f"Starting Test")
	
	run_test()
	
	os.remove("auto_test.cpp")

	# driver.close()




def run_test():
	os.system('g++ auto_test.cpp')
	os.system('bash s.sh')
	print(f"Test Completed")




def main():
	print("##::::'##::::'###::::::######:::##::::##::::'##::::'##::::'###:::::'######::'##::::'##:'####:'##::: ##:'########:")
	print("##:::: ##:::'## ##:::'##... ##: ##::'##::::: ###::'###:::'## ##:::'##... ##: ##:::: ##:. ##:: ###:: ##: ##.....::")
	print("##:::: ##::'##:. ##:: ##:::..:: ##:'##:::::: ####'####::'##:. ##:: ##:::..:: ##:::: ##:: ##:: ####: ##: ##:::::::")
	print("#########:'##:::. ##: ##::::::: #####::::::: ## ### ##:'##:::. ##: ##::::::: #########:: ##:: ## ## ##: ######:::")
	print("##.... ##: #########: ##::::::: ##. ##:::::: ##. #: ##: #########: ##::::::: ##.... ##:: ##:: ##. ####: ##...::::")
	print("##:::: ##: ##.... ##: ##::: ##: ##:. ##::::: ##:.:: ##: ##.... ##: ##::: ##: ##:::: ##:: ##:: ##:. ###: ##:::::::")
	print("##:::: ##: ##:::: ##:. ######:: ##::. ##:::: ##:::: ##: ##:::: ##:. ######:: ##:::: ##:'####: ##::. ##: ########:")
	print("..:::::..::..:::::..:::......:::..::::..:::::..:::::..::..:::::..:::......:::..:::::..::....::..::::..::........::")
	for i in range(5):
		print(" ")
	open_contest()
    

if __name__ == "__main__":
    main()

#  https://codeforces.com/contest/1401
