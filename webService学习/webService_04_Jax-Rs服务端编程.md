---
name: webService_04_Jax-Rs服务端编程.md
date: Fri 13 Jan 2017 01:38:22 PM CST
update: Fri 13 Jan 2017 01:38:22 PM CST
keyword: cxf jax-rs
---

目录
----
* 根资源类

    * @Path
    * @GET,@PUT,@POST,@DELETE,...(HTTP Methods)
    * @Produces
    * @Consumes

* 参数注解(@*Param)
* 子资源
* 根资源的生命周期
* 注入规则
* @Context的使用
* 可编程的资源对象

根资源类(Root Resources Classes)
----

根资源类，至少带有一个@Path的POJOs(Plain Old Java Objects)；
比如下面就是简单的hello world根资源类：
```java
package org.glassfish.jersey.examples.helloworld;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;

@Path("helloworld")
public class HelloWorldResource {
    public static final String CLICHED_MESSAGE = "Hello, World!";

    @GET
    @Produces("text/html")
    public String getHello() {
        return CLICHED_MESSAGE;
    }
}
```

* @Path

    * 最简单的使用
        
        比如上面使用的`@Path("helloworld")`,直接把HelloWorldResource这个类映射到相对URI路径/helloworld

    * URI路径模板

        URI路径模板就是在URI中带有变量，下面大括号里面的`username`就是变量
        ```
        @Path("/users/{username}")
        ```
        如果想要在代码中使用`username`变量，可以像下面使用参数注解把`username`当做参数传进去
        ```java
        @Path("/users/{username}")
        public class UserResource {

            @GET
            @Produces("text/html")
            public String getUser(@PathParam("username") String userName) {
                ...
            }
        }
        ```
    
    * URI正则表达式

        有时候你可能需要对变量进行过滤，这时候就可以使用正则表达式，如下：
        ```
        @Path("/users/{username: [a-zA-Z][a-zA-Z_0-9]*}")
        ```

* HTTP Methods(@GET, @PUT, @POST, @DELETE, ...)

    @GET, @PUT, @POST, @DELETE, @HEAD等通常对应http协议的get, put, post, delete, head等方法；
    比如上面的HelloWorldResource类例子中，`@GET`就是用来处理http的get请求；
    又如，像下面这个例子就是使用@PUT注解来处理http的put请求：
    ```java
    @PUT
    public Response putContainer() {
        System.out.println("PUT CONTAINER " + container);

        URI uri = uriInfo.getAbsolutePath();
        Container c = new Container(container, uri.toString());

        Response r;
        if (!MemoryStore.MS.hasContainer(c)) {
            r = Response.create(uri).build();
        } else {
            r = Response.noContent().build();
        }

        MemoryStore.MS.createContainer(c);
        return r;
    }
    ```
    另外，JAX-RS在运行的时候通常默认会支持HEAD和OPTIONS方法；

* @Produces

    这个注解是用来说明返回给客户端的MIME类型的，例如使用`@Produces("text/plain")`就是返回"text/plain"的格式给客户端；`@Produces`这个注解可以用在类，也可以用在方法上面；比如下面例子：
    ```
    @Path("/myResource")
    @Produces("text/plain")
    public class SomeResource {
        @GET
        public String doGetAsPlainText() {
            ...
        }

        @GET
        @Produces("text/html")
        public String doGetAsHtml() {
            ...
        }
    }
    ```
    @Produces还可以声明多个类型返回，例如：
    ```
    @GET
    @Produces({"application/xml", "application/json"})
    public String doGetAsXmlOrJson() {
        ...
    }
    ```
    此时，如果"application/xml"和"application/json"都支持，那么前面的那种格式会被优先返回；
    如果get请求只接受"application/xml"或"application/json"的一种，那么被接受的那种格式就会被返回；

* @Consumes

    指定处理输入媒体的类型，例如"Content-Type: application/json".如果你的服务中函数带一个自由的参数，规定合适的输入provider，那么使用body中的内容，实例化这个参数。例如：
    ```
    @Post
    @Consumes("text/plain")
    public String sayHello(@PathParam("username") String userName, String letter) {
        return "hello " + userName + ":" + letter;
    }
    ```


参数注解(@*Param)
----

资源方法的参数可以使用参数注解从请求里面提取；
比如像上面使用`@PathParam`提取在`@Path`定义的`username`变量；
又如@QueryParam，这种是从QueryString或者Form中提取变量信息；
另外，还可以使用@DefaultValue 为变量制定默认值，比如下面代码：
```
@GET
@Path("girlfriend")
@Produces("text/html")
public String girlFriend(@PathParam("username") String userName, 
        @DefaultValue("Mary") @QueryParam("name") String name,
        @DefaultValue("123") @QueryParam("id") String id) {
    return "hello " + userName + ": your's gf is " + name;
}
```
参数注解还有很多种，比如从HTTP headers里面提取信息的@HeaderParam；
从cookies里面提取的信息的@CookieParam等；

* @FormParam
    
    从POST表单里面获取参数；比如下面代码：
    ```
    @POST
    @Path("/girlfriend")
    @Produces("text/html")
    public String girlFriendPost(@PathParam("username") String userName,
                    @FormParam("") Customer user ) {
            return "hello " + userName + ": your's gf is " + user.getName();
    }
    ```
    上面代码中会把表单定义成类，让系统自动实例化并填充；

* @BeanParam
    
    这个参数注解可以让我们自己定义类来获取参数信息；比如先定义下面的类：
    ```java
    public class MyBeanParam {
        @PathParam("p")
        private String pathParam;
     
        @MatrixParam("m")
        @Encoded
        @DefaultValue("default")
        private String matrixParam;
     
        @HeaderParam("header")
        private String headerParam;
     
        private String queryParam;
     
        public MyBeanParam(@QueryParam("q") String queryParam) {
            this.queryParam = queryParam;
        }
     
        public String getPathParam() {
            return pathParam;
        }
        ...
    }
    ```
    然后就可以使用下面的代码进行参数获取：
    ```
    @POST
    public void post(@BeanParam MyBeanParam beanParam, String entity) {
        final String pathParam = beanParam.getPathParam(); // contains injected path parameter "p"
        ...
    }
    ```
    在上面的例子中，我们把@PathParam, @QueryParam @MatrixParam 和 @HeaderParam 都集合进一个类里面，
    使用起来会比较灵活，但是不怎么简洁；


子资源(Sub-resources)
----


根资源的生命周期(Life-cycle of Root Resources Classes)
----


注入规则(Rules of Injection)
----


@Context的使用
----


可编程资源对象(Programmatic resource model)
----


参考链接
----

* [https://jersey.java.net/documentation/latest/jaxrs-resources.html](https://jersey.java.net/documentation/latest/jaxrs-resources.html)

* [http://ss.sysu.edu.cn/~pml/webservices/5-jax-rs-std.html](http://ss.sysu.edu.cn/~pml/webservices/5-jax-rs-std.html)
