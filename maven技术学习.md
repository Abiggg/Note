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

Maven 入门例子
----

* 创建项目

    使用下面命令创建项目
    ```
    $ mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
    ```
    第一次运行需要等一会下载一些东西，在完成下载后会自动配置插件到环境中。
    然后你会看到在当前目录下会创建一个my-app的项目目录;`cd my-app`进入项目目录,目录结构如下：
    ```
    my-app
    |-- pom.xml
    `-- src
        |-- main
        |   `-- java
        |       `-- com
        |           `-- mycompany
        |               `-- app
        |                   `-- App.java
        `-- test
            `-- java
                `-- com
                    `-- mycompany
                        `-- app
                            `-- AppTest.java
    ```
    src/main/java目录包含的是项目源代码
    src/test/java目录包含的是项目的测试代码
    pom.xml文件是Project Object Model（POM）

* POM介绍

    POM是工程对象模型，是指文件pom.xml，这个文件是maven项目配置的核心。包含了关于工程和各种配置细节的信息，Maven 使用这些信息构建工程。
    所有的项目都只有一个POM文件，文件最少需要包含groupId， artifactId， version三个信息;其中，

        groupId：描述的是项目名称，由于有的项目并不是一个jar包构成的，而是由很多的jar包组成的。因此这个groupId就是整个项目的名称

        artifactId:描述的是包的名称

        version:描述包的版本号

    详细信息参考[https://maven.apache.org/pom.html](https://maven.apache.org/pom.html)


* 编译打包项目

    在目录my-app下运行下面命令
    ```
    $ mvn package
    ```
    会看到项目的编译过程，最后输出会有下面信息：
    ```
    ...
    [INFO] 
    [INFO] --- maven-jar-plugin:2.4:jar (default-jar) @ my-app ---
    [INFO] Building jar: /home/zhushh/Rick/mavenRepository/my-app/target/my-app-1.0-SNAPSHOT.jar
    [INFO] ------------------------------------------------------------------------
    [INFO] BUILD SUCCESS
    [INFO] ------------------------------------------------------------------------
    [INFO] Total time: 4.613 s
    [INFO] Finished at: 2016-12-29T16:16:55+08:00
    [INFO] Final Memory: 21M/331M
    [INFO] ------------------------------------------------------------------------
    ```

* 检验是否成功生成目标包
    ```
    $ java -cp target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App 
    ```
    看到输出Hello World， 成功运行第一个maven例子，更多详细使用参考链接[https://maven.apache.org/guides/getting-started/index.html](https://maven.apache.org/guides/getting-started/index.html)
