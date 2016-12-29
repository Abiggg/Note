---
name: maven
date: 2016-12-29
keyword: maven
---

## Maven技术学习

Maven 环境安装与配置
----

* 安装前提：

Java环境的配置，并设置有JAVA_HOME环境变量;

* 下载解压安装：

前往[https://maven.apache.org/download.cgi](https://maven.apache.org/download.cgi)，
下载  apache-maven-3.3.9-bin.tar.gz安装包;运行下面命令进行解压：
```
$ tar -zxvf apache-maven-3.3.9-bin.tar.gz
```
移到/usr/local目录：

```
$ sudo mv apache-maven-3.3.9 /usr/local/
```

* 添加命令到环境变量：

编辑/etc/profile文件，添加/修改下面环境变量内容:
```
export M2_HOME=/usr/local/apache-maven
export MAVEN_OPTS="-Xms256m -Xmx512m"
export MAVEN_HOME=/usr/local/apache-maven
export PATH=/usr/local/apache-maven/bin:$PATH
```

* 检验安装成功：

输入下面命令：
```
$ mvn --version
```
看到类似下面的输出则说明安装配置成功：
```
Apache Maven 3.3.9 (bb52d8502b132ec0a5a3f4c09453c07478323dc5; 2015-11-11T00:41:47+08:00)
Maven home: /usr/local/apache-maven
Java version: 1.8.0_51, vendor: Oracle Corporation
Java home: /opt/jdk1.8.0_51/jre
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "4.4.0-57-generic", arch: "amd64", family: "unix"
```
