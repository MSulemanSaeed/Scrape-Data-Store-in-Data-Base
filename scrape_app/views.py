from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def home(request):
    return HttpResponse("Scrape Data Store Directly into the DataBase.")


def scrape_books(request):
    data = []
    base_url = "https://books.toscrape.com/"
    #we can enter pages that we want to scrape#
    for i in range(1):
        page = i + 1
        print("Scraping page:", page)
        
        url = f"{base_url}catalogue/page-{page}.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        products = soup.select("li > article.product_pod")

        for product in products:
            title = product.select_one('h3 > a').get('title')
            price = product.select_one('p.price_color').text
            image_relative_url = product.select_one('img').get('src')
            # Ensure the relative URL is correct
            image_url = base_url + image_relative_url.replace('../', '')

            # Save to database
            book = Book.objects.create(
                title=title,
                price=price,
                image=image_url
            )

            data.append({
                "title": title,
                "price": price,
                "image": image_url
            })

    return HttpResponse("Scraping and saving to the database was successful.")