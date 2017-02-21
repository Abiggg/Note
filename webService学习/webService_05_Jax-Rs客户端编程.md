---
name: webService_05_Jax-Rs客户端编程.md
date: Fri 13 Jan 2017 04:47:21 PM CST
update: Fri 13 Jan 2017 04:47:21 PM CST
keyword: 
---

目录
----
* RESTful客户端编程
    * Java访问web服务/应用的原理
    * 函数式web服务的ClientAPI
    * 异步访问与服务编排
    * 动态代理（Proxy）

Java访问web服务/应用的原理
----

直接使用java网络编程编写客户端，也可以使用Apache的HttpClient这个类来编写；

* 参考链接

    * [Apache HttpComponents project](http://hc.apache.org/)

    * [Apache HttpClient教程](https://hc.apache.org/httpcomponents-client-ga/tutorial/pdf/httpclient-tutorial.pdf)

    * [Apache HttpCore教程](http://www.cnblogs.com/loveyakamoz/category/311258.html)


函数式web服务的Client API
----

* 统一接口限制

    统一接口限制是为了使 RESTful 架构的web service具有清晰的界限，这样一个客户端（例如浏览器）就可以使
    用相同的接口和任何的服务进行交流；在软件工程中，这是一个非常重要的概念，因为它使得基于web的搜索引擎和服务
    可以统一；它包括下面特征：

        (1) 简单，架构容易理解和维护
        (2) 解耦，随着时间的演变，客户端和服务可以保持向后兼容
    另外需要更多的限制：
        (1) 每一个资源都具有一个URI
        (2) 客户端通过HTTP请求和响应，使用特定的HTTP方法获取资源
        (3) 通过指定媒体类型，可以返回一种或者多种格式的表示
        (4) 内容可以链接到其他的资源
    在JAX-RS client API里，资源是一个封装有URI的`WebTarget`类；这个类可以调用一组基于`WebTarget`的特定
    的HTTP方法；

* 更容易地使用和重复使用JAX-RS artifacts

    带参数的POST请求例子：
    ```java
    Client client = ClientBuilder.newClient();
    WebTarget target = client.target("http://localhost:9998").path("resource");

    Form form = new Form();
    form.param("x", "foo");
    form.param("y", "bar");

    MyJAXBBean bean = 
    target.request(MediaType.APPLICATION_JSON_TYPE)
        .post(Entity.entity(form,MediaType.APPLICATION_FROM_URLENCODED_TYPE),
            MyJAXBBean.class);
    ```
    上面的例子中，首先使用Client实例创建一个WebTarget实例，

* Client API简介
    
    * 开始使用Client API 
    * 创建和配置Client实例
    * 定位web resource
    * 在WebTarget上识别资源
    * 调用Http请求
    * 例子总览

* Java实例和类型表示
    
    * 为新的representation添加支持

* Client传输连接器
* 使用Client 请求和响应过滤
* 关闭链接
* client provider注入
* 使用安全的Client
    
    * Http Authentication支持

异步访问与服务编排
----

动态代理（Proxy）
----
