from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from support.logger import logger


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # ### CHROME Browser ####
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # ### FIREFOX Browser ####
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument("--window-size=1440, 900")
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # ### BROWSERSTACK ###
    # bs_user = 'enter your own bs_user'
    # bs_key = 'enter your own email bs_key'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     ##Windows##
    #     # 'os': 'Windows',
    #     # 'osVersion': '11',
    #     # 'browserName': 'Chrome',
    #     # 'browserVersion': 'latest',
    #     # 'sessionName': scenario_name
    #     ##OSX##
    #     # 'os': 'OS X',
    #     # 'osVersion': 'Monterey',
    #     # 'browserName': 'Safari',
    #     # 'browserVersion': '15.6',
    #     # 'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


#  ### To run behave with allure in terminal, use: ###
#  # behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/password.feature
#  ### To generate report, run: ###
#  # allure serve test_results/

def before_scenario(context, scenario):
    logger.info(f'Started scenario: {scenario.name}')
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'Started step: {step}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
