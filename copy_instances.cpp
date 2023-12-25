// used to copy input instances and change the format
#include<bits/stdc++.h>
using namespace std;
vector<string> Graphs;
vector<int> Ns;
vector<int> Degs;
vector<int> Weights;
string input;

int N;
vector<string> vt(string s) {
    string tmp = "";
    vector<string> res;
    for(int i = 0 ; i < s.length() ; i++) {
        if(s[i] == ' ') {
            res.push_back(tmp);
            tmp = "";
        }
        else tmp += s[i];
    }
    res.push_back(tmp);
    return res;
}

signed main() {
    Graphs.push_back("er");
    for(int i = 40 ; i <= 40 ; i += 20) Ns.push_back(i);
    for(int i = 4 ; i <= 12 ; i += 2) Degs.push_back(i);
    for(int i = 32 ; i <= 32 ; i *= 2) Weights.push_back(i);
    for(string graph: Graphs) {
        for(int n: Ns) {
            for(int deg: Degs) {
                for(int weight: Weights) {
                    string iname = "instances_4/" + graph + "_" + to_string(n) + "_" + to_string(deg) + "_" + to_string(weight) + ".txt";
                    string oname = "../piqmc-chainstrength-main/data/" + iname;
                    cout << "iname = " << iname << endl;
                    cout << "oname = " << oname << endl;
                    ofstream out;
                    ifstream inp;
                    out.open(oname);
                    //freopen(oname.c_str(), "w", stdout);
                    inp.open(iname);
                    inp >> input;
                    inp >> N;
                    cout << "input = " << input << endl;
                    cout << "N = " << N << endl;
                    cout << "n = " << n << endl;
                    assert(N == n);
                    for(int i = 0 ; i < n ; i++) {
                        int x;
                        inp >> x;
                        out << i + 1 << ' ' << i + 1 << ' ' << x << '\n'; 
                    }
                    while(getline(inp, input)) {
                        cout << "input = " << input << endl;
                        vector<string> ss = vt(input);
                        if(ss.size() < 3) continue;
                        int u = stoi(ss[0]);
                        int v = stoi(ss[1]);
                        int w = stoi(ss[2]);
                        out << u + 1 << ' ' << v + 1 << ' ' << w << '\n';
                    }
                }
            }
        }
    }
}