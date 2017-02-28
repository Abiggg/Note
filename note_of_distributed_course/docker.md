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
    Docker Register地址: 地址格式是`<域名/IP>[:端口号]`,默认地址是Docker Hub;
    
    仓库名: 仓库名使用两段式名称,既`<用户名>/<软件名>`;对于Docker Hub,如果不给出用户名,默认为library;
    
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

* **运行**

    有了镜像后,就可以使用`docker run`命令运行;以上面ubuntu:14.04为例:
    ```
    $ docker run -it --rm ubuntu:14.04 bash
    root@e7009c6ce357:/# cat /etc/os-release
    NAME="Ubuntu"
    VERSION="14.04.5    LTS,    Trusty  Tahr"
    ID=ubuntu
    ID_LIKE=debian
    PRETTY_NAME="Ubuntu 14.04.5 LTS"
    VERSION_ID="14.04"
    HOME_URL="http://www.ubuntu.com/"
    SUPPORT_URL="http://help.ubuntu.com/"
    BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
    root@e7009c6ce357:/# exit
    exit
    ```
    `-it`参数是两个参数,`-i`表示交互操作,`-t`是终端,因为我们打算进入`bash`,所以需要交互式终端;
    
    `--rm`参数的意思是,在容器运行结束的时候自动将其删除;
    
    `ubuntu:14.04`就是上面我们pull下来的镜像,这里就是使用这个镜像作为基础来运行容器;
    
    `bash`参数放在`ubuntu:14.04`镜像参数后面,是一个命令;
    
    运行容器后,我们便在镜像中启动了bash命令,然后输入了`cat /etc/os-release`和`exit`两个命令;

    另外,如果我们想启动某一服务的容器时,可以像这样执行:
    ```
    $ docker run --name webservice -d -p 81:80 nginx
    ```
    这条命令是指，用ｎｇｉｎｘ镜像运行一个容器，容器命名为ｗｅｂｓｅｒｖｉｃｅ，并且映射８０端口，这样我们就可以使用浏览器去访问这个ｎｇｉｎｘ服务器；
    
    `--name webservice`: 命名容器为webservice;
    
    `-d`: 后台运行;
    
    `-p 81:80`: 81是指当前系统端口,80是指nginx镜像的端口,也就是把81端口映射到镜像的80端口;然后就可以通过浏览器localhost:81访问nginx服务;
    
    
    **列出所有的容器**
    ```
    $ docker ps -a
    ```
    
    **列出正在运行的容器**
    ```
    $ docker ps
    ```

    **停止正在运行的容器**
    ```
    $ docker stop <container-name>
    ```
    例如,停止上面的webservice容器就是:
    ```
    $ docker stop webservice
    ```
    
    **启动已终止的容器**    
    ```
    $ docker start <container-name>
    ```
    例如,如果上面的webservice容器被停止了,那么浏览器就无法访问http://localhost地址,现在重启webservice容器:
    ```
    $ docker start webservice
    ```
    
    **进入容器**
    ```
    $ docker attach <container-name>
    ```
    例如,先启动一个后台运行的ubuntu:
    ```
    $ docker run -idt ubuntu:14.04
    ```
    然后,我们可以使用`docker ps`查看一下它的容器名:
    ```
    $ docker ps
    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                         NAMES
    61bc61919df0        ubuntu:14.04        "/bin/bash"              5 seconds ago       Up 4 seconds                                      objective_raman
    960c831d71eb        nginx               "nginx -g 'daemon ..."   2 hours ago         Up 5 minutes        0.0.0.0:80->80/tcp, 443/tcp   webservice
    ```
    上面的`objective_raman`容器名就是刚刚创建的(你的可能跟我展示的不一样);然后在使用`docker attach`命令进入容器:
    ```
    $ docker attach objective_raman
    root@61bc61919df0:/#
    ```
    这样就进去容器了;
    
* **列出镜像**
 
    想要列出已经下载下来的镜像,可以使用`docker images`命令:
    ```
    $ docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    ubuntu              14.04               7c09e61e9035        17 hours ago        188 MB
    ```
    列出的列表包含: 仓库名, 标签, 镜像ID, 创建时间, 大小;
    
    **虚悬镜像(dangling image)**
    
    这类镜像没有仓库名,也没有标签;可以使用下面命令专门显示虚悬镜像:
    ```
    $ docker images -f dangling=true
    ```
    虚悬镜像一般没有什么价值,可以使用下面命令删除掉:
    ```
    $ docker rmi $(docker images -q -f dangling=true)
    ```
    
    **中间层镜像**
    
    为了加速镜像构建和重复利用资源,Docker会利用中间层镜像;可以使用下面命令查看中间层镜像:
    ```
    $ docker images -a
    ```
    
    **列出部分镜像**
    
    不加任何参数,`docker images`会列出所有的顶级镜像;我们也可以只列出我们希望看到的镜像;例如:
    
    根据仓库名列出镜像或指定仓库名和标签
    ```
    $ docker images ubuntu
    $ docker images ubuntu:14.04
    ```
    
    使用`--filter`(简写是`-f`)进行过滤,例如列出`mongo:3.2`之后建立的镜像:
    ```
    $ docker images since=mongo:3.2
    ```
    若想看某个镜像之前的镜像,就把`since`换成`before`即可;
    如果镜像构建的时候定义了label,那么可以使用label进行过滤:
    ```
    $ docker images -f label=com.example.version=0.1
    ...
    ```
    
    使用`-q`参数只列出镜像的ID:
    ```
    $ docker images -q
    ```
    比较常用的组合就是`--filter`和`-q`;
    
    列出镜像ID和仓库名:
    ```
    $ docker images --format "{{.ID}}: {{.Repository}}"
    5f515359c7f8:   redis
    05a60462f8ba:   nginx
    fe9198c04d62:   mongo
    00285df0df87:   <none>
    f753707788c5:   ubuntu
    f753707788c5:   ubuntu
    1e0c3dd64ccd:   ubuntu
    ```
