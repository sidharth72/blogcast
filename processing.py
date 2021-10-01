from blogger_api_fetch import get_api
from image_making import get_image, create_code_snippet
from instabot import Bot
from instagrapi import Client
from PIL import Image
import time
from dotenv import load_dotenv
import os

def Process():

	try:

		data = get_api()[0].get('title', None)

		with open('posted/posted.txt','r') as f:
			read_file = f.readlines()
		
		
		if data+"\n" in read_file:
			print("No updateds in blog..")

		elif data+"\n" not in read_file:
			get_image()
			create_code_snippet()
			with open('posted/posted.txt','a') as post_file:
				post_file.write(data+"\n")

				# PNG converted to JPG
			convert_to_jpg()

			#Posting on instagram.
			post_on_instagram()
			print("processing finished successfully.")

	except Exception as e:
		print("Processing Error! {}".format(e))
				

def convert_to_jpg():

	img = Image.open('carbon.png')
	rgb_im = img.convert('RGB')
	rgb_im.save('carbon.jpg')



def post_on_instagram():

	try:

		time.sleep(1)
		Username = os.environ.get('USER')
		Password = os.environ.get('PASSWORD')
		bot = Client()
		bot.login(Username, Password)
		bot.user_id_from_username(Username)
		bot.album_upload(paths=['intro.jpg','carbon.jpg'], caption='successfully')

	except Exception as e:
		print("Error occured! {}".format(e))

