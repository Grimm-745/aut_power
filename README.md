# aut_power
<h1 align="center">
  <br>
  <img src="./favicon.ico" width="50px" alt="aut_power">
</h1>

<h4 align="center">aut_power 基于python的自动化模拟登录</h4>

<p align="center">
  <a href="#开始">开始</a> •
  <a href="#调整">调整</a> •
  <a href="#示例">示例</a> •
  <a href="#faq">FAQ</a> •
</p>

[简体中文]

---

## 开始

**安装库**
- 建议先给pip换源 [[Recommend](https://webxxe.cn/index.php/archives/452/)]
  - [(https://webxxe.cn/index.php/archives/452/)](https://webxxe.cn/index.php/archives/452/)

- pip install
  - `pip install -r requirements.txt`

> 电脑要自己下有chrome浏览器，版本要113.0以上的

**使用**

1.启动
```bash
python aut_power.py
```

2.双击打开index.html，填写好对应信息
- URL : `登陆页面地址`
- username : `登陆用户名`
- Password File Path : `密码字典路径`
- Username CSS Selector : `登陆页面填入账号的标签的selector`
- Password CSS Selector : `登陆页面填入密码的标签的selector`
- Submit Button CSS Selector : `登陆页面点击提交的标签的selector`

复制selector方法如下：
<img src="./img/selector.png" width="1000px" alt="aut_power">

**python环境**

适配python3.7以上环境



**适用环境**

适用于账号密码经过加密处理，登陆后没有跳转，没有验证码的登陆页面


---

## 调整

因为登陆的速度和网速成正比，所以在使用的时候如果网速慢或者挂了全局代理，可以到aut_power.py中调整等待时间稍长一点

可调节处已经标注`#等待结果`

## 示例
