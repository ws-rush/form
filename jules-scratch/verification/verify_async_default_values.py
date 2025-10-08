from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:3001")

    # Wait for the loading indicator to appear and then disappear
    loading_indicator = page.get_by_text("Loading...")
    expect(loading_indicator).to_be_visible()
    expect(loading_indicator).to_be_hidden()

    # Assert that the input fields have the correct default values
    first_name_input = page.get_by_label("First Name:")
    expect(first_name_input).to_have_value("Jules")

    last_name_input = page.get_by_label("Last Name:")
    expect(last_name_input).to_have_value("The Engineer")

    # Take a screenshot for visual verification
    page.screenshot(path="jules-scratch/verification/verification.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)