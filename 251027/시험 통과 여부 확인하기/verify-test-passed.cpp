#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int score;
    cin >> score;
    if (80 <= score)
        cout << "pass";
    else
        cout << 80 - score << " more score";
    return 0;
}