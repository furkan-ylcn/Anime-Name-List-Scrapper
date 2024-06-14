# Selenium Web Scraper

This repository contains a Python script that uses Selenium WebDriver to scrape anime titles from the TurkAnime website.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/turkanime-scraper.git
    cd turkanime-scraper
    ```

2. **Install the required Python packages:**
    ```sh
    pip install selenium
    ```

3. **Download Chrome WebDriver:**
    - Download the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Ensure the WebDriver version matches your installed Chrome browser version.
    - Place the `chromedriver.exe` in a directory and update the `chrome_driver_path` variable in the script with the correct path.

## Usage

1. **Update the WebDriver path:**
    Ensure the `chrome_driver_path` variable in the script points to your `chromedriver.exe` location.

    ```python
    chrome_driver_path = r'./ChromeDriver/chromedriver.exe'
    ```

2. **Run the script:**
    ```sh
    python scraper.py
    ```

## Script Explanation

The script performs the following actions:

1. **Initial Setup:**
    - Import necessary modules from Selenium.
    - Define the path to the Chrome WebDriver.

2. **Open TurkAnime Website:**
    - Navigate to the TurkAnime homepage.

3. **Navigate to Anime List:**
    - Click on the "Anime İzle" link to open the anime list in a new window.
    - Close the popup window and switch back to the main window.

4. **Scrape Anime Titles:**
    - Continuously click the "Sonraki" button to load more anime titles.
    - Extract and print the titles of the anime displayed on the page.

5. **Close the Browser:**
    - After scraping all titles, close the browser.

## Notes

- Ensure your Chrome browser is up-to-date and the Chrome WebDriver version matches your browser version.
- Modify the sleep times if the script runs too fast or too slow.

## License

This project is licensed under the MIT License.

## Acknowledgements

- The script uses [Selenium WebDriver](https://www.selenium.dev/documentation/en/webdriver/) for web scraping.
- The TurkAnime website for providing the anime titles.

