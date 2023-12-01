# Selenium Automation Script Documentation

## Introduction

This document details the Selenium automation script designed to interact with a web survey form hosted on [Qualtrics](https://www.qualtrics.com/). The script is built to automate the completion of the survey form using Python and the Selenium library. It simulates user interaction by filling in required fields with randomly generated or predefined data.

## Purpose

The purpose of this script is to automate the process of filling out a complex survey form. It uses a web browser to navigate through multiple pages of the survey, answer questions, and submit responses.

## Requirements

- **Python:** Version 3.6 or higher
- **Selenium:** Python library for browser automation
- **Chrome WebDriver:** ChromeDriver corresponding to the installed Chrome browser

## Usage

1. **Environment Setup:**

   - Ensure Python and Selenium are installed in the environment.
   - Download and install the appropriate Chrome WebDriver and specify its path in the script.

2. **Customization:**

   - Modify the list of Houston zip codes (`houston_zipcodes`) to match the required data pool.
   - Define the email (`email`) to be used for survey completion.
   - Adjust the age range (`ages`) and other demographic data lists as needed.

3. **Execution:**

   - Run the Python script in a compatible environment.

## Script Overview

The script navigates through multiple pages of the Qualtrics survey form, simulating user interactions. It utilizes Selenium's WebDriver to find and interact with specific HTML elements identified by XPATH or ID. The script handles scrolling, clicking, and data input to proceed through the survey.

## Workflow

1. **Initialization:**

   - Imports required libraries (Selenium, random).
   - Defines demographic data (zip codes, ages, household composition).
   - Initializes the Chrome WebDriver.

2. **Page Navigation:**

   - Uses WebDriver to open the survey form URL.
   - Clicks through the survey pages using `element_to_be_clickable` conditions.
   - Scrolls into view and clicks on specified questions sequentially.

3. **Data Input:**

   - Randomly selects and fills demographic fields (age, zip code, household composition).
   - Handles checkbox and radio button selections.

4. **Completion:**

   - Submits the final page of the survey with provided data.
   - Waits for elements and scrolls into view as necessary to ensure interaction.

5. **Error Handling:**

   - Uses `WebDriverWait` to handle waiting for elements before interaction.
   - Catches `StaleElementReferenceException` and `NoSuchElementException` to ensure stability.

## Limitations

- The script assumes the structure and IDs of survey elements remain unchanged. Any alterations to the survey form's HTML structure might cause the script to fail.
- It is designed for a specific Qualtrics survey; modifications might be necessary for use with different surveys.

## Conclusion

This Selenium automation script streamlines the process of completing the Qualtrics survey form. It provides a structured approach to interact with the form, input random or predefined data, and simulate user behavior.

## References

- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [Qualtrics](https://www.qualtrics.com/) - Official website

---
