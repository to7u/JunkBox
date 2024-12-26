import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def load_values_from_form(cve):
    values = cve.split('\r\n')
    print(values)
    return values

# Seleniumを使って動的ページのスクレイピング
def scrape_with_selenium(url):
    # ChromeOptionsを設定してヘッドレスモードにする
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')  # 一部環境で必要
    options.add_argument('--disable-dev-shm-usage')  # 一部環境で必要
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # ページがロードされるまで待機
    time.sleep(3)
    # 動的に生成される内容を取得
    try:
        content = driver.find_element(By.ID, 'cve-overview').text  # id="cve-overview"のテキストを取得
        print(f"Scraped Content: {content[:100]}...")  # 先頭100文字だけ表示
    except Exception as e:
        print(f"Error scraping the page: {e}")
        content = None
    driver.quit()
    return content

# メイン処理
def main(cve):
    # formから送信された値をから配列を作成
    values = load_values_from_form(cve)
    # print(cve)
    content = ""
    for value in values:
        url = f"https://access.redhat.com/security/cve/{value}\n"
        content += url
        print(url)
        content += scrape_with_selenium(url)
        # print(content)
        content += "\n==================\n"
    return content

if __name__ == '__main__':
    main()
