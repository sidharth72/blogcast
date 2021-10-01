import requests
from blogger_api_fetch import get_api
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options



def get_code_snippet():

	try:
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		driver = webdriver.Chrome(options= chrome_options)
		url = get_api()[0].get('url', None)
		driver.get(url)
		elem = driver.find_element_by_tag_name('pre')
		data = elem.get_attribute('innerText')
		print("Getting code snippet from the site....")

		return data

	except:

		return "Code snippet fetch failed!"




#url = get_api()[0]['url']

#page = requests.get(url)

#soup = BeautifulSoup(page.content, 'html.parser')

#code_snippets_pre = soup.find("pre").get_text(strip=True)

#print(code_snippets_pre)