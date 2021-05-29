from selenium import webdriver
from time import sleep
from secrets import pw
from selenium.webdriver.common.keys import Keys
from random import randint

class Bot():

    links = []

    comments = [
        'Great post!', 'Awesome!' , 'Woah!' , 'Amazing Content'
    ]

    def __init__(self):
        self.login('your_id_username',pw)
        self.like_comment_by_hashtag('stockstobuy')

    def login(self, username, password):
        self.driver = webdriver.Chrome('C:/Users/Ramesh/Downloads/chromedriver_win32/chromedriver') # Enter the path where chromedriver is installed in your device
        self.driver.get('https://instagram.com/')
        sleep(5)
        username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        sleep(1)
        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()  #XPath locators can also use attributes other than id and name for locating the element.
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click() # clicking 'not now button'
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click() # clicking 'not now button'

    def like_comment_by_hashtag(self, hashtag):
        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        links = self.driver.find_elements_by_tag_name('a')   #Here instead of element, elements is used beacause more than one links are going to be there 
        #This method allows you to find a web-element by specifying the tag name.

        def condition(link):
            return '.com/p/' in link.get_attribute('href') #get_attribute method is used to get attributes of an element, such as getting href attribute of anchor tag. 
        valid_links = list(filter(condition, links))

        for i in range(15):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        for link in self.links:
            self.driver.get(link)
            # like
            sleep(3)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
            sleep(5)

            # comment
            self.driver.find_element_by_class_name('RxpZH').click()   #This method allows you to locate elements based on the class name.
            sleep(1)
            self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0,1)])
            sleep(1)
            self.driver.find_element_by_xpath("//button[@type='submit']").click()

def main():
    while True:
        my_bot = Bot()
        sleep(60*60) # one hour

if __name__ == '__main__':
    main()

