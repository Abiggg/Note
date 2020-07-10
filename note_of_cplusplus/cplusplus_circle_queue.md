

```
constexpr int maxSize = 10; 

// 循环列表是先进出队列
// 插入数据时，tail++,表示列尾加1
// 移出数据时，head++,表头指针前移
// 当为空时，tail == head;
// 当为满时, tail + 1 == head;
// 最多可以存储数据为 maxSize - 1, 这样才能保证满与空有区别

using CircleQueue = struct sCircleQueue {
    int arr[maxSize];
    int tail, head;
    sCircleQueue ()
    {
        arr[maxSize] = {0};
        tail = 0;
        head = 0;
    }
    public:
    bool isFull() // 循环队列，判断满的条件，不然tail 会与head相同
    {
        return ((tail + 1) % 10 == head); 
    }
    bool isEmpty()
    {
        return (tail == head);
    }
    int insertQueue(int i)
    {
        if (isFull()) {
            cout << "current queue is full" << endl;
            return -1;
        }
        arr[tail] = i;
        tail = (tail + 1) % maxSize;
        return 0;        
    }
    int popQueue(int &i)
    {
        if (isEmpty()) {
            cout << "current queue is empty" << endl;
            return -1;
        }
        i = arr[head];
        arr[head] = 0;
        head = (head + 1) % maxSize;
        return 0;
    }
};
```