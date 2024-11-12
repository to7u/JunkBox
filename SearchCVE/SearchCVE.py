import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 配列に格納するテキストファイルを読み込む関数
def load_values_from_file(filename):
    with open(filename, 'r') as file:
        values = file.read().splitlines()  # 改行で分割してリストに格納
    return values

# Seleniumを使って動的ページのスクレイピング
def scrape_with_selenium(url):
    # ChromeOptionsを設定してヘッドレスモードにする
    options = Options()
    # options.headless = True  # ヘッドレスモード（ブラウザを表示しない）
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')  # 一部環境で必要
    options.add_argument('--disable-dev-shm-usage')  # 一部環境で必要
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    # ページがロードされるまで待機
    time.sleep(3)
    
    # 動的に生成される内容を取得
    try:
        # content = driver.find_element(By.TAG_NAME, 'body').text  # bodyタグ内のテキストを取得
        content = driver.find_element(By.ID, 'cve-overview').text  # id="cve-overview"のテキストを取得
        print(f"Scraped Content: {content[:100]}...")  # 先頭100文字だけ表示
    except Exception as e:
        print(f"Error scraping the page: {e}")
        content = None
    
    driver.quit()
    return content

# メイン処理
def main():
    # ファイルから値を読み込んで配列に格納
    values = load_values_from_file('input.txt')  # 'input.txt' に読み込む
    with open('output.txt', 'w') as output_file:  # 出力ファイルに結果を書き込む
        for value in values:
            # URLを作成
            url = f"https://access.redhat.com/security/cve/{value}"
            print(f"Scraping URL: {url}")
            
            # 動的ページのスクレイピング（Selenium）
            content = scrape_with_selenium(url)
            
            # 結果を表示
            print(f"Content: {content}")
            print("==============================")
            
            # 結果をoutput.txtに書き込む
            output_file.write(f"URL: {url}\n")

            output_file.write(f"Content: {content}\n")
            output_file.write("==============================\n")
            
            # 3秒間の待機（負荷を軽減するため）
            # time.sleep(3)

if __name__ == '__main__':
    main()
