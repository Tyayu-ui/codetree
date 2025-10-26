#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, c;
    cin >> a >> b >> c;
    double sum = a+b+c;
    double mean = sum / 3;
    cout << sum << '\n';
    cout << mean << '\n';
    cout << sum - mean << '\n';


    return 0;
}