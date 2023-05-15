# aut_power
<h1 align="center">
  <br>
  <img src="./favicon.ico" width="50px" alt="aut_power">
</h1>

<h4 align="center">aut_power 基于python的自动化模拟登录</h4>

<p align="center">
  <a href="#开始">开始</a> •
  <a href="#options">Options</a> •
  <a href="#example">Example</a> •
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
<img src="./img/selector.png" width="1000px" alt="aut_power">

**python环境**

适配python3.7以上环境



**适用环境**

适用于账号密码经过加密处理，登陆后没有跳转，没有验证码的登陆页面


---

## Options

The following options are currently supported by f8x

**Batch installation**
- `-b`            : install Basic Environment (gcc、make、git、vim、telnet、jq、unzip and other basic tools)
- `-p`            : install Proxy Environment (Warning : Use only when needed)
- `-d`            : install Development Environment (python3、pip3、Go、Docker、Docker-Compose、SDKMAN)
- `-k` (`a`/`b`/`c`/`d`/`e`): install Pentest environment (hashcat、ffuf、OneForAll、ksubdomain、impacket and other Pentest tools)
- `-s`            : install Blue Team Environment (Fail2Ban、chkrootkit、rkhunter、shellpub)
- `-f`            : install Other Tools (AdguardTeam、trash-cli、fzf)
- `-cloud`        : install Cloud Applications (Terraform、Serverless Framework、wrangler)
- `-all`          : fully automated deployment (Compatible with CentOS7/8,Debain10/9,Ubuntu20/18,Fedora33)

**Development Environment**
- `-docker`         : install docker
- `-lua`            : install lua
- `-nn`             : install npm & NodeJs
- `-go`             : install go
- `-oraclejdk(8/11)`: install oraclejdk
- `-openjdk`        : install openjdk
- `-py3(7/8/9/10)`  : install python3
- `-py2`            : install python2
- `-pip2-f`         : force install pip2 (It is recommended to run with the -python2 option failing)
- `-perl`           : install perl
- `-ruby`           : install ruby
- `-rust`           : install rust
- `-code`           : install code-server
- `-chromium`       : install Chromium (Used with rad, crawlergo in the -k option)
- `-phantomjs`      : install PhantomJS

**Blue Team Service**
- `-binwalk`      : install binwalk
- `-binwalk-f`    : force install binwalk (It is recommended to run if the -binwalk option fails)
- `-clamav`       : install ClamAV
- `-lt`           : install LogonTracer (High hardware configuration requirements)
- `-suricata`     : install Suricata
- `-vol`          : install volatility
- `-vol3`         : install volatility3

**Red Team Service**
- `-aircrack`     : install aircrack-ng
- `-bypass`       : install Bypass
- `-goby`         : install Goby (The client side requires a graphical environment, the server side does not.)
- `-wpscan`       : install wpscan
- `-yakit`        : install yakit

**Red Team Infrastructure**
- `-awvs14`       : install AWVS14 (~1.04 GB)
- `-cs`           : install CobaltStrike 4.3
- `-cs45`         : install CobaltStrike 4.5
- `-frp`          : install frp
- `-interactsh`   : install interactsh (https://github.com/projectdiscovery/interactsh)
- `-merlin`       : install merlin (https://github.com/Ne0nd0g/merlin)
- `-msf`          : install Metasploit
- `-nps`          : install nps
- `-pupy`         : install pupy (https://github.com/n1nj4sec/pupy)
- `-rg`           : install RedGuard (https://github.com/wikiZ/RedGuard)
- `-sliver`       : install sliver-server && client (https://github.com/BishopFox/sliver)
- `-sliver-client` : install sliver-client
- `-sps`          : install SharPyShell (https://github.com/antonioCoco/SharPyShell)
- `-viper`        : install Viper (~2.1 GB)

**Docker-based environment deployment**
- `-arl`          : install ARL (~872 MB)
- `-mobsf`        : install MobSF (~1.54 GB)
- `-nodejsscan`   : install nodejsscan (~873 MB)
- `-vulhub`       : install vulhub (~210 MB)
- `-vulfocus`     : install vulfocus (~1.04 GB)
- `-TerraformGoat`: install TerraformGoat

**Miscellaneous Services**
- `-asciinema`    : install asciinema
- `-bt`           : install 宝塔服务
- `-clash`        : install clash (https://github.com/juewuy/ShellClash)
- `-nginx`        : install nginx
- `-ssh`          : install ssh (RedHat is available by default, no need to reinstall)
- `-ssr`          : install ssr
- `-zsh`          : install zsh

**Other**
- `-clear`        : Clean up system usage traces
- `-info`         : View system information
- `-optimize`     : Improve device options and optimize performance
- `-remove`       : Uninstall some vps cloud monitoring
- `-rmlock`       : Run the Unlock module
- `-swap`         : Configuring swap partitions
- `-update`       : Update f8x
- `-upgrade`      : Upgrade Pentest tools

---

## Example
