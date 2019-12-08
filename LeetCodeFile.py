# author: 村纪委
# createTime: 2019/12/8 17:00
# name: LeetCodeFile 爬取力扣所有题库标题
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import threading


def open_chrome(file_list):
    browser = webdriver.Chrome()
    count = 0
    try:
        browser.get('https://leetcode-cn.com/problemset/all/')
        select = browser.find_element(By.CLASS_NAME, "zh-hans")
        select.find_element(By.XPATH, '//option[@value="9007199254740991"]').click()
        table_data = browser.find_element(By.CLASS_NAME, "reactable-data")
        for item in table_data.find_elements(By.XPATH, '//tr//div//a'):
            file_list.append(item.text)
            if len(file_list) == 100:
                print(file_list)
                file_list_copy = file_list[:]
                t = threading.Thread(target=save, args=(file_list_copy,))
                t.start()
                file_list.clear()
            count += 1
    finally:
        print("over")
        print(count)
        browser.close()


def save(file_name_list):
    print('每获得100个存一次')
    for item in file_name_list:
        with open("leetcode/" + str(validateTitle(item)).replace(' ', '') + '.md', 'w', encoding='UTF-8') as f:
            f.write("#" + item + ":")


def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title


if __name__ == '__main__':
    file_list = []
    open_chrome(file_list)
    print(file_list)
