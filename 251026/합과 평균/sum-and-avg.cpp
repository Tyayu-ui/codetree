#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b = 0;
    cin >> a >> b;
    int sum = a+b;
    double mean = (double)sum / 2;
    cout << fixed;
    cout.precision(1);
    cout << sum << " " << mean;
    return 0;
}