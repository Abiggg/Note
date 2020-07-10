#include <iostream>

using namespace std;

constexpr int maxSize = 10; 

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
    bool isFull()
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

int main()
{
    cout << "hello world" << endl;
    CircleQueue q;
    for (int i = 1; i < maxSize; i++) {
        q.insertQueue(i);
    }
    int out = 0;
    for (int i = 1; i < maxSize; i++) {
        q.popQueue(out);
        cout << out << endl;
    }

    for (int i = 0; i < maxSize; i++) {
        q.insertQueue(i);
    }
    return 0;
}