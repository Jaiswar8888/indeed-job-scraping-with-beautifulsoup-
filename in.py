from turtle import title
from bs4 import BeautifulSoup as bs
import requests
import re 
import csv
import pandas as pd 

link="https://in.indeed.com/jobs?q=python%20fresher&l=Mumbai%2C%20Maharashtra&vjk=f0dcf4ed3daff2cb"
page=requests.get(link)
# print(page.content)
soup=bs(page.content,'html.parser')

titles=[]
job_title=soup.find_all('div',class_='heading4 color-text-primary singleLineTitle tapItem-gutter')
for job in job_title:
    titles.append(job.text)
print(titles)
print(len(titles))

comP=[]
company_name = soup.find_all('div',class_='heading6 company_location tapItem-gutter companyInfo')
for com in company_name:
    comP.append(com.text)
print(comP)
print(len(comP))

location=[]
location_name = soup.find_all('div',class_='companyLocation')
for loc in location_name:
    location.append(loc.text)
print(location)
print(len(location))

indeed = pd.DataFrame({
'Titles': titles,
'Company' : comP,
'location': location,

})


#add dataframe to csv file named 'movies.csv'
indeed.to_csv('indeed.csv')