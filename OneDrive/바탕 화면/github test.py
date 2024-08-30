import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_news(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    news_data = []
    for article in articles:
        title = article.find('h2').get_text(strip=True)
        summary = article.find('p').get_text(strip=True)
        news_data.append({'Title': title, 'Summary': summary})

    return news_data

def save_to_csv(news_data, filename):
    df = pd.DataFrame(news_data)
    df.to_csv(filename, index=False)
    print(f"News data saved to {filename}")

# 예제 URL (실제 뉴스 웹사이트 URL로 변경하세요)
url = 'https://example-news-website.com/latest'
news_data = fetch_news(url)

if news_data:
    save_to_csv(news_data, 'latest_news.csv')
else:
    print("No news data found.")
