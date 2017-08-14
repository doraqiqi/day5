一、基本功能
模拟实现一个ATM + 购物商城程序

- 额度 15000或自定义
- 实现购物商城，买东西加入 购物车，调用信用卡接口结账
- 可以提现，手续费5%
- 支持多账户登录
- 支持账户间转账
- 记录每月日常消费流水
- 提供还款接口
- ATM记录操作日志 
- 提供管理接口，包括添加账户、用户额度，冻结账户等。。。
- 用户认证用装饰器


二、运行环境
python版本：python 3.6.1

三、移植性
该程序只能在windows系统上运行

四、目录结构及说明


    ATM及购物商城
    │
    ├─README
    │
    ├─Atm
    │  │
    │  ├─bin
    │  │  atm.py #主程序入口
    │  │
    │  │
    │  ├─conf
    │  │ settings.py #一些配置文件
    │  │  
    │  ├─core
    │  │ accounts.py #用于从文件里加载和存储账户数据
    │  │ auth.py #验证模块
    │  │ db_handler.py #读取数据库模块
    │  │ logger.py #日志模块
    │  │ main.py #主程序
    │  │ transaction.py #交易模块
    │  │
    │  ├─db
    │  │  │
    │  │  ├─accounts #一些账户，包括用户名、密码、额度
    │  │  │  │  a.json
    │  │  │  │  b.json
    │  │  │  │  c.json
    │  │  │  │  d.json
    │  │  │  │  e.json
    │  │  │  │  mall.json
    │  │  │  │
    │  │  │  └─frozen #冻结的账户
    │  │  │  f.json
    │  │  │
    │  │  └─logs #每个账户对应的日志
    │  │  a.txt
    │  │  b.txt
    │  │
    │  ├─logs #程序的日志
    │  │
    │  └─test #测试内容
    │  test.py
    │
    └─Mall
    	money #购物车里的商品总额
    	product #商品
    	product.bak
    	shoppingCart_buy.py #买家程序
    	shoppingCart_sell.py #卖家程序
    	shoppinglist #购物车

五、程序使用方法及功能：

**1、atm**

a、运行atm\bin\atm.py可以运行程序

b、使用普通账户登陆后可以进行还款、取现、转账、账户查询、账单查询等操作

c、使用admin账户登陆，密码123456，可以进行额度管理、账户管理、账户冻结解冻等操作

**2、购物商城**

a、运行shoppingCart_sell.py可以运行卖家程序，编辑货物和价格

b、运行shoppingCart_buy.py可以运行买家程序

c、买家程序先选择要购物的商品加入购物车，再按c查看购物车，进入购物车后可以结算或返回，返回时可以选择清空购物车或不操作

d、结算时调用ATM，使用用户帐号登陆后付款

e、可以用，帐号：mall，密码：MALL来管理购物商城在atm的帐号




