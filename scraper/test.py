import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class JobScraper:
    def __init__(self):
        self.data = None

    def smartjob_az(self):
        print("Started scraping SmartJob.az")
        url = "https://smartjob.az/vacancies?page=5"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            job_listings = soup.find_all('div', class_='item-click')
            jobs = []
            for listing in job_listings:
                title = listing.find('div', class_='brows-job-position').h3.a.text.strip()
                company = listing.find('span', class_='company-title').a.text.strip()
                location = listing.find('span', class_='location-pin').text.strip()
                views = listing.find('span', class_='total-views').find('span', class_='number').text.strip()
                job_type = listing.find('span', class_='job-type').text.strip()
                posted_date = listing.find('div', class_='created-date').text.strip().replace('Yerləşdirilib ', '')
                salary = listing.find('div', class_='salary-val').text.strip()
                jobs.append({
                    'company': company,
                    'vacancy': title,
                    'location': location,
                    'views': views,
                    'job_type': job_type,
                    'posted_date': posted_date,
                    'salary': salary,
                    'apply_link': listing.find('div', class_='brows-job-position').h3.a['href']
                })
            df = pd.DataFrame(jobs)
            print("Scraping completed for SmartJob.az")
            return df
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)
            return pd.DataFrame()



    def get_data(self):
        smartjob_az_df = self.smartjob_az()
        scrape_date = datetime.now()
        smartjob_az_df['scrape_date'] = scrape_date
        self.data = pd.concat([
            smartjob_az_df
        ], ignore_index=True)
        return self.data



# Create an instance of the JobScraper
job_scraper = JobScraper()

# Get the data
data = job_scraper.get_data()

# Save the data to an Excel file
data.to_excel('job_listings.xlsx', index=False)
print("Data has been saved to job_listings.xlsx")