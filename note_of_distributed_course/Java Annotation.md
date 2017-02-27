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

    **(1) Annotation使用@interface而不是interface**
    
    这个关键子隐含了一个信息:它是继承了java.lang.annotation.Annotation接口,并非声明了一个interface;
    
    **(2) 注解的方法/类型是独特受限制的**
    
    注解类型的方法必须是无参数和无异常抛出的;
    
    注解的方法名定义了annotation的成员名: 方法名=成员名;
    
    方法的返回值=成员类型;另外,方法的返回值只能是primitive类型/class类型/枚举类型/annotation类型/以前面几种类型为元素的数组类型;
    
    方法的后面可以使用default声明默认值;(null不能作为默认值)
    
    **(3) 注解与Interface相似之处**
    
    他们可以定义常量/静态成员类型;他们也都可以被实现和继承;
  
**内嵌的注解**

    **(1) Override**
  
    java.lang.Override是一个marker annotation类型,被用作标注方法;
  
    说明被标注的方法重载了父类的方法,起到一个断言的作用;如果使用了这个annotation的方法没有重载父类的方法时,
    java编译器会产生一个编译错误来警示(可以保障父类包含有这个方法,防止写错方法名等错误);
  
    **(2) Deprecated**
  
    **(3) SuppressWarnings**

**自定义的注解**


**参考链接**

[Java annotation - wiki](https://en.wikipedia.org/wiki/Java_annotation)

[Java注解基础理解](http://www.cnblogs.com/mandroid/archive/2011/07/18/2109829.html)
