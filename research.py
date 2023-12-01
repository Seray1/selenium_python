from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
from selenium.common.exceptions import StaleElementReferenceException

# Creating a list of Houston zip codes
houston_zipcodes = [
    "77001",
    "77002",
    "77003",
    "77004",
    "77005",
    "77006",
    "77007",
    "77008",
    "77009",
    "77010",
    "77011",
    "77012",
    "77013",
    "77014",
    "77015",
    "77016",
    "77017",
    "77018",
    "77019",
    "77020",
    "77021",
    "77022",
    "77023",
    "77024",
    "77025",
    "77026",
    "77027",
    "77028",
    "77029",
    "77030",
    "77031",
    "77032",
    "77033",
    "77034",
    "77035",
]

random_zipcode = random.choice(houston_zipcodes)
email = "rayribjam907@tapi.re"

# Creating a list of ages from 35 to 60
ages = list(range(35, 61))
random_age = random.choice(ages)
people_in_household = list(range(3, 10))
random_people_in_household = random.choice(people_in_household)
children_in_household = list(range(1, 2))
random_children_in_household = random.choice(children_in_household)


driver = webdriver.Chrome()
driver.get("https://uthtmc.az1.qualtrics.com/jfe/form/SV_3VOxNqOqRsvmsIK")

wait = WebDriverWait(driver, 30)

# Click the first "Next" button to go to the second page
first_arrow_button = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#Buttons[role="navigation"] input#NextButton')
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", first_arrow_button)
driver.execute_script("arguments[0].click();", first_arrow_button)

# Now, wait for the Next button on the second page and click it
next_button_second_page = wait.until(EC.element_to_be_clickable((By.ID, "NextButton")))

driver.execute_script("arguments[0].scrollIntoView(true);", next_button_second_page)
driver.execute_script("arguments[0].click();", next_button_second_page)

first_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID32-6-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", first_question)
driver.execute_script("arguments[0].click();", first_question)

second_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID85-5-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", second_question)
driver.execute_script("arguments[0].click();", second_question)


next_button_third_page = wait.until(EC.element_to_be_clickable((By.ID, "NextButton")))

driver.execute_script("arguments[0].scrollIntoView(true);", next_button_third_page)
driver.execute_script("arguments[0].click();", next_button_third_page)


third_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID84-5-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", third_question)
driver.execute_script("arguments[0].click();", third_question)

fourth_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID1-3-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", fourth_question)
driver.execute_script("arguments[0].click();", fourth_question)


fifth_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID11-4-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", fifth_question)
driver.execute_script("arguments[0].click();", fifth_question)

six_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID86-2-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", six_question)
driver.execute_script("arguments[0].click();", six_question)

seven_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID87-2-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", seven_question)
driver.execute_script("arguments[0].click();", seven_question)

eight_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID69-4-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", eight_question)
driver.execute_script("arguments[0].click();", eight_question)

nine_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID8-2-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", nine_question)
driver.execute_script("arguments[0].click();", nine_question)

ten_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID33-1-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", ten_question)
driver.execute_script("arguments[0].click();", ten_question)

eleven_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID88-4-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", eleven_question)
driver.execute_script("arguments[0].click();", eleven_question)

# 12
twelve_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID103-2-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", twelve_question)
driver.execute_script("arguments[0].click();", twelve_question)

# 13
thirteen_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID10-1-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", thirteen_question)
driver.execute_script("arguments[0].click();", thirteen_question)

# 14
fourteen_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID104-3-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", fourteen_question)
driver.execute_script("arguments[0].click();", fourteen_question)

# 15
fifteen_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID105-2-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", fifteen_question)
driver.execute_script("arguments[0].click();", fifteen_question)

# 16
sixteen_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID106-4-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", sixteen_question)
driver.execute_script("arguments[0].click();", sixteen_question)

# 17
seventeen_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID107-2-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", seventeen_question)
driver.execute_script("arguments[0].click();", seventeen_question)

# 18
eighteen_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID108-3-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", eighteen_question)
driver.execute_script("arguments[0].click();", eighteen_question)

# 19
nineteen_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID66-5-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", nineteen_question)
driver.execute_script("arguments[0].click();", nineteen_question)

# 20
twenty_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID46-6-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", twenty_question)
driver.execute_script("arguments[0].click();", twenty_question)

# 21
twenty_one_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID109-5-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", twenty_one_question)
driver.execute_script("arguments[0].click();", twenty_one_question)

# 22
twenty_two_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID90-5-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", twenty_two_question)
driver.execute_script("arguments[0].click();", twenty_two_question)

# 23
twenty_three_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID89-2-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", twenty_three_question)
driver.execute_script("arguments[0].click();", twenty_three_question)

# 24
twenty_four_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID91-5-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", twenty_four_question)
driver.execute_script("arguments[0].click();", twenty_four_question)

# 25
twenty_five_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID110-4-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", twenty_five_question)
driver.execute_script("arguments[0].click();", twenty_five_question)

# 26
twenty_six_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID93-6-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", twenty_six_question)
driver.execute_script("arguments[0].click();", twenty_six_question)


# fourth page button
next_button_fourth_page = wait.until(EC.element_to_be_clickable((By.ID, "NextButton")))

driver.execute_script("arguments[0].scrollIntoView(true);", next_button_fourth_page)
driver.execute_script("arguments[0].click();", next_button_fourth_page)

# 27
twenty_seven_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID16-1-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", twenty_seven_question)
driver.execute_script("arguments[0].click();", twenty_seven_question)

# fifth page button
next_button_fifth_page = wait.until(EC.element_to_be_clickable((By.ID, "NextButton")))

driver.execute_script("arguments[0].scrollIntoView(true);", next_button_fifth_page)
driver.execute_script("arguments[0].click();", next_button_fifth_page)

# 28
twenty_eight_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID17-1-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", twenty_eight_question)
driver.execute_script("arguments[0].click();", twenty_eight_question)

# 29
twenty_nine_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID18-1-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", twenty_nine_question)
driver.execute_script("arguments[0].click();", twenty_nine_question)

# 30
thirty_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID49-3-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", thirty_question)
driver.execute_script("arguments[0].click();", thirty_question)

# 31
thirty_one_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID48-2-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", thirty_one_question)
driver.execute_script("arguments[0].click();", thirty_one_question)

# 32
thirty_two_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID47-1-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", thirty_two_question)
driver.execute_script("arguments[0].click();", thirty_two_question)

# 33
thirty_three_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID21-4-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", thirty_three_question)
driver.execute_script("arguments[0].click();", thirty_three_question)

# 34
thirty_four_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID95-3-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", thirty_four_question)
driver.execute_script("arguments[0].click();", thirty_four_question)

# 35
thirty_five_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID25-5-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", thirty_five_question)
driver.execute_script("arguments[0].click();", thirty_five_question)

# 36
thirty_six_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID23-4-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", thirty_six_question)
driver.execute_script("arguments[0].click();", thirty_six_question)

# 37
thirty_seven_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID26-3-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", thirty_seven_question)
driver.execute_script("arguments[0].click();", thirty_seven_question)

# 38
thirty_eight_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID55-4-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", thirty_eight_question)
driver.execute_script("arguments[0].click();", thirty_eight_question)

# 39
thirty_nine_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID56-5-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", thirty_nine_question)
driver.execute_script("arguments[0].click();", thirty_nine_question)

# 40
forty_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID97-4-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", forty_question)
driver.execute_script("arguments[0].click();", forty_question)

# 41
forty_one_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID98-5-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", forty_one_question)
driver.execute_script("arguments[0].click();", forty_one_question)

# 42
forty_two_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID60-2-label"]/span',
        )
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", forty_two_question)
driver.execute_script("arguments[0].click();", forty_two_question)

# sixth page button
next_button_sixth_page = wait.until(EC.element_to_be_clickable((By.ID, "NextButton")))

driver.execute_script("arguments[0].scrollIntoView(true);", next_button_sixth_page)
driver.execute_script("arguments[0].click();", next_button_sixth_page)

# Wait for the Forty-three Question element
forty_three_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID96-4-label"]/span',  # Your XPath for Forty-three Question here
        )
    )
)

# Scroll and click the Forty-three Question element
driver.execute_script("arguments[0].scrollIntoView(true);", forty_three_question)
driver.execute_script("arguments[0].click();", forty_three_question)

# Wait for the Forty-four Question element
forty_four_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID99-2-label"]/span',  # Your XPath for Forty-four Question here
        )
    )
)

# Scroll and click the Forty-four Question element
driver.execute_script("arguments[0].scrollIntoView(true);", forty_four_question)
driver.execute_script("arguments[0].click();", forty_four_question)

# Wait for the Forty-five Question element
forty_five_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID50-4-label"]/span',  # Your XPath for Forty-five Question here
        )
    )
)

# Scroll and click the Forty-five Question element
driver.execute_script("arguments[0].scrollIntoView(true);", forty_five_question)
driver.execute_script("arguments[0].click();", forty_five_question)

# Wait for the Forty-six Question element
forty_six_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID63-3-label"]/span',  # Your XPath for Forty-six Question here
        )
    )
)

# Scroll and click the Forty-six Question element
driver.execute_script("arguments[0].scrollIntoView(true);", forty_six_question)
driver.execute_script("arguments[0].click();", forty_six_question)

# Wait for the Forty-seven Question element
forty_seven_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID62-2-label"]/span',  # Your XPath for Forty-seven Question here
        )
    )
)

# Scroll and click the Forty-seven Question element
driver.execute_script("arguments[0].scrollIntoView(true);", forty_seven_question)
driver.execute_script("arguments[0].click();", forty_seven_question)

# Wait for the Forty-eight Question element
forty_eight_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID59-4-label"]/span',  # Your XPath for Forty-eight Question here
        )
    )
)

# Scroll and click the Forty-eight Question element
driver.execute_script("arguments[0].scrollIntoView(true);", forty_eight_question)
driver.execute_script("arguments[0].click();", forty_eight_question)

# Wait for the Forty-nine Question element
forty_nine_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID68-4-label"]/span',  # Your XPath for Forty-nine Question here
        )
    )
)

# Scroll and click the Forty-nine Question element
driver.execute_script("arguments[0].scrollIntoView(true);", forty_nine_question)
driver.execute_script("arguments[0].click();", forty_nine_question)

# Wait for the Fifty Question element
fifty_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID64-3-label"]/span',  # Your XPath for Fifty Question here
        )
    )
)

# Scroll and click the Fifty Question element
driver.execute_script("arguments[0].scrollIntoView(true);", fifty_question)
driver.execute_script("arguments[0].click();", fifty_question)

# Wait for the Fifty-one Question element
fifty_one_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID65-2-label"]/span',  # Your XPath for Fifty-one Question here
        )
    )
)

# Scroll and click the Fifty-one Question element
driver.execute_script("arguments[0].scrollIntoView(true);", fifty_one_question)
driver.execute_script("arguments[0].click();", fifty_one_question)


# seventh page button
next_button_seventh_page = wait.until(EC.element_to_be_clickable((By.ID, "NextButton")))

driver.execute_script("arguments[0].scrollIntoView(true);", next_button_seventh_page)
driver.execute_script("arguments[0].click();", next_button_seventh_page)

# Wait for the Fifty-two Question element
fifty_two_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID115-1-label"]/span',  # Your XPath for Fifty-two Question here
        )
    )
)

# Scroll and click the Fifty-one Question element
driver.execute_script("arguments[0].scrollIntoView(true);", fifty_two_question)
driver.execute_script("arguments[0].click();", fifty_two_question)


# eighth page button
next_button_eighth_page = wait.until(EC.element_to_be_clickable((By.ID, "NextButton")))

driver.execute_script("arguments[0].scrollIntoView(true);", next_button_eighth_page)
driver.execute_script("arguments[0].click();", next_button_eighth_page)


# Wait for the Fifty-three Question element
fifty_three_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QR~QID79"]',  # Your XPath for Fifty-two Question here
        )
    )
)

# Scroll and click the Fifty-three Question element
driver.execute_script("arguments[0].scrollIntoView(true);", fifty_three_question)
driver.execute_script(
    "arguments[0].value = arguments[1];", fifty_three_question, str(random_zipcode)
)

# Wait for the Fifty-four Question element
fifty_four_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QR~QID72"]',  # Your XPath for Fifty-four Question here
        )
    )
)

# Scroll and click the Fifty-four Question element
driver.execute_script("arguments[0].scrollIntoView(true);", fifty_four_question)
driver.execute_script(
    "arguments[0].value = arguments[1];", fifty_four_question, str(random_age)
)


# Wait for the Fifty-five Question element
fifty_five_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID73-2-label"]/span',  # Your XPath for Fifty-five Question here
        )
    )
)

# Scroll and click the Fifty-five Question element
driver.execute_script("arguments[0].scrollIntoView(true);", fifty_five_question)
driver.execute_script("arguments[0].click();", fifty_five_question)


# Wait for the Fifty-six Question element
fifty_six_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID74-4-label"]/span',  # Your XPath for Fifty-six Question here
        )
    )
)

# Scroll and click the Fifty-six Question element
driver.execute_script("arguments[0].scrollIntoView(true);", fifty_six_question)
driver.execute_script("arguments[0].click();", fifty_six_question)

# Wait for the Fifty-seven Question element
fifty_seven_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID75-1-label"]/span',  # Your XPath for Fifty-seven Question here
        )
    )
)

# Scroll and click the Fifty-seven Question element
driver.execute_script("arguments[0].scrollIntoView(true);", fifty_seven_question)
driver.execute_script("arguments[0].click();", fifty_seven_question)


# Wait for the Fifty-eight Question element
fifty_eight_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QR~QID76"]',  # Your XPath for Fifty-eight Question here
        )
    )
)

# Scroll and click the Fifty-four Question element
driver.execute_script("arguments[0].scrollIntoView(true);", fifty_eight_question)
driver.execute_script(
    "arguments[0].value = arguments[1];",
    fifty_eight_question,
    str(random_people_in_household),
)


# Wait for the Fifty-nine Question element
fifty_nine_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QR~QID81"]',  # Your XPath for Fifty-nine Question here
        )
    )
)

# Scroll and click the Fifty-nine Question element
driver.execute_script("arguments[0].scrollIntoView(true);", fifty_nine_question)
driver.execute_script(
    "arguments[0].value = arguments[1];",
    fifty_nine_question,
    str(random_children_in_household),
)


# Wait for the sixty Question element
sixty_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID77-1-label"]/span',  # Your XPath for sixty Question here
        )
    )
)

# Scroll and click the Fifty-seven Question element
driver.execute_script("arguments[0].scrollIntoView(true);", sixty_question)
driver.execute_script("arguments[0].click();", sixty_question)


# Wait for the sixty-one Question element
sixty_one_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID78-3-label"]/span',  # Your XPath for sixty-one Question here
        )
    )
)

# Scroll and click the sixty-one Question element
driver.execute_script("arguments[0].scrollIntoView(true);", sixty_one_question)
driver.execute_script("arguments[0].click();", sixty_one_question)


# nineth page button
next_button_nineth_page = wait.until(EC.element_to_be_clickable((By.ID, "NextButton")))

driver.execute_script("arguments[0].scrollIntoView(true);", next_button_nineth_page)
driver.execute_script("arguments[0].click();", next_button_nineth_page)


# Wait for the sixtty-two Question element
sixty_two_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QR~QID100"]',  # Your XPath for sixty-two Question here
        )
    )
)

# Scroll and click the sixty=two Question element
driver.execute_script("arguments[0].scrollIntoView(true);", sixty_two_question)
driver.execute_script(
    "arguments[0].value = arguments[1];",
    sixty_two_question,
    str(email),
)


# Wait for the sixty-three Question element
sixty_three_question = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="QID101-2-label"]/span',  # Your XPath for sixty-one Question here
        )
    )
)

# Scroll and click the sixty-three Question element
driver.execute_script("arguments[0].scrollIntoView(true);", sixty_three_question)
driver.execute_script("arguments[0].click();", sixty_three_question)


# tenth page button
next_button_tenth_page = wait.until(EC.element_to_be_clickable((By.ID, "NextButton")))

driver.execute_script("arguments[0].scrollIntoView(true);", next_button_tenth_page)
driver.execute_script("arguments[0].click();", next_button_tenth_page)

# eleventh page button
# eleventh page button
next_button_eleventh_page = wait.until(
    EC.presence_of_element_located((By.ID, "NextButton"))
)

driver.execute_script("arguments[0].scrollIntoView(true);", next_button_eleventh_page)

try:
    next_button_eleventh_page.click()
except StaleElementReferenceException:
    next_button_eleventh_page = wait.until(
        EC.presence_of_element_located((By.ID, "NextButton"))
    )
    driver.execute_script(
        "arguments[0].scrollIntoView(true);", next_button_eleventh_page
    )
    next_button_eleventh_page.click()


input("press enter")
