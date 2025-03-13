#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Stack {
private:
    Node* head;     
    int num;        
    int capacity;   

public:
    Stack(int initialCapacity) {  
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }
    void push(int x) {
        if(num>=capacity-1) {
            cout<<"Stack is full!"<<endl;
            return;
        }
        else{
            Node* newNode = new Node();
            newNode->data = x;
            newNode->next = head;
            head = newNode;
            num++;
        }
    }

    int pop() {
        if(num<0) {
            cout<<"Stack is empty!"<<endl;
            return -1;
        }
        else{
            Node* temp = head;
            head = head->next;
            int val = temp->data;
            delete temp;
            num--;
            return val;
        }
    }
    int peek() {
        if(num<0) {
            cout<<"Stack is empty!"<<endl;
            return -1;
        }
        else{
            return head->data;
        }
    }

    bool isEmpty() {
        return num < 0;
    }

    void increaseCapacity() {
        capacity*=2;
        cout << "Capacity increased to: " << capacity<< endl;

    }

    bool deleteElement(int val) {
        Node* current = head;
        Node* prev = nullptr;
        
        while (current != nullptr) {
            if (current->data == val) {
                if (prev == nullptr) { 
                    head = current->next;
                } else {
                    prev->next = current->next;
                }
                delete current;
                num--;
                return true;
            }
            prev = current;
            current = current->next;
        }
        cout << "Element not found!\n";
        return false;
    }
};

int main() {
    Stack stack(3);
    stack.push(5);
    stack.push(10);
    stack.push(15);
    stack.push(20);


    cout << "Top element: " << stack.peek() << endl;
    cout<< "Popped: "<<stack.pop()<<endl;
    stack.deleteElement(10);
    cout<< "Popped: "<<stack.pop()<<endl;
    


    return 0;
}
