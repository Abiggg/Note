## cplusplus pthread.h

Hello World
----
编译命令为：
```bash
$ gcc pth_hello.c -o pth_hello -lpthread
```
pth_hello.c文件如下：
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

long thread_count;

void* hello(void*);

int main(int argc, char** argv) {
    thread_count = strtol(argv[1], NULL, 10);
    long thread;
    pthread_t *thread_handlers;
    thread_handlers = (pthread_t*)malloc(thread_count*sizeof(pthread_t));

    for (thread = 0; thread < thread_count; thread++) {
        pthread_create(&thread_handlers[thread], NULL, hello, (void*)thread);
    }
    printf("Hello world from main.\n");

    for (thread = 0; thread < thread_count; thread++) {
        pthread_join(thread_handlers[thread], NULL);
    }

    free(thread_handlers);
    return 0;
}

void* hello(void* rank) {
    long my_rank = (long)rank;
    printf("Hello world from thread %ld.\n", my_rank);
    return NULL;
}
```

pthread函数
----
```cpp
pthread_t // 不透明的对象,存储的数据都是系统绑定,用户级无法直接访问里面数据
pthread_create(
    pthread_t*              thread_p,                   /* out */
    const pthread_attr_t*   attr_p,                     /* in */
    void*                   (*start_routine)(void*),    /* in */
    void*                   arg_p                       /* in */
);
pthread_join(
    pthread_t   thread,     /* in */
    void**      ret_val_p   /* out */
);
```

概念词语
----
* 竞争条件(race condition)
```
当多个线程要访问共享变量或共享文件时，如果至少有一个访问是更新操作，那么这些访问就可能会导致某种错误，这种情况就叫竞争条件
```
* 临界区(critical section)
```
一段共享的代码段，每次只允许一个线程进入该代码段
```
* 忙等待
```
1. y = Compute(my_rank);
2. while (flag != my_rank);    // 此处一直检测flag值，处于忙等待状态
3. x = x+y;
4. flag++;
忙等待有可能在编译器开启编译优化的时候可能会失效，比如上面进行编译优化后可能为：
1. y = Compute(my_rank);
2. x = x + y
3. while (flag != my_rank);
4. flag ++
```

pthread计算矩阵乘法
----
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

long thread_count;
int m, n;
double *x;
double *y;
double **A;

void* Pth_mat_vect(void*);

int main(int argc, char** argv) {
    thread_count = strtol(argv[1], NULL, 10);
    long thread;
    pthread_t* thread_handlers;
    thread_handlers = (pthread_t*)malloc(thread_count*sizeof(pthread_t));
    scanf("%d %d", &m, &n);
    x = (double*)malloc(n*sizeof(double));
    y = (double*)malloc(m*sizeof(double));
    A = (double**)malloc(m*sizeof(double*));
    for (int i = 0; i < m; i++) {
        A[i] = (double*)malloc(n*sizeof(double));
        // 读取矩阵行元素
        for (int j = 0; j < n; j++) {
            scanf("%lf", &A[i][j]);
        }
    }
    // 读入向量x
    for (int i = 0; i < n; i++) {
        scanf("%lf", &x[i]);
    }

    for (thread = 0; thread < thread_count; thread++) {
        pthread_create(&thread_handlers[thread], NULL, Pth_mat_vect, (void*)thread);
    }

    for (thread = 0; thread < thread_count; thread++) {
        pthread_join(thread_handlers[thread], NULL);
    }

    printf("The result:\n");
    for (int i = 0; i < m; i++) {
        printf("%lf\n", y[i]);
    }
    free(thread_handlers);
    free(x);
    free(y);
    for (int i = 0; i < m; i++) {
        free(A[i]);
    }
    free(A);
    return 0;
}

void* Pth_mat_vect(void*rank) {
    long my_rank = (long)rank;
    int my_m = m / thread_count;
    int my_first_row = my_m * my_rank;
    int my_last_row = my_m + my_first_row;

    for (int i = my_first_row; i <= my_last_row && i < m; i++) {
        y[i] = 0.0;
        for (int j = 0; j < n; j++) {
            y[i] += A[i][j] * x[j];
        }
    }
    return NULL;
}
```

互斥量
----
```
互斥锁的简称，是一个特殊的变量，可以通过某些特殊类型的函数，互斥量可以用来限制每次只有一个线程能进入临界区。
```

* 函数操作
```cpp
pthread_mutexattr_t // 特殊的类型变量，用来做互斥量
int pthread_mutex_init(
    pthread_mutex_t*            mutex_p,    /* out */
    const pthread_mutexattr_t*  attr_p      /* in */
);
int pthread_mutex_destroy(pthread_mutex_t* mutex_p);
int pthread_mutex_lock(pthread_mutext_t* mutex_p);
int pthread_mutex_unlock(pthread_mutex_t* mutex_p);
```

计算Pi的值例子
----
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

long thread_count;
pthread_mutex_t mutex;
long long n;
double sum;

void* Thread_sum(void*);

int main(int argc, char** argv) {
    thread_count = strtol(argv[1], NULL, 10);
    n = strtol(argv[2], NULL, 10);
    long thread;
    pthread_t* thread_handlers;
    thread_handlers = (pthread_t*)malloc(thread_count*sizeof(pthread_t));
    pthread_mutex_init(&mutex);

    for (thread = 0; thread < thread_count; thread++) {
        pthread_create(&thread_handlers[thread], NULL, Thread_sum, (void*)thread);
    }

    for (thread = 0; thread < thread_count; thread++) {
        pthread_join(thread_handlers[thread], NULL);
    }

    printf("Pi = %lf\n", 4.0*sum);

    pthread_mutex_destroy(&mutex);
    free(thread_handlers);
    return 0;
}

void* Thread_sum(void* rank) {
    long my_rank = (long)rank;
    long long my_n = n / thread_count;
    long long my_first_i = my_n*my_rank;
    long long my_last_i = my_first_i + my_n;
    double factor;
    double local_sum = 0.0;
    if (my_first_i%2 == 0) {
        factor = 1.0;
    } else {
        factor = -1.0;
    }
    for (long long i = my_first_i; i < my_last_i; i++, factor = -factor) {
        local_sum += factor*(2*i+1);
    }
    pthread_mutex_lock(&mutex);
    sum += local_sum;
    pthread_mutex_unlock(&mutex);
    return NULL;
}
```

信号量(semaphore)
----
```
一种特殊类型的unsigned int无符号整型变量，可以赋值为0,1,2,...
它与互斥量最大的区别在于信号量没有个体拥有权，主线程把所有信号量初始化为0，即“加锁”，其他线程都能调用sem_post和sem_wait函数。
```

* 操作函数
```cpp
头文件: #include <semaphore.h>
sem_t // 信号量类型
int sem_init(
    sem_t*      semaphore_p,    /* out */
    int         shared,         /* in */
    unsigned    initial_val     /* in */
);
int sem_destroy(sem_t* semaphore_p  /* in/out */);
int sem_post(sem_t* semaphore_p     /* in/out */);
int sem_wait(sem_t* semaphore_p     /* in/out */);
```

信号量实现线程间消息传递
----
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

void* Send_msg(void*);

const int MSG_MAX = 1024;
long thread_count;
char **message;
sem_t *semaphores;

int main(int argc, char const *argv[])
{
    if (argc != 2) {
        printf("Usage: ./a.out thread_number\n");
        exit(0);
    }
    long thread;
    thread_count = strtol(argv[1], NULL, 10);
    pthread_t* thread_handlers;
    thread_handlers = (pthread_t*)malloc(thread_count*sizeof(pthread_t));
    message = (char**)malloc(thread_count*sizeof(char*));
    semaphores = (sem_t*)malloc(thread_count*sizeof(sem_t));

    // initialize message to NULL and semaphore to 0(locked)
    for (thread = 0; thread < thread_count; thread++) {
        message[thread] = NULL;
        sem_init(&semaphores[thread], 0, 0);
    }

    // create thread
    for (thread = 0; thread < thread_count; thread++) {
        pthread_create(&thread_handlers[thread], NULL, Send_msg, (void*)thread);
    }

    // join thread
    for (thread = 0; thread < thread_count; thread++) {
        pthread_join(thread_handlers[thread], NULL);
    }

    // destroy semaphore
    for (thread = 0; thread < thread_count; thread++) {
        sem_destroy(&semaphores[thread]);
    }

    // free memory
    free(semaphores);
    for (thread = 0; thread < thread_count; thread++) {
        free(message[thread]);
    }
    free(message);
    free(thread_handlers);
    return 0;
}

void* Send_msg(void* rank) {
    long my_rank = (long)rank;
    long dest = (my_rank+1) % thread_count;
    char *my_msg = (char*)malloc(MSG_MAX*sizeof(char));

    sprintf(my_msg, "Hello to %ld from %ld", dest, my_rank);
    message[dest] = my_msg;
    sem_post(&semaphores[dest]);    // unlock semaphores of dest
    sem_wait(&semaphores[my_rank]); // wait for semaphores to be unlocked
    printf("Thread %ld > %s\n", my_rank, message[my_rank]);
    return NULL;
}
```

