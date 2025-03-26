import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

# Import website from env
load_dotenv()

base_url = os.getenv("WEBSITE_URL")
session_duration_range = (30, 45)  # session duration in seconds


def start_session():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    # chrome_options.add_argument("--headless")  # Uncomment to run without GUI

    # ignore SSL certificate errors (for HTTP sites)
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Set overall session duration
        session_duration = random.randint(*session_duration_range)
        start_time = time.time()
        end_time = start_time + session_duration

        # Visit the homepage
        driver.get(base_url)

        # Directly try to find and click the proceed button
        time.sleep(2)  # Short wait for page to load so other processes can continue

        # Since its HTTP, click the button allowing entry
        try:
            # Using XPath directly from website
            proceed_button = driver.find_element(By.XPATH, "//*[@id='proceed-button']")
            proceed_button.click()
            print("Found and clicked proceed button using XPath")
        except Exception as e:
            print(f"Could not click using XPath, {e}")

        # Main session loop
        # Continue the session even if we can't find links to click
        while time.time() < end_time:
            try:
                # Find clickable elements (links, buttons, etc.)
                clickable_elements = driver.find_elements(By.TAG_NAME, "a")

                if clickable_elements:
                    # Randomly choose an element to click
                    element = random.choice(clickable_elements)

                    # Scroll to the element
                    driver.execute_script("arguments[0].scrollIntoView();", element)

                    # Simulate reading content for a random time (shorter than remaining time)
                    remaining_time = end_time - time.time()
                    if remaining_time > 0:
                        read_time = min(random.randint(3, 8), int(remaining_time))
                        time.sleep(read_time)

                    # Try to click the element if it's visible and the href is on the same domain
                    try:
                        href = element.get_attribute("href")
                        if href and base_url in href:
                            element.click()
                            # Wait for page to load
                            WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.TAG_NAME, "body"))
                            )

                            # Try to click the proceed button again if we navigate to a new page
                            try:
                                proceed_button = driver.find_element(By.XPATH, "//*[@id='proceed-button']")
                                proceed_button.click()
                                print("Clicked proceed button on new page")
                            except:
                                pass  # No button found, continue normally
                    except Exception as e:
                        print(f"Error clicking element: {e}")
                        # If clicking fails, just continue with current page
                else:
                    # No clickable elements found, just scroll and wait
                    print("No clickable elements found, just scrolling")

                # Scroll down randomly regardless of whether we clicked a link
                scroll_amount = random.randint(100, 1000)
                driver.execute_script(f"window.scrollBy(0, {scroll_amount});")

                # Simulate more reading (shorter than remaining time)
                remaining_time = end_time - time.time()
                if remaining_time > 0:
                    read_time = min(random.randint(2, 5), int(remaining_time))
                    time.sleep(read_time)

                # If very little time left, just wait out the remaining time
                remaining_time = end_time - time.time()
                if 0 < remaining_time < 3:
                    time.sleep(remaining_time)

            except Exception as e:
                # Handle any unexpected errors and continue the session
                print(f"Error during session: {e}")
                time.sleep(1)  # Short wait before continuing

                # If an error causes us to lose the page, go back to base URL
                try:
                    driver.base_url = base_url
                except:
                    driver.get(base_url)

        actual_duration = time.time() - start_time
        print(f"Session completed. Duration: {actual_duration:.2f} seconds (target: {session_duration})")

    finally:
        driver.quit()


# Run multiple sessions
def run_multiple_sessions(count=5):
    """Run multiple browsing sessions"""
    for i in range(count):
        print(f"Starting session {i + 1}/{count}")
        start_session()

        # Wait between sessions
        wait_time = random.randint(5, 15)
        print(f"Waiting {wait_time} seconds before next session...")
        time.sleep(wait_time)


# Example usage
if __name__ == "__main__":
    run_multiple_sessions(5)  # Run x amount of sessions