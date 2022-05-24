from bs4 import BeautifulSoup
import requests
import csv
import time
import os



pages ={10, 20, 30, 40, 50}

with open('D:/Web Scrapping/data_scientist.csv' , 'a', encoding='utf-8', newline='') as f_output:
    csv_print = csv.writer(f_output)

    file_is_empty = os.stat('D:/Web Scrapping/data_scientist.csv').st_size == 0
    if file_is_empty:
        csv_print.writerow(['Job_Title', 'Company', 'Location', 'Salary' ])

for page in pages:
    source = requests.get('https://in.indeed.com/rc/clk?jk=bc6c094544c1da18&from=mobhp_jobfeed&tk=1ftprcp9hi934802'.formatt(page)).text
    soup = BeautifulSoup(source, 'lxml')
    for jobs in soup.find_all(class_='result'):


        try:
            title = jobs.h2.text.strip()
        except Exception as e:
            title = None
        print('Job title:' , title)

        try:
            company = jobs.span.text.strip()
        except Exception as e:
            title = None
        print('Company:' , company)

        try:
            location = jobs.find('span', class_='location').text.strip()
        except Exception as e:
            location = None
        print('Location:' , location)

        try:
            salary = jobs.find('span', class_='no-wrap').text.strip()
        except Exception as e:
            salary = None
        print('Salary:' , salary)



        csv_print.writerow([title, company, location, salary])


        print('.........................')

        time.sleep(0.5)

