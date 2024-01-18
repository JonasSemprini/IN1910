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
class CircLinkedList {
    Node *head;
    Node *tail;
    int size;

    Node *get_node(int index) {
        if (head == nullptr) {
            throw out_of_range("Index is out of range!");
        } else {
            Node *current;
            current = head;
            for (int i = 0; i < index; i++) {
                current = current->next;
            }
            return current;
        }
    }

   public:
    CircLinkedList() {
        head = nullptr;
        tail = nullptr;
        size = 0;
    }
    CircLinkedList(int n) {
        size = 0;
        head = nullptr;
        tail = nullptr;
        for (int i = 1; i < n + 1; i++) {
            append(i);
        }
    }

    void append(int val) {
        if (head == nullptr) {
            head = new Node(val);
            head->next = head;
            tail = head;
            size++;
            return;
        }
        Node *current;
        current = head;
        while (current->next != head) {
            current = current->next;
        }

        // Link new node to end of list
        current->next = new Node(val);
        current->next->prev = current;
        current->next->next = head;
        tail = current->next;
        size++;
    }
    int length() {
        return size;
    }
    void print() {
        if (head == nullptr) {
            cout << "[]" << endl;
            return;
        }
        Node *current;
        current = head;
        cout << "[";
        while (current->next != head) {
            cout << current->value << ", ";
            //current->value == current.value
            current = current->next;
        }
        cout << current->value << "]" << endl;
    }

    int &operator[](int index) {
        Node *node = get_node(index);
        return node->value;
    }

    vector<int> josephus_sequence(int k) {
        vector<int> sekvens;
        Node *current = head;
        int i = 1;
        while (size > 0) {
            while (i < k) {
                current = current->next;
                i++;
            }
            sekvens.push_back(current->value);
            if (current == head) {
                tail->next = head->next;
                head = current->next;
                head->prev = head;

            } else if (current == tail) {
                current->prev->next = current->next;
                tail = current->prev;

            } else {
                current->prev->next = current->next;
                current->next->prev = current->prev;
            }

            size--;
            i = 0;
            print();
        }
        return sekvens;
    }

    ~CircLinkedList() {
        Node *current;
        Node *next;
        current = head;
        while (current->next != head) {
            next = current->next;  //values on hold
            delete current;
            current = next;
        }
    }
};

int last_man_standing(int n, int k) {
    CircLinkedList my_list(n);
    vector<int> sekvens = my_list.josephus_sequence(k);
    return sekvens.back();
}
int main() {
    cout << last_man_standing(68, 7) << endl;
}