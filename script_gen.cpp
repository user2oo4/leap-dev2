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

bool dwave = 0;
bool findgap = 0;


signed main() {
    // Testing file
    // network_model
    cout << "DWave (0/1) ? " << endl;
    cin >> dwave;
    cout << "findgap (0/1) ? " << endl;
    cin >> findgap;
    network_model.push_back("er");
    // network_model.push_back("ba");
    // network_model.push_back("plt");
    // network_size
    // network_size.push_back(20);
    network_size.push_back(40);
    // network_size.push_back(60);
    // network_size.push_back(80);
    // avg_deg
    avg_deg.push_back(4);
    avg_deg.push_back(6);
    avg_deg.push_back(8);
    avg_deg.push_back(10);
    avg_deg.push_back(12);
    // weight_range
    // weight_range.push_back(16);
    weight_range.push_back(32);
    // weight_range.push_back(64);

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

    // findgap

    // command
    freopen("scripts.sh", "w", stdout);
    cout << "#!/bin/sh" << endl;
    
    if(findgap) for(string test: test_file) {
        string command = "cat parameters.txt " + test + " | " + "python algorithms/findgap.py";
        cout << command << endl;
    }
    
    
    if(dwave) for(string test: test_file) {
        string command = "cat " + test + " | " + "python algorithms/UTC.py";
        cout << command << endl;
    }
    
}