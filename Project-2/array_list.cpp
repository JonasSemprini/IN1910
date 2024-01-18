#include <math.h>

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

class ArrayList {
   private:
    int *data;
    int capacity;
    float growth_factor;
    int size;

    void resize() {
        capacity = ceil(growth_factor * capacity);
        int *temp = new int[capacity];
        for (int i = 0; i < size; i++) {
            temp[i] = data[i];
        }
        delete[] data;
        data = temp;
    }

   public:
    ArrayList() {
        size = 0;
        capacity = 1;
        growth_factor = 2;
        data = new int[capacity];
    }
    ArrayList(vector<int> initial) {
        size = 0;
        growth_factor = 2;
        int expo = ceil((size / growth_factor));
        capacity = pow(2, expo);
        data = new int[capacity];
        for (int i : initial) {
            append(i);
        }
    }
    ~ArrayList() {
        delete[] data;
    }
    int &operator[](int i) {  //Use & to change the array
        if ((0 <= i) and (i < size)) {
            return data[i];
        } else {
            throw range_error("Indexerror");
        }
    }
    void append(int n) {
        if (size >= capacity) {
            resize();
        }
        data[size] = n;
        size++;
    }
    void insert(int val, int index) {
        cout << "Insert " << val << " to index " << index << endl;
        int *tmp = new int[capacity];
        for (int i = 0; i < index; i++) {
            tmp[i] = data[i];  // Rewrite new data onto a new array
        }
        tmp[index] = val;  // Rewrite new data onto a given index
        for (int i = index + 1; i <= size; i++) {
            tmp[i] = data[i - 1];
        }
        delete[] data;  // Delete old array
        data = tmp;
        size++;
    }
    void remove(int i) {
        if (i >= 0 && i < size) {
            for (int j = i; j < size - 1; j++) {
                data[j] = data[j + 1];
            }
            size--;
        } else {
            throw out_of_range("Not able to remove elements from without lists bounds");
        }
        if (size / capacity < 0.25) {
            shrink_to_fit();
        }
    }
    int pop(int i) {
        int value = data[i];
        remove(i);
        return value;

        if (size / capacity < 0.25) {
            shrink_to_fit();
        }
    }
    int pop() {
        return pop(size - 1);
    }
    int length() {
        return size;
    }
    void shrink_to_fit() {
        growth_factor = 2;
        int exponent = ceil((size / growth_factor));
        capacity = pow(2, exponent);
        int *tmp = new int[capacity];
        for (int i = 0; i < size; i++) {
            tmp[i] = data[i];
        }
        delete[] data;
        data = tmp;
    }
    int get_cap() {
        return capacity;
    }
    void print() {
        cout << "[";
        if (size > 0) {
            cout << data[0];
        }
        for (int i = 1; i < size; i++) {
            cout << "," << data[i];
        }
        cout << "]" << endl;
    }
};
bool is_prime(int n) {
    if (n == 1) {
        return false;
    }
    for (int d = 2; d < n; d++) {
        if (n % d == 0) {
            return false;
        }
    }
    return true;
}
ArrayList find_n_primes(int n) {
    ArrayList primes;
    int f_primes = 0;
    int i = 2;
    while (f_primes < 10) {
        if (is_prime(i)) {
            primes.append(i);
            f_primes++;
        }
        i++;
    }
    primes.print();
    return primes;
}
void test1() {
    ArrayList example;
    example.append(1);
    example.append(2);
    example.append(3);
    example.append(4);
    example.append(5);
    example.print();
    example.insert(6, 3);
    example.print();
    example.remove(0);
    example.print();
    example.pop(2);
    example.print();
    example.pop();
    example.print();
}
void test_primes() {
    ArrayList my_primes = find_n_primes(10);
    my_primes.print();
    int expected[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    for (int i = 0; i <= 9; i++) {
        if (my_primes[i] != expected[i]) {
            throw "Elements in list are not equivalent";
        }
    }
}
void test_shrink_to_fit() {
    ArrayList my_fibonacci({1, 1, 2, 3, 5, 8});
    if (my_fibonacci.get_cap() != 8) {
        throw range_error("Something went wrong");
    }
    for (int i = 0; i <= 2; i++) {
        my_fibonacci.remove(i);
    }
    my_fibonacci.shrink_to_fit();
    my_fibonacci.print();
    if (my_fibonacci.get_cap() != 4) {
        throw range_error("Something went wrong");
    }
}
int main() {
    test1();
    test_primes();
    test_shrink_to_fit();
}