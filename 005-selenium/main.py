import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd

website = "https://www.adamchoi.co.uk/overs/detailed"

driver = webdriver.Chrome()
driver.get(website)

all_matches_btn = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_btn.click()

dropdown = Select(driver.find_element(By.ID, 'country'))
dropdown.select_by_visible_text("Spain")

time.sleep(5)

matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:
    try:
        date_text = match.find_element(By.XPATH, "./td[1]").text
        home_team_text = match.find_element(By.XPATH, "./td[2]").text
        score_text = match.find_element(By.XPATH, "./td[3]").text
        away_team_text = match.find_element(By.XPATH, "./td[4]").text

        date.append(date_text)
        home_team.append(home_team_text)
        score.append(score_text)
        away_team.append(away_team_text)
    except Exception as e: # noqa
        continue

driver.quit()

df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_date.csv', index=False)
print(df)

