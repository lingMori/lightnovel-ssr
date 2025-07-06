import requests
import json
from bs4 import BeautifulSoup
import time

def fetch_with_headers():
    """使用浏览器请求头尝试获取内容"""
    url = "https://novelpia.com/viewer/2921749"
    
    # 模拟浏览器请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        return None

def fetch_with_selenium():
    """使用 Selenium 获取动态内容"""
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from webdriver_manager.chrome import ChromeDriverManager
        
        url = "https://novelpia.com/viewer/2921749"
        
        # 配置 Chrome 选项
        chrome_options = Options()
        # chrome_options.add_argument('--headless')  # 无头模式
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
        
        # 使用 webdriver-manager 自动管理驱动
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        try:
            print("正在加载页面...")
            driver.get(url)
            
            # 等待页面加载完成
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # 额外等待，确保动态内容加载完成
            time.sleep(5)
            
            html_content = driver.page_source
            return html_content
            
        finally:
            driver.quit()
            
    except ImportError as e:
        print(f"缺少依赖包: {e}")
        print("请运行: pip install -r requirements.txt")
        return None
    except Exception as e:
        print(f"Selenium 获取失败: {e}")
        return None

def main():
    print("正在尝试获取网页内容...")
    
    # 方法1: 使用请求头
    print("\n1. 尝试使用浏览器请求头...")
    html_content = fetch_with_headers()
    
    if html_content and len(html_content.strip()) > 100 and False:
        print("✓ 使用请求头成功获取内容")
    else:
        print("✗ 使用请求头失败，尝试 Selenium...")
        
        # 方法2: 使用 Selenium
        html_content = fetch_with_selenium()
        
        if html_content and len(html_content.strip()) > 100:
            print("✓ 使用 Selenium 成功获取内容")
        else:
            print("✗ 所有方法都失败了")
            return
    
    # 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 打印页面标题和部分内容
    title = soup.find('title')
    if title:
        print(f"页面标题: {title.get_text()}")
    
    # 查找可能的内容区域
    content_areas = soup.find_all(['div', 'article', 'main'], class_=True)
    print(f"找到 {len(content_areas)} 个可能的内容区域")
    
    # 保存完整 HTML
    with open("novelpia.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())
    
    print(f"HTML 已保存到 novelpia.html，文件大小: {len(html_content)} 字符")

if __name__ == "__main__":
    main()
