from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def auto_fill_form(url):
    # Connect to the running Chrome session
    options = webdriver.ChromeOptions()
    options.debugger_address = "127.0.0.1:9222"  # Attach to Chrome's debugging port

    # Start Selenium WebDriver
    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to the target URL
        driver.get(url)
        time.sleep(3)  # Wait for the page to load

        while True:
            print("Filling the form on the current page...")

            # Example: Selecting radio buttons dynamically based on the text next to the radio button
            radio_buttons = driver.find_elements(By.XPATH, "//li[.//div[@class='answerlist1']]//input[@type='radio']")
            for radio in radio_buttons:
                label = radio.find_element(By.XPATH, "following-sibling::div[@class='answerlist1']").text
                # Check the text of the label and select the appropriate radio button
                if "Sangat puas" in label:
                    driver.execute_script("arguments[0].click();", radio)
                    time.sleep(0.5)
                    print(f"Selected radio button with label: {label}")
                elif "Tidak" in label:
                    driver.execute_script("arguments[0].click();", radio)
                    time.sleep(0.5)
                    print(f"Selected radio button with label: {label}")
                else:
                    print(f"Skipping radio button with label: {label}")
            
            # Filling out a text area if available
            try:
                text_area = driver.find_element(By.TAG_NAME, "textarea")
                text_area.send_keys("Tidak ada masukan, dosen sudah sangat baik.")
                time.sleep(1)
            except Exception:
                print("No text area found on this page.")

            # Click the "Save and Continue" button if available
            try:
                save_button = driver.find_element(By.XPATH, "//input[@type='image' and @value='simpan']")
                driver.execute_script("arguments[0].click();", save_button)
                time.sleep(3)  # Wait for the next page to load
            except Exception:
                print("No 'Save and Continue' button found. Assuming form is complete.")
                break

        print("Form completed successfully!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Script completed. Chrome will remain open.")

# URL of the form page
form_url = "https://igracias.telkomuniversity.ac.id/survey/?pageid=2001&actC=kuesioneredit&exeC=2&course=2&lec_code=MRT"
auto_fill_form(form_url)
