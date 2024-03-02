# Microsoft_research
Automating download of latest pdf from a website.

## With Selenium IDE:

### In your browser (Google Chrome), go to Settings:

Step1: Privacy and Security -> Site Settings -> Additional content settings -> PDF Documents -> Download PDFs

Step2: Downloads -> Deselect "Ask where to save each file before downloading"

Step3: Open Selenium IDE -> Open Existing Project -> Select Microsoft.side provided here

Step4: Run tests to automatically download the latest pdf on URL "https://dsssb.delhi.gov.in/dsssb/latest-updates"

Note: This won't work on selenium command line runner as your google chrome settings are not imported in command line (it creates a new anonymous profile for running  tests), so instead of downloading it will simply preview the latest pdf (default behaviour of Chrome).

### With Pyhton file (Using Selenium and Webdriver):

Step1: Make sure you have python installed on your system.

Step2: Open automate.py in your favourite Code Editor. Update "path" and "download_directory" with your desired location to store downloaded PDF.

Step3: Open Command Prompt, type "python automate.py".
This will automatically download the latest pdf on URL "https://dsssb.delhi.gov.in/dsssb/latest-updates" in your specified location. 

