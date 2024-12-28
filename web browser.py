import webbrowser
import os

# List of available browsers (option 9 now opens the GitHub repository)
available_browsers = {
    '1': 'firefox',
    '2': 'chrome',
    '3': 'safari',
    '4': 'edge',
    '5': 'opera',
    '6': 'brave',
    '7': 'vivaldi',
    '8': 'yandex',
    '9': 'source_code',  # Option 9 now opens the GitHub repository directly
}

# GitHub repository URL (replace with your actual repository URL)
github_repo_url = "https://github.com/yourusername/your-repository"  # Replace with your actual GitHub URL

# Function to log errors to a file
def log_error(message):
    with open("browser_error_log.txt", "a") as log_file:
        log_file.write(message + "\n")

# Function to get the browser based on the choice
def get_browser(browser_choice):
    try:
        if browser_choice == '9':  # "Source Code" option opens GitHub repository
            print(f"Opening GitHub repository: {github_repo_url}")
            webbrowser.open_new_tab(github_repo_url)
            return None  # No browser needed for this option
        elif browser_choice in available_browsers:
            browser_name = available_browsers[browser_choice]
            browser = webbrowser.get(browser_name)
            print(f"Using {browser_name.capitalize()} browser.")
            return browser
        else:
            raise ValueError("Invalid browser choice.")
    except Exception as e:
        error_message = f"Error: {str(e)} - Could not detect the browser: {available_browsers.get(browser_choice, 'Unknown')}"
        print(error_message)
        log_error(error_message)
        exit(1)  # Exit if browser isn't found or choice is invalid

# Prompt the user to select a browser
print("Select a browser:")
for key, browser in available_browsers.items():
    print(f"{key}. {browser.capitalize()}")

browser_choice = input("Enter the number for your selected browser: ")

# Get the selected browser
browser = get_browser(browser_choice)

# If the user did not choose the "Source Code" option, open the URL with the selected browser
if browser and browser_choice != '9':
    try:
        print(f"Opening GitHub repository: {github_repo_url}")
        browser.open_new_tab(github_repo_url)
    except Exception as e:
        error_message = f"Error: {str(e)} - Failed to open GitHub URL: {github_repo_url}"
        print(error_message)
        log_error(error_message)
