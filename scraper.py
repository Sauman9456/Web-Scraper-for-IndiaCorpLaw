import json
import requests
from bs4 import BeautifulSoup
import re
import schedule
import time
from datetime import datetime

base_url = 'https://indiacorplaw.in/page/'

def job():
    data = []
    for page in range(1, 6):
        print(f'Scraping page {page}') 
        url = base_url + str(page)
        response = requests.get(url)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        articles = soup.find_all('article')
        
        for article in articles:
            title = article.h2.text
            content = article.find('div', class_='entry-content').text
            
            # Convert HTML tables to Markdown
            tables = article.find_all('table')
            for table in tables:
                table_md = '\n' + table.prettify()
                table_md = re.sub(r'<table[^>]*>', '| ', table_md) 
                table_md = re.sub(r'</table>', ' |', table_md)
                table_md = re.sub(r'<tr[^>]*>', '| ', table_md)
                table_md = re.sub(r'</tr>', ' |', table_md) 
                table_md = re.sub(r'<td[^>]*>', '| ', table_md)
                table_md = re.sub(r'</td>', ' |', table_md)
                table_md = re.sub(r'<th[^>]*>', '| ', table_md) 
                table_md = re.sub(r'</th>', ' |', table_md)
                content = content.replace(str(table), table_md)
            
            data.append({'title': title, 'content': content, 'timestamp': datetime.now().isoformat()})
            
    with open('scraped_data_schedule.json', 'w') as f:
        json.dump(data, f)
        
    print('Scraping complete!')

# Schedule the job every day at a specific time
schedule.every().day.at("16:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
