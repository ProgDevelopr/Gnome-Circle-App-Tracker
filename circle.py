from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

DATA_FILE = "gnome_circ.txt"

def read():
    try:
        with open(DATA_FILE, "r") as f:
            cont = [line.strip() for line in f.read().splitlines() if line.strip()]
            cont = [item.replace(' - NEW!!','') for item in cont]
            cont = [item.replace('é','e') for item in cont]
            cont = [item.replace('à','a') for item in cont]
            return cont
    except:
        return []
    
OLD_DATA = read()
before = f"{len(OLD_DATA)}"

def clear():
    with open(DATA_FILE, "w") as f:
        f.write("")
        
def write(writing):
    with open(DATA_FILE, "a") as f:
        f.write(str(writing) + "\n")

service = Service(".\driver\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.minimize_window()
driver.get("https://apps.gnome.org/#circle")
driver.implicitly_wait(10)

apps = driver.find_elements(by=By.XPATH, value="/html/body/div[2]/section[3]/ul/li/a/div/b/span")

apps = [x.text.strip() for x in apps if x.text.strip()]
apps = [item.replace('é','e') for item in apps]
apps = [item.replace('à','a') for item in apps]
now = f"{len(apps)}"

clear()
new_apps = 0
for app in apps:
    if app in OLD_DATA:
        write(f"{app}")
        print(f"App: {app}")
    else:
        write(f"{app} - NEW!!")
        print(f"New: {app}")
        new_apps += 1
print("\n+ SUMMARY")
print(f"""| Amount of apps before: {before}
| Amount of apps found: {now} 
| New apps found: {new_apps}""")

driver.quit()