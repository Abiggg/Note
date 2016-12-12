### Linux环境安装配置java

检查并删掉默认的openjdk
----
以centos环境为例子

查看命令如下：
```shell
$ rpm -qa | grep openjdk | grep -v grep
java-1.7.0-openjdk-1.7.0.75-2.5.4.2.el7_0.x86_64
java-1.6.0-openjdk-devel-1.6.0.34-1.13.6.1.el7_0.x86_64
java-1.7.0-openjdk-headless-1.7.0.75-2.5.4.2.el7_0.x86_64
java-1.6.0-openjdk-1.6.0.34-1.13.6.1.el7_0.x86_64
java-1.7.0-openjdk-devel-1.7.0.75-2.5.4.2.el7_0.x86_64
```

删除命令如下：
```shell
# rpm -e --nodeps java-1.7.0-openjdk-1.7.0.75-2.5.4.2.el7_0.x86_64
# rpm -e --nodeps java-1.6.0-openjdk-devel-1.6.0.34-1.13.6.1.el7_0.x86_64
# rpm -e --nodeps java-1.7.0-openjdk-headless-1.7.0.75-2.5.4.2.el7_0.x86_64
# rpm -e --nodeps java-1.6.0-openjdk-1.6.0.34-1.13.6.1.el7_0.x86_64
# rpm -e --nodeps java-1.7.0-openjdk-devel-1.7.0.75-2.5.4.2.el7_0.x86_64
```


下载安装并配置oracle的jdk
----
到官网网址[http://www.oracle.com/technetwork/java/javase/downloads/index.html](http://www.oracle.com/technetwork/java/javase/downloads/index.html)下载jdk-8u51-linux-x64.tar.gz，然后执行下面命令进行解压及安装：
```shell
# tar -zxvf jdk-8u51-linux-x64.tar.gz
# mv jdk1.8.0_51 /usr/java/jdk1.8.0_51
```

配置环境变量
```shell
# echo "export JAVA_HOME=/usr/java/jdk1.8.0_51" >> /etc/profile
# echo -e 'export CLASSPATH=.:$JAVA_HOME/jre/lib/rt.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar'
# echo -e 'export PATH=$PATH:$JAVA_HOME/bin'
```


完整脚本
----
为方便以后配置使用，编写成脚本如下：
```shell
#!/bin/bash

for i in $(rpm -qa | grep openjdk | grep -v grep)
do
	echo "Delete rpm -> "$i
	rpm -e -nodeps $i
done

if [[ ! -z $(rpm -qa | grep openjdk | grep -v grep) ]]; then
	echo "--->Failed to remove openjdk"
else
	if [[ ! -e "jdk-8u51-linux-x64.tar.gz" ]]; then
		wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u51-b16/jdk-8u51-linux-x64.tar.gz"

		echo "Download jdk8 from oracle success."
	fi

	# 解压tar并安装到/usr/java中
	if [[ ! -e /usr/java ]]; then
		mkdir /usr/java
	fi
	tar -zxvf jdk-8u51-linux-x64.tar.gz
	mv jdk1.8.0_51 /usr/java/jdk1.8.0_51

	# 配置java环境变量
	echo "export JAVA_HOME=/usr/java/jdk1.8.0_51" >> /etc/profile
	echo -e 'export CLASSPATH=.:$JAVA_HOME/jre/lib/rt.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar'
	echo -e 'export PATH=$PATH:$JAVA_HOME/bin'

	source /etc/profile
fi
```
