import unittest
from selenium import webdriver
from pageObjects import MessageFeature

class MessagingTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.Message = MessageFeature(self.driver)

        # Navigate to https://staging.joordev.com
        self.driver.implicitly_wait(30)
        self.driver.get('https://staging.joordev.com')

        # Click on person login icon in top right corner
        self.Message.clickLoginPerson()

        # Add email and password credentials and click sign in
        self.Message.addEmail('qatest1')
        self.Message.addPassword('qatest1')
        self.Message.clickSignIn()

    def testSentMessage(self):
        self.driver.implicitly_wait(30)
        self.Message.hoverMessage()  # Hover over Messages tab
        self.Message.clickSendMessage() # Click Send a Message
        self.Message.clickSelectConnections() # Click select connections
        self.Message.addSelectConnections('JOOR Regress') # Add connection
        self.Message.clickJoorReg() # Clicks on JOOR Regress connection
        self.Message.addSubject('Message Subject') # Fill out subject of message feature
        self.Message.addMessage('Message Body') # Fill out body of message feature
        self.Message.clickSend() # Click send on message feature
        self.assertEqual(self.Message.msgSentVerification(), 'Your message has been sent')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()