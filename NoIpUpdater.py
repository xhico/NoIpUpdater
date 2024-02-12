# -*- coding: utf-8 -*-
# !/usr/bin/python3

import logging
import os
import traceback

from Misc import get911, sendEmail
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def main():
    # Goto Page
    logger.info("Goto Login Page")
    browser.get("https://www.noip.com/login")

    # Input credentials
    logger.info("Input credentials")
    browser.find_element(By.ID, "username").send_keys(NOIP_USERNAME)
    browser.find_element(By.ID, "password").send_keys(NOIP_PASSWORD)
    browser.find_element(By.ID, "clogs-captcha-button").click()

    # Get actionBtn
    logger.info("Goto DynDNS Page")
    browser.get("https://my.noip.com/dynamic-dns")
    logger.info("Get actionBtn")
    table = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
    actionBtn = table.find_element(By.TAG_NAME, "tbody").find_element(By.TAG_NAME, "tr").find_elements(By.TAG_NAME, "td")[-1].find_element(By.TAG_NAME, "button")
    logger.info(f"actionBtn text - {actionBtn.text}")

    # If actionBtn is "Confirm"
    if actionBtn.text == "Confirm":
        actionBtn.click()
        logger.info("actionBtn CLICK")
        sendEmail(os.path.basename(__file__), "NoIp Updated")
    else:
        logger.info("actionBtn NOT Confirm")


if __name__ == "__main__":
    # Set Logging
    LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.abspath(__file__).replace(".py", ".log"))
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()])
    logger = logging.getLogger()

    logger.info("----------------------------------------------------")

    # Get NOIP Credentials
    NOIP_USERNAME = get911("NOIP_USERNAME")
    NOIP_PASSWORD = get911("NOIP_PASSWORD")

    # Create Selenium
    logger.info("Launch Browser")
    options = Options()
    options.add_argument('-headless')
    service = Service("/home/pi/geckodriver", log_output="/home/pi/geckodriver.log")
    browser = webdriver.Firefox(service=service, options=options)

    try:
        main()
    except Exception as ex:
        logger.error(traceback.format_exc())
        sendEmail(os.path.basename(__file__), str(traceback.format_exc()))
    finally:
        browser.close()
        logger.info("Close")
        logger.info("End")
