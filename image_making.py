from PIL import Image, ImageDraw, ImageFont
from fetch_code_snippets import get_code_snippet
from blogger_api_fetch import get_api
import textwrap
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyperclip as pyp
import time
from urllib.parse import quote_plus

width = 700
height = 700

#img  = Image.new( mode = "RGB", size = (width, height), color=(14,52,65) )

def get_image():

	try:
		print("Making image..")
		img_ = Image.open(fp='template.jpg', mode='r')
		img_draw = ImageDraw.Draw(img_)
		img_font = ImageFont.truetype('lemon-milk-font/LemonMilkBold-gx2B3.otf', 50)
		resp = get_api()[0].get('title', None)
		string = textwrap.fill(text=resp, width=13)
		img_draw.text((20, 40),string, fill=(225, 225, 225),font=img_font)
		img_.save('intro.jpg')
	except:
		print("Creating image failed")


# Change needed
def create_code_snippet():

	try:
		chrome_options = Options()
		#chrome_options.add_argument('--headless')
		with webdriver.Chrome(options=chrome_options) as driver:
			code = get_code_snippet()
			encoded_code = quote_plus(code)
			url = "https://carbon.now.sh?l=Python&code={code}/".format(code=encoded_code)
			driver.get(url)
			driver.find_element_by_id('export-menu').click()
			driver.find_element_by_id('export-png').click()
			time.sleep(5)

	except:

		return "Creating code snippet failed!"






