# Contributed by github.com/Mik-27

import datetime
import json
import requests
import time
import logging
import os
from dotenv import load_dotenv
# The .env file contains DIST_ID(district id for the intended district) and
# BLOCK_NAME (name of the block to be checked).

browser_header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36'}

def get_state_id(state="Maharashtra"):
    """
        Getting the state id from the complete list of states for the specified state
    """
    states_url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
    res = requests.get(states_url, headers=browser_header)
    states = json.loads(res.text)

    for i in range(len(states['states'])):
        if states['states'][i]['state_name'] == state:
            return states['states'][i]['state_id']


def get_distrcit_id(state_id, district):
    """
        Getting the specifie district from the specified state through state_id
    """
    dist_url = f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state_id}"
    res = requests.get(dist_url, headers=browser_header)
    districts = json.loads(res.text)

    for i in range(len(districts['districts'])):
        if districts['districts'][i]['district_name'] == district:
            return districts['districts'][i]['district_id']


def find_by_district(dist_id, date, block):
    """
        Find the vaccination centres in a specific area and doses available using District ID and the Date.
    """
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={dist_id}&date={date}"
    res = requests.get(url, headers=browser_header)
    vac_centres = json.loads(res.text)

    # Storing centres od specific area/block in a differnt dictionary
    centres = {
        "sessions":[]
    }
    for i in range(len(vac_centres['sessions'])):
        if vac_centres['sessions'][i]['block_name'] == block:
            centres["sessions"].append(vac_centres['sessions'][i])

    return centres



load_dotenv()

# Config for logging messages
logging.basicConfig(level=logging.INFO, 
                    format="[%(asctime)s] - %(message)s", 
                    datefmt="%d-%m-%Y %H:%M:%S",
                    handlers=[
                        logging.FileHandler("vac.log"),
                        logging.StreamHandler()
                    ]
                )

today = datetime.datetime.now().strftime("%d-%m-%Y")

def check_dose_availability(centres, age_group, dose_no):
    """
        Check whether doses are available for specific age group, first or second dose, etc
        age_group - 18 or 45
        dose_no - 1 or 2 (strictly single digit)
    """
    now_time = datetime.datetime.now().time()
    if len(centres['sessions']) > 0:
        # print(centres['sessions'])
        for i in range(len(centres['sessions'])):
            logging.info("Centre: %s", centres['sessions'][i]["name"])
            # Check age group
            if centres['sessions'][i]['min_age_limit'] == age_group:
                # Check availability of doses for the specific dose
                if centres['sessions'][i][f'available_capacity_dose{dose_no}'] > 0:
                    logging.info("%s dose(s) available for %s+.\n ", centres['sessions'][i][f'available_capacity_dose{dose_no}'], age_group)
                else:
                    logging.info("Dose %s not available.\n", dose_no)
            else:
                logging.info("No centres available for age group %s.\n", age_group)
    else:
        logging.info("No vaccination centres available.\n")

# print(datetime.datetime.now().strftime("%d-%m-%Y"))
try:
    while True:
        check_dose_availability(find_by_district(os.environ.get("DIST_ID"), today, os.environ.get("BLOCK_NAME")), 45, 1)
        # Break the loop and end the program if time is 9 AM.
        if datetime.datetime.now().time().strftime("%H") == "09":
            break
        # Create a time interval of the specified time.
        time.sleep(5)
except KeyboardInterrupt:
    logging.error("Keyboard Interrupt.")
finally:
    logging.info("Logging Completed.")
