
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage(object):
  """This is the base page object.  It is used to create all page objects"""

  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 10)
    self.ec = EC
    self.by = By

class MessageFeature(BasePage):

    # clicks on login icon
    def clickLoginPerson(self):
        path = '//*[@id="top-right-navigation"]/div[2]/a'
        self.driver.find_element_by_xpath(path).click()

    # adds email on log in module
    def addEmail(self, email):
        self.driver.find_element_by_id('login-name').send_keys(email)

    # adds password on log in module
    def addPassword(self, pw):
        path = '//*[@id="sign-in-form"]/input[2]'
        self.driver.find_element_by_xpath(path).send_keys(pw)

    # clicks sign in on log in module
    def clickSignIn(self):
        path = '//*[@id="sign-in-form"]/input[4]'
        self.driver.find_element_by_xpath(path).click()

    # hovers over 'Message' tab to make subtabs visible
    def hoverMessage(self):
        tab = self.driver.find_element_by_xpath('//*[@id="nav-container"]/ul[1]/li[4]/div/a')
        hover = ActionChains(self.driver).move_to_element(tab)
        hover.perform()

    # clicks on subtab 'Send Message'
    def clickSendMessage(self):
        path = '//*[@id="sub-nav-messages"]/li[2]/a'
        self.driver.find_element_by_xpath(path).click()

    # clicks 'Select Connections' on message feature
    def clickSelectConnections(self):
        path = '//*[@id="MessageSendToSelectConnections"]'
        self.driver.find_element_by_xpath(path).click()

    # adds connections on compose message feature (only after select connections)
    def addSelectConnections(self, con):
        path = '//*[@id="MessageSendForm"]/div[2]/div[2]/input'
        self.driver.find_element_by_xpath(path).send_keys(con)

    # clicks on 'Send to all connections' on compose message feature
    def clickSendToAllConnections(self):
        path = '//*[@id="MessageSendToAllConnections"]'
        self.driver.find_element_by_xpath(path).click()

    # clicks on 'JOOR Regress' receipient in message feature
    def clickJoorReg(self):
        path = '/html/body/ul/li[1]/a'
        wait = WebDriverWait(self.driver, 10)
        conn = wait.until(EC.visibility_of_element_located((By.XPATH, path)))
        conn.click()

    # adds message to subject line of message feature
    def addSubject(self, msg):
        path = '//*[@id="MessageSubject"]'
        self.driver.find_element_by_xpath(path).send_keys(msg)

    # adds message to body of message feature
    def addMessage(self, msg):
        self.driver.find_element_by_id('MessageBody').send_keys(msg)

    # clicks send on message feature
    def clickSend(self):
        path = '//*[@id="MessageSendForm"]/a'
        self.driver.find_element_by_xpath(path).click()

    # finds and returns element 'Your message has been sent'
    def msgSentVerification(self):
        path = '/html/body/p'
        wait = WebDriverWait(self.driver, 10)
        txt = wait.until(EC.visibility_of_element_located((By.XPATH, path)))
        return txt.text


