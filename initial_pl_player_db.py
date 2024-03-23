import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import re

import sqlite3

driver = webdriver.Firefox()

res = driver.get('https://fantasy.premierleague.com/api/bootstrap-static/')



