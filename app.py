
from flask import Flask, render_template, request
import requests



app = Flask(__name__)



@app.route('/')
def Index():

	r = requests.get('http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=8f7334b8228f4767867ad0ad2b30f9cd')
	json_object = r.json()
	

	articles = json_object['articles']

	desc = []
	news = []
	img = []


	for i in range(len(articles)):
		myarticles = articles[i]


		news.append(myarticles['title'])
		desc.append(myarticles['description'])
		img.append(myarticles['urlToImage'])



	mylist = zip(news, desc, img)


	return render_template('index.html', context = mylist)







if __name__ == "__main__":
    app.run(debug=True)