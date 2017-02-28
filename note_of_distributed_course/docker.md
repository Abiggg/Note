---
name: docker.md
date:
update:
keywords:
---


Docker简介
----
* **镜像**
  
  操作系统分为内核空间和用户空间,对于linux系统,内核启动后会挂在root文件系统为其提供用户空间支持;
  Docker镜像就相当于一个root文件系统,除了提供容器运行时所需要的程序,库,资源,配置等文件之外,
  还包含一些为运行时准备的配置参数;
  
  **分层存储**
  
  Docker利用Union FS技术,将文件系统设计为分层存储架构;
  
* **容器**
* **仓库**

Docker基础命令
----
* **获取镜像**

  从Docker Register获取镜像的命令是`docker pull`,命令格式为:
  ```
  docker pull [选项] [Docker Register地址]<仓库名>:<标签>
  ```
  使用`docker pull --help`可以查看详细命令信息,下面是获取ubuntu 14.04的例子:
  ```
  $ docker pull ubuntu:14.04
    14.04:  Pulling from    library/ubuntu
    bf5d46315322:   Pull    complete
    9f13e0ac480c:   Pull    complete
    e8988b5b3097:   Pull    complete
    40af181810e7:   Pull    complete
    e6f7c7e5c03e:   Pull    complete
    Digest: sha256:147913621d9cdea08853f6ba9116c2e27a3ceffecf3b49298
    3ae97c3d643fbbe
    Status: Downloaded  newer   image   for ubuntu:14.04
  ```
