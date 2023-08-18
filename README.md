# FastTraceESLog

## Introduction

根据traceId 检出相关elk 上的链路日志, 并使用本地文本编辑器打开, 按照时间正序排列, 相对于kibana看日志, 更简单直接, 当然需要更多复杂信息时, 还是需要kibana, 本工具只是方便本地查看trace 链路 log.

![](https://files.catbox.moe/31uju3.png)

## Usage

1. clone 项目, `git@github.com:Fly0708/FastTraceESLog.git`

2. 修改`config.properties`, 填入相关ElasticSearch 连接数据, 具体参数

   ```
   es.url ElasticSearch连接url
   es.username ElasticSearch用户名
   es.password ElasticSearch密码
   random.log.file.path logfile暂存路径, 建议新建单独文件夹
   
   ```

3. 将`ft.bat`文件夹目录加入环境变量path中(Windows 系统)

4. 在terminal中就可以 ft trace_id 来检出该trace日志了, 例如 `ft c7098f5502b8e440`

根据traceId或关键词搜索 elk 的日志, 并按时间升序的写入到临时log文件, 并调用本地文本编辑器打开, 当前默认atom 编辑器, 未做扩展 可自行修改.

## Best Practices

结合utools 和其中的快捷命令插件
