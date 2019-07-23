from django.shortcuts import render
import requests
import json

def home(request):
	url="https://newsapi.org/v2/top-headlines?country=in&apiKey=befa4351bdb544af94ab498b876a8920"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def world(request):
	url="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=befa4351bdb544af94ab498b876a8920"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def sports(request):
	url="https://newsapi.org/v2/top-headlines?category=sports&apiKey=befa4351bdb544af94ab498b876a8920&country=in"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def entertainment(request):
	url="https://newsapi.org/v2/top-headlines?category=entertainment&apiKey=befa4351bdb544af94ab498b876a8920&country=in"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def business(request):
	url="https://newsapi.org/v2/top-headlines?category=business&apiKey=befa4351bdb544af94ab498b876a8920&country=in"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def science(request):
	url="https://newsapi.org/v2/top-headlines?category=science&apiKey=befa4351bdb544af94ab498b876a8920&country=in"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def tech(request):
	url="https://newsapi.org/v2/top-headlines?category=technology&apiKey=befa4351bdb544af94ab498b876a8920&country=in"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def search(request):
	keyword=""
	if request.method=='POST':
		keyword=request.POST['keyword']
	url="https://newsapi.org/v2/everything?q="+keyword+"&apiKey=befa4351bdb544af94ab498b876a8920&language=en&sortBy=relevance"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api,'keyword':keyword})

def about(request):
	return render(request,'about.html',{})
