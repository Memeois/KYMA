import requests
from datetime import datetime
from bs4 import BeautifulSoup

class kymSearch:
	def __init__(self,term:str): #term is word to be searched
		self.t1=datetime.now().second #set time on start
		self.term=term
		for i in term: #change every space to +
			if i==" ":
				i="+"
		self.url = "http://knowyourmeme.com/search?q=" + self.term #making a url to be used
		self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} #defining headers for browser
		self.page = requests.get(self.url, headers=self.headers) #requesting code
		self.soup = BeautifulSoup(self.page.content, 'html.parser') #parsing code with Beautiful Soup
		self.list1=self.soup.findAll("a", href=True) #Finding all links of search
		self.url2="http://knowyourmeme.com"+self.list1[129]['href'] #Picking first result and using its href
		self.page2=requests.get(self.url2,headers=self.headers) #requesting page again
		self.soup2=BeautifulSoup(self.page2.content, 'html.parser') #parsing it
		self.about = self.soup2.find('meta', attrs={"name":"description"}) #finding description
		self.imageurl = self.soup2.find('meta', attrs={"property":"og:image"})['content'] #finding image url
		self.t2=datetime.now().second #getting time on finish
		self.time=self.t2-self.t1 #time it took to do all this
	def __repr__(self):
		return self.about['content'] #This is used for you to be able to print object and get definition print(nameofobject)