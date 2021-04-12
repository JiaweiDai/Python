from selenium.webdriver import Chrome
from selenium import webdriver

#driver = Chrome('./chromedriver')

driver = webdriver.Chrome()

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})
#driver.get('https://www.rebatesme.com/')
driver.get('https://www.baidu.com/')