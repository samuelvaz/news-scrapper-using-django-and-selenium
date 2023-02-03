from selenium import webdriver
from time import sleep
import re
from selenium.webdriver.common.keys import Keys
import datetime, time, os

import smtplib

def get_headline():
    td = datetime.date.today()

    # creating a webdriver object for chrome
    wait_imp = 10
    CO = webdriver.ChromeOptions()
    CO.add_experimental_option('useAutomationExtension', False)
    CO.add_argument('--ignore-certificate-errors')
    CO.add_argument('--start-minimized')  # maximized
    wd = webdriver.Chrome(r'C:\Program Files (x86)\chromedriver.exe', options=CO)

    # Format for printing output
    print("Connecting to Authentic News source, Please wait .....\n")
    news_site = "https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"

    # print("Date:", td.strftime("%b-%d-%Y"))
    # print("--------------------------------------------------------------------------------------------")
    # print("       >>>>>>>>>>>>>>>>>>> INDIA's TOP 5 NEWS HEADLINES on CORONAVIRUS <<<<<<<<<<<<<<       ")
    # print("--------------------------------------------------------------------------------------------\n")

    wd.get(news_site)
    wd.implicitly_wait(wait_imp)
    cov_news = wd.find_elements_by_tag_name('h3')

    headlines = []

    # To get top 10 news headlines
    n_ind = 0
    for news in cov_news:
        headlines.append(news.text)
        print('>> ' + news.text, end='\n')
        n_ind += 1
        if n_ind > 10:  # Increase the number to get more top newsheadlines --> Replace 4 by any other value
            break
    print('\n')
    return headlines

class Coronavirus():
    def init(self):
        self.driver = webdriver.Chrome(r'C:\Program Files (x86)\chromedriver.exe')

    def get_data(self):
        # try:
        wait_imp = 10
        CO = webdriver.ChromeOptions()
        CO.add_experimental_option('useAutomationExtension', False)
        CO.add_argument('--ignore-certificate-errors')
        CO.add_argument('--start-minimized')  # maximized
        wd = webdriver.Chrome(r'C:\Program Files (x86)\chromedriver.exe', options=CO)
        site2 = "https://www.worldometers.info/coronavirus/country/india/"

        site4 = "https://www.grainmart.in/news/coronavirus-covd-19-live-cases-tracker-john-hopkins/"

        wd.get(site2)
        wd.implicitly_wait(wait_imp)
        c2 = wd.find_elements_by_class_name("maincounter-number")
        Total_2 = c2[0].text
        Death_2 = c2[1].text
        Recovered_2 = c2[2].text

        wd.get(site4)
        wd.implicitly_wait(wait_imp)



        t4 = wd.find_element_by_xpath("//div[@class='td-tc']")
        D4 = wd.find_element_by_xpath("//div[@class='td-td']")
        R4 = wd.find_element_by_xpath("//div[@class='td-tr']")
        Total_4=t4.text
        Death_4=D4.text
        Recovered_4=R4.text

        data = {
            'total_1': Total_2,
            'death_1': Death_2,
            'recovered_1': Recovered_2,
            'total_2': Total_4,
            'death_2': Death_4,
            'recovered_2': Recovered_4,

        }




        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('crce.8928.ce@gmail.com', 'duuvtcegizdbukds')

        subject = 'Coronavirus stats in your country today'

        body =  '\
        \nThere is new data on coronavirus:\
        \nData from worldometer:\
        \nTotal cases: ' + Total_2 + '\
        \nRecovered cases: ' + Recovered_2 + '\
        \nDeath: ' + Death_2 + '\
        \nData from Johns-Hopkins:\
        \nTotal cases: ' + Total_4 + '\
        \nRecovered cases: ' + Recovered_4 + '\
        \nDeath: ' + Death_4 + '\
        \nCheck the link: https://www.worldometers.info/coronavirus/,https://www.grainmart.in/news/coronavirus-covd-19-live-cases-tracker-john-hopkins/'


        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail('crce.8928.ce@gmail.com', 'crce.8961.ce@gmail.com', msg)

        print('Hey Email has been sent!')

        server.quit()
        return data




