---
name:
date:
update:
keywords:
---

Java Annotation
----

**什么是注解(Annotation)**

  可以嵌入到Java源代码中的语义元数据;这一机制是在Java 5中引入的;注解可以用来为程序的元素(包括类/方法/成员变量等)加上说明;
  注解与注释不同的是,注解不是用来提供代码功能说明,而是实现程序功能的组成部分;注解经常被基础框架使用,以简化程序的配置;
**注解实现原理**

  注解是一种接口,通过Java的反射机制相关的API来访问Annotation的信息;注解不会影响代码的执行,无论注解怎样变化,代码都始终如一的运行;

**Annotation与Interface的异同**

  (1)Annotation使用@interface而不是interface;这个关键子隐含了一个信息:它是继承了java.lang.annotation.Annotation接口,
  并非声明了一个interface;
  
  
**内嵌的注解**


**自定义的注解**


**参考链接**

[Java annotation - wiki](https://en.wikipedia.org/wiki/Java_annotation)

[Java注解基础理解](http://www.cnblogs.com/mandroid/archive/2011/07/18/2109829.html)
