#include<bits/stdc++.h>
using namespace std;

// cat test_name | python code_name


vector<string> network_model;
vector<int> network_size;
vector<int> avg_deg;
vector<int> weight_range;

vector<string> test_file;

vector<int> Ns;
vector<int> Loop;
vector<string> code_file;

vector<string> commands;

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
    // Testing file
    // network_model
    network_model.push_back("er");
    // network_model.push_back("ba");
    // network_model.push_back("plt");
    // network_size
    network_size.push_back(20);
    network_size.push_back(40);
    network_size.push_back(60);
    // network_size.push_back(80);
    // avg_deg
    avg_deg.push_back(4);
    avg_deg.push_back(6);
    avg_deg.push_back(8);
    // weight_range
    weight_range.push_back(16);
    // weight_range.push_back(32);
    weight_range.push_back(64);

    for(string nw_model: network_model) {
        for(int nw_sz: network_size) {
            for(int deg: avg_deg) {
                for(int weight: weight_range) {
                    string test_name = "instances_4/";
                    test_name += nw_model;
                    test_name += ("_" + to_string(nw_sz));
                    test_name += ("_" + to_string(deg));
                    test_name += ("_" + to_string(weight));
                    test_name += ".txt";
                    test_file.push_back(test_name);
                }
            }
        }
    }

    // Ns
    Ns.push_back(50);
    // Ns.push_back(100);
    // Loop
    Loop.push_back(1);
    Loop.push_back(2);
    Loop.push_back(4);
    // Loop.push_back(8);
    // code_file
    for(int n: Ns) {
        for(int loop: Loop) {
            string code = "findgap_versions/findgap";
            code += ("_" + to_string(n));
            code += ("_" + to_string(loop));
            code_file.push_back(code);
        }
    }

    // command
    freopen("scripts.sh", "w", stdout);
    cout << "#!/bin/sh" << endl;
    for(string test: test_file) {
        for(string code: code_file) {
            string command = "cat " + test + " | " + "python " + code + ".py";
            cout << command << endl;
        }
    }
}