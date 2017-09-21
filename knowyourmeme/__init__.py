import requests
from datetime import datetime
from bs4 import BeautifulSoup

class kymSearch:
	def __init__(self,term:str):
		self.t1=datetime.now().second
		self.term=term
		for i in term:
			if i==" ":
				i="+"
		self.url = "http://knowyourmeme.com/search?q=" + self.term
		self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
		self.page = requests.get(self.url, headers=self.headers)
		self.soup = BeautifulSoup(self.page.content, 'html.parser')
		self.list1=self.soup.findAll("a", href=True)
		self.url2="http://knowyourmeme.com"+self.list1[129]['href']
		self.page2=requests.get(self.url2,headers=self.headers)
		self.soup2=BeautifulSoup(self.page2.content, 'html.parser')
		self.about = self.soup2.find('meta', attrs={"name":"description"})
		self.t2=datetime.now().second
		self.time=self.t2-self.t1
	def __repr__(self):
		return self.about['content']