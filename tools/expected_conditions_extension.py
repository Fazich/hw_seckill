from selenium.webdriver.support import expected_conditions as EC

def title_contains_any(titles: list) -> EC.Callable[[EC.WebDriver], bool]:
    """An expectation for checking that the title contains any of the case-sensitive
    substrings from the given list.

    titles is a list of fragments of title expected.
    Returns True if the title matches any fragment in the list, False otherwise.
    """

    def _predicate(driver):
        return any(title in driver.title for title in titles)

    return _predicate