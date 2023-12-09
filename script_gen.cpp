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

signed main() {
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