#include <iostream>
#include <chrono>

using namespace std;

double harmonic_sum = 0;

double harmonic(int n) {

    if (n == 1) {
        harmonic_sum = 1;
        return harmonic_sum;
    }
    harmonic_sum = harmonic(n - 1) + (1.0 / n);
    return harmonic_sum;
}

pair<double, double> harmonic_with_time(int n) {
    harmonic_sum = 0; 
    
    auto start = chrono::high_resolution_clock::now();

    double result = harmonic(n);
    
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;

    return {result, elapsed.count()};
}

int main() {
    int n;
    cout << "n degerini girin: ";
    cin >> n;

    auto [result, elapsed_time] = harmonic_with_time(n);

    cout << "H_" << n << " = " << result << endl;
    cout << "Gecen sure: " << elapsed_time << " saniye" << endl;

    return 0;
}
