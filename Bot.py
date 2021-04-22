from selenium import webdriver
import undetected_chromedriver as uc


tabs = input("Tabs:")
cps = input("Clicks:")
url = 'https://popcat.click'
drivers = ["driver1", "driver2"]
script = """
var event = new KeyboardEvent('keydown', {
    key: 'g',
    ctrlKey: true
});

setInterval(function(){
    for (i = 0; i < 200; i++) {
        document.dispatchEvent(event);
    }
}, 0);
"""



options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("--mute-audio")
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.execute_script(script.replace("200", cps))
for i in range(int(f"{tabs}")-1):
    driver.execute_script(f'window.open("about:blank", "{i}");')
    driver.switch_to.window(f'{i}')
    driver.get(url)
    driver.execute_script(script.replace("200", cps))




PROXY = "185.157.161.85:8118"
webdriver.DesiredCapabilities.CHROME['proxy'] = {
"httpProxy": PROXY,
"ftpProxy": PROXY,
"sslProxy": PROXY,
"proxyType": "MANUAL",
}


