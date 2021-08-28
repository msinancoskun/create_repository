import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class RepositoryCreate:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://github.com/login')

    username = '*********'
    password = '********'

    folder_name = input("What is the name of the directory you want to make?\n")
    path = 'C:/Users/Sinan/Desktop/git_repos/' + folder_name

    def create_folder(self):
        
        try:    
            os.mkdir(self.path, mode=0o777)
        
        except FileExistsError:
            print(self.folder_name + ' already exists! Try another one...')
            print("Do you want to create another repository or continue with the one you have? (Y/N)")
            yes_or_no = input(">").upper()
            if yes_or_no == 'Y':
                pass
            else:
                self.create_folder()

    def repository(self):
        login_info = self.browser.find_element_by_xpath('//*[@id="login_field"]')
        login_info.send_keys(self.username)

        login_info = self.browser.find_element_by_xpath('//*[@id="password"]')
        login_info.send_keys(self.password)

        login_info = self.browser.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
        login_info.click()

        self.browser.get('https://github.com/new')

        create_remote_repo = self.browser.find_element_by_xpath('//*[@id="repository_name"]')
        create_remote_repo.send_keys(self.folder_name)

        create_remote_repo = self.browser.find_element_by_xpath('//*[@id="repository_description"]')
        create_remote_repo.send_keys('remote repo automation test!')

        button = self.browser.find_element_by_css_selector('button.first-in-line')
        button.submit()


if __name__ == '__main__':
    create = RepositoryCreate()
    # create.create_folder()
    create.repository()
