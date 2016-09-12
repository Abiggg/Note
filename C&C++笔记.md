## C/C++

类
----
### 虚类的构造函数和析构函数执行顺序
```c++

class Test {
public:
    Test() {cout << "Test Constructed" << endl;}
    ~Test() {cout << "Test Destructed" << endl;}
};
class Base {
public:
    Base() {cout << "Base Constructed" << endl;}
    virtual ~Base() {cout << "Base Destructed" << endl;}
};
class Derived: public Base
{
public:
    Derived() {cout << "Derived Constructed" << endl;}
    virtual ~Derived() {cout << "Derived Destructed" << endl;}
private:
    Test t;
};

int main(int argc, char const *argv[])
{
    Base *bptr = new Derived();
    delete bptr;
    return 0;
}

输出结果：
Base Constructed
Test Constructed
Derived Constructed
Derived Destructed
Test Destructed
Base Destructed

原因：
delete指向派生类的基类指针构造函数和析构函数的执行顺序如下：
基类构造函数->成员变量的构造函数->自身构造函数
自身析构函数->成员变量析构函数->基类析构函数
```

### 虚函数表的修改
```c++
class animal
{
protected:
    int age;
public:
    virtual void print_age(void) = 0;
};

class dog : public animal
{
public:
       dog() {this -> age = 2;}
       ~dog() { }
       virtual void print_age(void)
       {
           cout<<"Wang, my age = "<<this -> age<<endl;
       }
};

class cat: public animal
{
public:
    cat() {this -> age = 1;};
    ~cat() { }
    virtual void print_age(void)
    {
        cout<<"Miao, my age = "<<this -> age<<endl;
    }
};

int main(void)
{
    cat kitty;
    dog jd;
    animal * pa;
    int * p = (int *)(&kitty);
    int * q = (int *)(&jd);
    p[0] = q[0];
    pa = &kitty;
    pa -> print_age();
    return 0;
}

输出结果：
Wang, my age = 1

原因：
理解虚函数表以及类的存储结构
int * p = (int *)(&kitty)   // p指向kitty
int * q = (int *)(&jd)      // q指向jd
p[0] = q[0]   // 把kitty的指向cat::print_age的指针值，修改成指向了dog::print_age
pa = &kitty   // pa指向kitty
pa->print_age()  // 调用的是刚刚被修改过的函数指针，也就是dog::print_age函数，但是
// 在this->age的这个语句的this是kitty,age也就自然是kitty的1
```

### 类的大小测试
```c++
class A {
public:
    virtual void f() {}
};
// 为了使不同的类具有不一样的地址，编译器回自动给空类加上一个字节
class B {};
class C : public B {
public:
    void f() {}
};
class D: public C, public A {};
class E {
private:
    static int f;
};

class F {
private:
    int a;
};

class G {
public:
    G(){}
    ~G(){}
    void ff() {}
};

int main(int argc, char const *argv[])
{
    cout << "sizeof int*: " << sizeof(int*) << endl;
    cout << "sizeof int: " << sizeof(int) << endl;
    cout << "sizeof A: " << sizeof(A) << endl;
    cout << "sizeof B: " << sizeof(B) << endl;
    cout << "sizeof C: " << sizeof(C) << endl;
    cout << "sizeof D: " << sizeof(D) << endl;
    cout << "sizeof E: " << sizeof(E) << endl;
    cout << "sizeof F: " << sizeof(F) << endl;
    cout << "sizeof G: " << sizeof(G) << endl;
    return 0;
}

输出结果（64位系统）：
sizeof int*: 8
sizeof int: 4
sizeof A: 8
sizeof B: 1
sizeof C: 1
sizeof D: 8
sizeof E: 1
sizeof F: 4
sizeof G: 1
结论：
/*
类的大小：
１．为类的非静态成员数据的类型大小之和．
２．有编译器额外加入的成员变量的大小，用来支持语言的某些特性（如：指向虚函数的指针）．
３．为了优化存取效率，进行的边缘调整．
４　与类中的构造函数，析构函数以及其他的成员函数无关．
*/
```

指针
----
### 数组+1时移动距离
```C++
int main(int argc, char const *argv[])
{
    int a[4] = {1, 2, 3, 4};
    int *ptr = (int*)(&a+1);
    printf("%d\n", *(ptr-1));
    return 0;
}

输出结果：
4

原因：
取标识符a它的地址加1会移动它本身元素个数的长度，
也就是说&a + 1 会向后移动四个位置,如下：
[1][2][3][4][null]
 |  |  |  |   |
 a           &a+1
```

### 指针移动
```c++
#include <iostream>
#include <cstdio>
using namespace std;

int main(int argc, char const *argv[])
{
    char *p[] = {"A", "B", "C"};
    char **pp[] = {p+2, p+1, p};
    char ***ppp = pp;
    printf("%s\n", **++ppp);
    printf("%s\n", *++*++ppp);
    return 0;
}

输出结果：
B
B

原因：
'++'和取值'*'运算的优先级是一样的，所以靠近的先执行；
'**++ppp'的执行顺序是先把ppp向后移动一位，在两次取值，所以输出"B";
'*++*++ppp'的执行顺序是先把ppp向后移动一位，再取值，得到的值是p，
然后对p进行'++'操作得到的是p+1的地址也就是指向字符串"B"

图示如下：
(1):                          (2)++ppp执行之后:     
["A"]["B"]["C"]               ["A"]["B"]["C"]      
  |    |    |                   |    |    |        
 [p0] [p1] [p2]                [p0] [p1] [p2]      
  |                             |                  
  p                             p                  
    [p2][p1][p0]                  [p2][p1][p0]     
     | \                          |     \          
     pp ppp                       pp    ppp        

(3)继续执行++ppp:              (4)最后++ppp执行之后:  
["A"]["B"]["C"]               ["A"]["B"]["C"]      
  |    |    |                   |    |    |        
 [p0] [p1] [p2]                [p0] [p1] [p2]      
  |                             |                  
  p                             p                  
    [p2][p1][p0]                  [p2][p1][p0]     
     |        \                    |        \      
     pp       ppp                  pp       ppp    

```

const关键字
----
### const修饰指针
[Clockwise/Spiral Rule](http://c-faq.com/decl/spiral.anderson.html)

[stackoverflow上的详解](http://stackoverflow.com/questions/1143262/what-is-the-difference-between-const-int-const-int-const-and-int-const)

![](https://raw.githubusercontent.com/zhushh/Note/master/const2.png)

### const修饰类的成员变量及成员函数
* 1.类的成员变量被const修饰时，需要在构造函数初始化列表初始化
```c++
class A {
public:
    A(int a) : age(a) {}
private:
    const int age;
}
```
* 2.类的成员函数被const修饰的时候，不能对类的成员变量进行修改且在函数体中不能调用非const函数
```c++
class A {
public:
    A() {}
    void printAge() { cout << age << endl; }
    int getAge() const {
        age++;    // Error
        printAge();   // Error
        return age;
    }
private:
    int age;
}
```

函数
----
### 函数执行顺序
```c++
#include <stdio.h>
int ff(int a, int b, int c) {
    return 0;
}
int main(int argc, char const *argv[])
{
    return ff(printf("A"), printf("B"), printf("C"));
}

输出结果：
CBA

原因：
函数参数入栈顺序是从右向左，所以先执行打印C，在打印B，最后打印A
```
