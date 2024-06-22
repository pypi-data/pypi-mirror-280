from flask import Flask, request, jsonify
import logging
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import WebDriverException, TimeoutException
from urllib.parse import urlparse

app = Flask(__name__)

def is_valid_url(url):
    """
    Validate the URL format.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def scrape_static_content(url):
    """
    Scrape static content using requests and BeautifulSoup.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        return str(soup)
    except requests.RequestException as e:
        logging.error(f"Error fetching static content: {e}")
        return None

def is_dynamic_content(html_content):
    """
    Check for indicators of dynamic content in the HTML.
    """
    if "<script" in html_content or "application/json" in html_content or "window." in html_content:
        return True
    return False

def scrape_with_firefox(url):
    """
    Scrape dynamic content using Selenium and headless Firefox.
    """
    options = Options()
    options.headless = True
    geckodriver_path = '/usr/local/bin/geckodriver'
    service = Service(geckodriver_path)
    content = ""
    try:
        with webdriver.Firefox(service=service, options=options) as browser:
            browser.get(url)
            content = browser.page_source
    except (WebDriverException, TimeoutException) as e:
        logging.error(f"Error during dynamic web scraping: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    finally:
        return content

@app.route('/scrape', methods=['GET'])
def scrape():
    """
    Scrape the given URL.
    """
    url = request.args.get('url')
    if not url or not is_valid_url(url):
        return jsonify({'message': 'Invalid or missing URL'}), 400

    content = scrape_static_content(url)
    if not content or is_dynamic_content(content):
        content = scrape_with_firefox(url)

    if content:
        return jsonify({'content': content}), 200
    else:
        return jsonify({'message': 'Failed to scrape the content'}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
