# 版本日志
## 3.0.0
- 新功能
    - 支持django2.2版本
    
## 3.0.1
- 修复
    - 修复jwt下，ESB使用白名单方式导致登录事变
    - 修复py3下，RIO登录存在问题
- 功能
    - 支持对外版本下支持登录弹框的能力
## 3.1.0
- 优化
    - 去掉对外版本下SaaS用户管理和平台同步逻辑
## 3.2.0
- 优化
    - 增加样例国际化
    
## 3.2.1
- 修复
    - 修复bk-admin startexample 命令生成开发样例适配不同平台调用不同的接口获取业务列表
    - blueapps/conf/project_template/config/__init__.py 增加 get_env_or_raise(key)函数
    - 国际化单词矫正(django1.11.x -> django2.x)
## 3.2.2
- 新功能
    - 增加获取app_host的函数 `get_app_host_by_request(request)`
    - 增加 `REMOTE_ANALYSIS_URL` saas 访问统计js url
    - 增加 `REMOTE_API_URL` paas 提供的前端 api.js url
    - 增加 `APIGW_APP_CODE_KEY` 从 apigw jwt 中获取 app_code 键
    - 增加 `APIGW_USER_USERNAME_KEY` 从 apigw jwt 中获取用户名的键
    
## 3.2.3
- 优化
    - 在文件中增加开源版权头信息
    - 修改open版本的csrf_token的`CSRF_COOKIE_NAME`值 为 `csrftoken`
## 3.2.4
- 优化
    - session过期时间使用默认值两周
    - 登录信息缓存改为使用cache缓存
    - admin管理页面增加用户名和是否管理员的过滤条件
## 3.2.5
- 优化
    - 对代码进行 pep8 优化
    
## 3.2.6
- 修复
    - 修复登录失效时无正常触发登录问题
- 优化
    - 优化session_id根据app_code动态发生变化
    
## 3.2.7
- 优化
    - 依赖的markupSafe依赖版本配置更改为1.1.1
    - 增加bk_ticket支持rio的登录方式
    
## 3.2.8
- 优化
    - 默认配置添加 celery 60s心跳配置
    
## 3.2.9
- 新功能
    - 增加前后端分离开发模式下本地和预发布环境中的跨域配置选项
    - 小程序样例前端支持本地配置
- 修复
    - 修复Exception ERROR_CODE问题
- 优化
    - 升级依赖的django-celery版本为3.3.1
## 3.3.0
- 新功能
    - 升级celery版本到celery4.4.0
    - 支持python3.7及以上版本
    
## 3.3.1
- 修复：
    - 修复日志级别设置不生效问题
    - 修复开发样例发送验证码校验超时逻辑时区问题
- 优化：
    - 优化开发框架代码规范
    - 更新celery相关命令
## 3.3.2
- 修复：
    - 修复前后端分离Hash路由模式下登陆重定向首页问题
  
## 3.3.4
- 优化：
    - 针对新版chrome不支持iframe登陆情况，页面直接跳转，ajax用弹窗登陆进行替换
    - 兼容paas企业版V3环境配置
## 3.3.6
- 新增：
  - 自动获取ESB-APIGW公钥(api_public_key)
  - 新增APIGW公钥缓存清理命令: python manage.py apigw_clean_cache
 
- 优化   
  - 在开发框架集成JWT SDK, 减少bkoauth依赖
## 3.3.7
- 修复：
    - 修复 bk_ticket 模式下认证失败，依旧写入 cache，导致无法触发登录重定向
## 3.3.8
- 优化：
    - 兼容 blueking 包缺失时进行部署
    
## 3.3.9
- 修复：
  - 修复Django启动时app未注册的错误
## 3.3.10
- 优化:
    - 开发框架支持修改open版本登录窗口大小
  
## 3.3.11
- 优化：
  - 去除six依赖，不再保证py2兼容
  
## 3.3.12
- 修复：
  - 登录态失效时关闭弹窗的问题
## 3.3.13
- 优化：
  - pycrypto 替换为 pyCryptodome==3.9.7
