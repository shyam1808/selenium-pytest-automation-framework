import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
HEADLESS = os.getenv("CI") == "true"
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    # chrome webbrowser invocation
    if browser_name == "chrome":
        chrome_options = ChromeOptions()

        # HEADLESS SETTINGS (Required for GitHub Actions)
        if HEADLESS:
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
    driver.get("https://awesomeqa.com/ui/index.php?route=account/login")
    yield driver
    driver.quit() #teardown


@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            os.makedirs(reports_dir, exist_ok=True)
            # File names
            file_name = report.nodeid.replace("::", "_") + ".png"  # relative path (for HTML)
            file_path = os.path.join(reports_dir, file_name)  # absolute path (for saving)
            #file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "Saving screenshot to:" + file_path )
            _capture_screenshot(file_path)
            if pytest_html:
                html = (
                           '<div>'
                           '<img src="%s" alt="screenshot" '
                           'style="width:304px;height:228px;border:1px solid #ddd;" '
                           'onclick="window.open(this.src)" align="right"/>'
                           '</div>'
                       ) % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(file_path):
    """
    Capture screenshot safely.
    Works for local runs and GitHub Actions.
    """
    global driver

    if driver:
        try:
            driver.save_screenshot(file_path)
        except Exception as e:
            print(f"Screenshot capture failed: {e}")
    else:
        print("Driver not initialized. Screenshot skipped.")