from selenium import webdriver

search_term = "bluetooth headset"

# Configure Chrome webdriver options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode (without opening browser window)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver executable
chromedriver_path = "path/to/chromedriver"

# Create a new Chrome webdriver instance
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

# Open Amazon search page
driver.get("https://www.amazon.com")

# Locate the search input field and enter the search term
search_input = driver.find_element_by_id("twotabsearchtextbox")
search_input.send_keys(search_term)

# Submit the search form
search_form = driver.find_element_by_xpath("//form[@id='nav-search-bar-form']")
search_form.submit()

# Wait for the search results to load
driver.implicitly_wait(10)

# Find all product listings on the page
product_listings = driver.find_elements_by_css_selector("div[data-asin]")

# Iterate over each product listing and extract the desired information
for listing in product_listings:
    product_name = listing.find_element_by_css_selector("span.a-size-base-plus").text
    sponsored_order = listing.find_element_by_css_selector("span[data-component-type='s-product-image'] .s-sponsored-label-info-icon").text
    price = listing.find_element_by_css_selector(".a-price-whole").text
    product_url = listing.find_element_by_css_selector("a.a-link-normal").get_attribute("href")
    asin = product_url.split("/dp/")[1].split("/")[0]  # Extract ASIN from the product URL

    print("Product Name:", product_name)
    print("Sponsored Order:", sponsored_order)
    print("Price:", price)
    print("ASIN:", asin)
    print()

# Close the webdriver
driver.quit()
