#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

class Queue {
private:
    Node* front;
    Node* tail;
    int count; 

public:
    Queue() : front(nullptr), tail(nullptr), count(0) {}

    void enqueue(int val) {
        Node* newNode = new Node(val);
        if (tail == nullptr) {
            front = tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
        count++;
    }

    void dequeue() {
        if (front == nullptr) {
            cout << "Queue is empty!" << endl;
            return;
        }
        Node* temp = front;
        front = front->next;
        if (front == nullptr) {
            tail = nullptr;
        }
        delete temp;
        count--;
    }

    int top() {
        if (front == nullptr) {
            cout << "Queue is empty!" << endl;
            return -1;
        }
        return front->data;
    }

    bool isEmpty()
    {
        if (front == nullptr) {
            return true;
        }
        return false;
    }

    int size() {
        return count;
    }

};

int main() {
    Queue q;
    q.enqueue(5);
    q.enqueue(8);
    q.enqueue(11);
    q.enqueue(14);

    cout << "Front element: " << q.top() << endl;
    cout << "Queue size: " << q.size() << endl;

    q.dequeue();
    cout << "Front element after dequeue: " << q.top() << endl;
    cout << "Queue size after dequeue: " << q.size() << endl;

    return 0;
}
