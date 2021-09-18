# Delete-Unread-Emails-Gmail
Currently, Gmail is limited to deleting 50 emails per cycle, which is incredibly tedious for someone who harbors +1000 unread email messages. This program is meant to automate this process. 

# Program Efficieny 
* Overview: 
    * Deletes 90% of unread messages on its first run, and 99.99% on its second one. 
   
* Time and Space Complexity 
    * O(n) Time, O(1) Space
    
# Prerequisites
* ###  Python 3.9.5 installed on machine
* ###  An IDE (Ex. Visual Studio Code) installed on machine
    * If using VS Code, you should also install the Python extension for VS Code.
* ###  Download Appropriate Chrome Version Driver

    1. On Chrome url bar, type chrome://version, and record the official Build number (ex. 93.04577.82)
    
    2. Download and unzip the appropriate chrome driver from : https://sites.google.com/chromium.org/driver/
        * Ex: If Chrome Build number is 93.04577.92, download the 93.0.4577.63 chrome driver
        
    3. Create a new folder called chromeDriver, and move it to your local C:/ directory
    
    4. Move chromeDriver.exe into chromedriver folder. Below is an example
        * https://drive.google.com/file/d/1k4WVkBPVSh5JxBrAQfK9i4rXbA8H_Hx8/view?usp=sharing
        
* ### Google Account Settings 
    * You MUST disable 2-factor authentication on the Google Account you are trying to access 
        * https://support.google.com/accounts/answer/1064203?hl=en&co=GENIE.Platform%3DDesktop
    * You MUST give less secure apps access to your gmail account.  
        * https://support.google.com/accounts/answer/6010255?hl=en#zippy=%2Cif-less-secure-app-access-is-off-for-your-account
    * Undo these settings after running the program, so your Google account and data remains secure. 
    
* ### Optional: 
     * Set up a virtual environment in project directory
           * Run ```py -m venv virtual ``` from terminal

# Installing necessary modules
* Run ```pip install -r requirements.txt ``` in project directory, using the terminal (if not using virtual environment)
    * if using a virtual environment, ensure it is active before running this command.
* Overview of modules and libraries requried 
    1. selenium
         * Selenium Documentation : https://www.selenium.dev
    2. selenium_stealth
         * Selenium Stealth Documentation : https://openbase.com/python/selenium-stealth/documentation

# You are ready to run the program! 
* If you are using an IDE, you can easily click on the play button on the index.py file. 
* You may also run this program from the terminal

## Important Notices: 
1. This program REQUIRES you to manually input your username/email, and click the next button.
      * This is due to Google's incredibly tough and secure bot detection algorithms. If this were completely automated, the user would be unable to sign into their account due to secruity risks. However, after manually entering your username/email and clicking next, everything from inputting your password to deletion of emails, is completely automated
      * You are given 40 seconds to manually input this information, but its duration can be increased in the index.py file.
2. This code runs optimally on Google Chrome version 93.0.4577.82, as of Sept 18th, 2021. 
      * If run on a different verison, setup portion of code may need adjustments   
3. This project will not be maintained by owner, but feel free to use it as a template for your own projects
4. Do not create a verison of this program that infringes upon the privacy rights of others. 
