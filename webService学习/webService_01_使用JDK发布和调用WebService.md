---
name: webService学习.md
date: Tue 10 Jan 2017 03:06:32 PM CST
update: Tue 10 Jan 2017 03:06:32 PM CST
keyword: web service cxf apache-cxf
---


使用JDK发布WebSerivce
----

* 第一步： 创建项目

    使用下面命令创建HelloService项目
    ```
    $ mkdir -p HelloService/demo/ws/soap_jdk
    ```

* 第二步：编写接口服务

    编写HelloService.java接口服务，保存文件到HelloService/demo/ws/soap_jdk/HelloService.java
    ```java
    package demo.ws.soap_jdk;

    import javax.jws.WebService;

    @WebService
    public interface HelloService {
        String say(String name);
    }
    ```

* 第三步：实现接口

    实现服务接口，保存下面代码到HelloService/demo/ws/soap_jdk/HelloServiceImpl.java
    ```java
    package demo.ws.soap_jdk;

    import javax.jws.WebService;

    @WebService(
        serviceName = "HelloService",
        portName = "HelloServicePort",
        endpointInterface = "demo.ws.soap_jdk.HelloService"
    )
    public class HelloServiceImpl implements HelloService {
        public String say(String name) {
            return "Hello, " + name;
        }
    }
    ```

* 第四步：编写发布WebService的Server类

    为发布web service，我们实现下面的Server类，保存代码到HelloService/demo/ws/soap_jdk/Server.java
    ```java
    package demo.ws.soap_jdk;

    import javax.xml.ws.Endpoint;

    public class Server {
        public static void main(String[] args) {
            String address = "http://localhost:8080/ws/soap/hello";
            HelloService helloService = new HelloServiceImpl();

            Endpoint.publish(address, helloService);
            System.out.println("ws is published.");
        }
    }
    ```

* 第五步：编译运行

    在目录HelloService下，使用下面命令进行编译运行
    ```
    javac demo/ws/soap_jdk/Server.java
    java demo.ws.soap_jdk.Server
    ```
    此时终端会输出`ws is published.`，然后打开浏览器输入网址
    [http://localhost:8080/ws/soap/hello?wsdl](http://localhost:8080/ws/soap/hello?wsdl)，
    就可以看到输出的xml文件内容；

* 参考阅读链接

    [https://my.oschina.net/huangyong/blog/286155](https://my.oschina.net/huangyong/blog/286155)


通过动态代理类调用WS
----

先使用JDK发布web service，然后执行下面命令创建项目HelloServiceDynamicClient
```
$ mkdir -p HelloServiceDynamicClient/demo/ws/soap_jdk
```

* 第一步： 编写动态代理DynamicClient类调用WS
    
    ```java
    package demo.ws.soap_jdk;

    import java.net.URL;
    import javax.xml.namespace.QName;
    import javax.xml.ws.Service;

    public class DynamicClient {

        public static void main(String[] args) {
            try {
                URL wsdl = new URL("http://localhost:8080/ws/soap/hello?wsdl");
                QName serviceName = new QName("http://soap_jdk.ws.demo/", "HelloService");
                QName portName = new QName("http://soap_jdk.ws.demo/", "HelloServicePort");
                Service service = Service.create(wsdl, serviceName);

                HelloService helloService = service.getPort(portName, HelloService.class);
                String result = helloService.say("world");
                System.out.println(result);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
    ```

* 第二步： 编译运行

    文件保存到demo/ws/soap_jdk/DynamicClient.java，编译运行在项目HelloServiceDynamicClient目录下，执行
    ```
    $ javac demo.ws.soap_jdk.DynamicClient.java
    $ java demo.ws.soap_jdk.DynamicClient
    ```
    可以看到下面的输出内容
    ```
    Hello, World
    ```
