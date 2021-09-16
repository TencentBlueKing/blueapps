## 蓝鲸Python开发框架（BLUEAPPS）代码结构

目前, 蓝鲸开发框架blueapps源码组成如下：

```bash
├─app_icons
├─blueapps
│  ├─account
│  ├─conf
│  ├─contrib
│  ├─core
│  ├─middleware
│  ├─patch
│  ├─template
│  └─utils
```

* app_icons：蓝鲸icon图片
* blueapps：蓝鲸开发框架源码
  * account：开发框架帐号封装模块。集鉴权中间件、用户类等功能
  * conf：开发框架统一配置类、示例功能模版代码
  * contrib：开发框架执行命令入口模块
  * core：celery配置及请求处理类
  * middleware：开发框架中间件模块
  * patch：日志配置及其它配置类。
  * template：开发框架模版渲染处理模块
  * utils：开发框架工具类



