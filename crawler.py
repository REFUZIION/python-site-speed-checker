import requests
from bs4 import BeautifulSoup
import time

def evaluate_website_speed(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()

    response_time = end_time - start_time

    soup = BeautifulSoup(response.content, 'html.parser')

    page_title = soup.title.string
    page_size = len(response.content)
    page_load_time = response.elapsed.total_seconds()

    print("Website evaluation results:")
    print("Page title:", page_title)
    print("Page size (in bytes):", page_size)
    print("Page load time (in seconds):", page_load_time)
    print("Response time (in seconds):", response_time)

    if page_size > 1000000:
        print("Tip: Consider reducing the size of the page by compressing images and optimizing code.")
    elif page_load_time > 5:
        print("Tip: Consider optimizing the code and reducing the number of requests to improve page load time.")
    else:
        print("Tip: Good job! Your website is fast and efficient.")

url = input("Enter the website URL: ")

evaluate_website_speed(url)
