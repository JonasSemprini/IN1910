#include <math.h>

#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Node {
    // Struct representing a node in a linked list, with a value, and a pointer to the next node.
    int value;
    Node *next;
    Node *prev;

    Node(int n) {
        // Node constructor with one value argument, used for end of linked list.
        value = n;
        next = nullptr;
        prev = nullptr;
    }

    Node(int n, Node *p) {
        // Node constructor with value and pointer argument.
        value = n;
        next = p;
    }
};

void test_node_chain() {
    Node a(12);
    Node b(33);
    Node c(2);
    a.next = &b;
    b.next = &c;
    //print node chain
    cout << "[";
    int i = 0;
    for (Node *n = &a; n != nullptr; n = n->next, i++) {
        if (i != 0) {
            cout << ", ";
        }
        cout << n->value;
    }
    cout << "]" << endl;
}
class LinkedList {
    Node *head;
    Node *tail;
    int size;

    Node *get_node(int index) {
        if (head == nullptr) {
            throw out_of_range("Index is out of range!");
        } else if (index < 0 or index >= size) {
            throw out_of_range("Index out of range!");
        } else {
            Node *current;
            current = head;
            for (int i = 0; i < index; i++) {
                if (current == nullptr) {
                    throw out_of_range("Index is out of range!");
                }
                current = current->next;
            }
            return current;
        }
    }

   public:
    LinkedList() {
        head = nullptr;
        tail = nullptr;
        size = 0;
    }
    LinkedList(vector<int> vec) {
        size = vec.size();
        tail = new Node(vec[size - 1]);
        Node *next = tail;
        Node *current = tail;
        for (int i = size - 2; i >= 0; i--) {
            current = new Node(vec[i], next);
            next = current;
        }
        head = current;
    }

    int length() {
        return size;
    }
    void append(int val) {
        if (head == nullptr) {
            //List is empty
            head = new Node(val);
            tail = head;
            size++;
            return;
        }
        Node *current = tail;
        current->next = new Node(val);
        tail = current->next;
        size++;
    }
    void print() {
        if (head == nullptr) {
            cout << "[]" << endl;
            return;
        }
        Node *current;
        current = head;
        cout << "[";
        while (current->next != nullptr) {
            cout << current->value << ", ";
            //current->value == current.value
            current = current->next;
        }
        cout << current->value << "]" << endl;
    }
    void push_front(int val) {
        Node *n = new Node(val, head);
        head = n;  //New value, points too head
        size++;
    }

    void insert_middle(int val, int index) {
        Node *prev = get_node(index - 1);
        Node *next = prev->next;
        prev->next = new Node(val, next);
        size++;
    }

    void insert(int val, int index) {
        if ((index < 0) or (index > size)) {
            throw out_of_range("Invalid index");
        }
        if (index == 0) {
            push_front(val);
        } else if (index == size) {
            append(val);
        } else {
            insert_middle(val, index);
        }
    }
    void remove(int i) {
        if (i >= 0 && i < size) {
            if (i == 0) {
                Node *new_head = head->next;
                delete head;
                head = new_head;
            } else {
                Node *prev = get_node(i - 1);
                Node *next = prev->next->next;
                delete prev->next;
                prev->next = next;
            }
            size--;
        }
    }
    int pop(int i) {
        int val = get_node(i)->value;
        remove(i);
        return val;
    }

    int pop() {
        return pop(size - 1);
    }
    int &operator[](int index) {
        if (index >= 0 && index < size) {
            Node *node = get_node(index);
            return node->value;
        } else {
            throw out_of_range("List out of range");
        }  // using ->value to refer to a value, not a pointer
    }

    ~LinkedList() {
        Node *current;
        Node *next;
        current = head;
        while (current->next != nullptr) {
            next = current->next;  //values on hold
            delete current;
            current = next;
        }
    }
};

void test_append() {
    LinkedList list;
    list.append(1);
    list.append(2);
    list.append(3);
    list.append(4);
    list.append(5);
    list.append(6);
    list.print();
    list.insert(9, 4);
    list.print();
    list.insert(420, 0);
    list.print();
    list.remove(2);
    list.print();
    list.pop(1);
    list.pop();
    list.print();
}
void test_vector() {
    LinkedList vec({1, 2, 3, 4, 5});
    vec.append(6);
    vec.insert(23, 3);
    vec.insert(69, 0);
    vec.pop();
    vec.pop(2);
    vec.remove(3);
    vec.print();
}
int main() {
    test_append();
    test_node_chain();
    test_vector();
}
