import requests
from apiclient.discovery import build


def get_api():

	try:

		Key = "AIzaSyD4rnaUKr3pDMmw_gTK83RuGSZyM96-It4"
		BlogId = "2457144399977145673"
		blog = build('blogger', 'v3', developerKey=Key)
		resp = blog.blogs().get(blogId=BlogId).execute()
		blog_name = resp.get('name', None)
		posts = blog.posts().list(blogId=BlogId).execute()
		items_ = posts['items']

		return items_

	except:
		return "API fetch failed!"
	
	