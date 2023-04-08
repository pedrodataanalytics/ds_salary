import glassdoor_scraper as gs
import pandas as pd


path = '/Users/pedromonteiro/Documents/ds_salary/chromedriver'

df = gs.get_jobs('data_scientist', 15, False, path, 15)