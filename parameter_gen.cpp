#include<bits/stdc++.h>
using namespace std;
/*
DEF_D: float = 0.01
DEF_SIGMA: float = 0.1
DEF_BETA: float = 0.01
DEF_NS: int = 50 # can change this to 10, 20, 50
DEF_LOOP: int = 4
DEF_PASS: float = 4 * (1.0 / (DEF_SIGMA * DEF_SIGMA)) * math.log(1.0 / DEF_BETA)

DEF_LB: float = 0.002
DEF_UB: float = 0.1
DEF_BS_RUNS: int = 15

DEF_STEP: float = 0.032
DEF_TRIES: int = 10
DEF_SPLIT: int = 4
DEF_ROUNDING: float = 0.1*/

string parameters[] = {"DEF_D", "DEF_SIGMA", "DEF_BETA", "DEF_NS", "DEF_LOOP", "DEF_PASS", "DEF_LB",
                        "DEF_UB", "DEF_BS_RUNS", "DEF_STEP", "DEF_TRIES", "DEF_SPLIT", "DEF_ROUNDING"};

signed main() {
    // Enter parameters
    ofstream out;
    out.open("parameters.txt");
    string input;
    cout << "Enter parameters: " << endl;
    for(int i = 0 ; i < 13 ; i++) {
        cout << parameters[i] << " = " << endl;
        getline(cin, input);
        if(input == "") out << "default" << endl;
        else out << input << endl;
    }
    out.close();
}