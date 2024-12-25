import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
import re

print("Collecting data from hackerrank.com...")
options = wd.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Edge(options=options)
driver.get("https://www.hackerrank.com/contests")
content = driver.page_source
soup = bs(content, 'html.parser')
driver.quit()

print("Parsing collected data")

skills = []
dates = []
for skill_name in soup.select(".hr-title-sm.contest-item__heading.ellipsis.title-ended"):
    if skill_name.text not in skills:
        skills.append(skill_name.text)

for end_date in soup.select(".hr-subtitle-sm.contest-item__time.ellipsis.contest-item__time-ended"):
    date = " ".join(re.findall("\\w+", end_date.text)[-3:])
    if re.match("\\d", date):
        dates.append(date)

df = pd.DataFrame({'Skills': skills, 'Topics': dates})
print('Data Collected:')
print(df)
print('\nData saved to results.csv.')