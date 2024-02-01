import requests
from bs4 import BeautifulSoup

url = 'https://www.feiluoglobal.com/661180/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 获取小说名称和作者
book_info = soup.select_one('.novel-info > h1').text.strip()
book_name, book_author = book_info.split(' 作者：')

# 创建一个txt文件，以小说名称命名
with open(f'{book_name}.txt', 'w', encoding='utf-8') as f:
    # 获取小说章节列表
    chapter_list = soup.select('.chapter-list li a')
    for chapter in chapter_list:
        chapter_url = chapter['href']
        chapter_title = chapter.text.strip()
        # 访问每个章节链接并获取内容
        chapter_response = requests.get(chapter_url)
        chapter_soup = BeautifulSoup(chapter_response.content, 'html.parser')
        chapter_content = chapter_soup.select_one('#chapter-container').text.strip()
        # 将章节标题和内容写入txt文件
        f.write(f'{chapter_title}\n\n{chapter_content}\n\n')
        print(f'{chapter_title} 写入完成')