# 蓝鲸Python开发框架使用教程

**注**：blueapps `3.2.x` 版本推荐使用python `3.6.x` 环境，默认安装django版本为 `2.2.6` 。 blueapps `2.5.x` 版本对应的django版本为 `1.11.23`。

在`pip install blueapps-open`安装完毕后，你可以直接基于里面的代码进行开发。或者使用蓝鲸提供的开发框架样例进行开发。

蓝鲸开发框架样例下载地址：https://bk.tencent.com/docs/document/6.0/149/6700

蓝鲸开发框架使用说明请参考：https://bk.tencent.com/docs/document/6.0/130/5949

## bk-admin命令

blueapps提供了`bk-admin <celery | celerybeat | migrate_from_djcelery> [OPTIONS] [ARGS]...`命令。

其中，`celery`，`celerybeat`与原生celery的命令一致，`migrate_from_djcelery`为celery数据库迁移命令。

下面示例创建一个celery任务：

```python
# cel.py
from celery import Celery

app = Celery('tasks', broker='pyamqp://admin@localhost//')

@app.task
def add(x, y):
    return x + y
```

启动worker：`bk-admin celery -A cel worker --loglevel=INFO`即可。

