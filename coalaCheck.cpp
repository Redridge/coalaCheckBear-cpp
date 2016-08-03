#include <iostream>
#include <string>
#include <regex>

#include "json.hpp"

using json = nlohmann::json;
using namespace std;

json in;
json out;
string origin;

void init_results(string bear_name) {
    origin = bear_name;
    out["results"] = json::array({});
}

void add_result(string message, int line, int column, int severity) {
    json result = {
        {"origin", origin},
        {"message", message},
            {"affected_code", json::array({{
                {"file", in["filename"]},
                {"start", {
                    {"column", column},
                    {"file", in["filename"]},
                    {"line", line}
                }},
                {"end", {
                    {"column", column+6},
                    {"file", in["filename"]},
                    {"line", line}
                }}
            }})},
        {"severity", severity}
    };
    out["results"] += result;
}

int main() {

    cin >> in;

    init_results("coalaCheckBear");
    
    int i = 0;
    for (auto it=in["file"].begin(); it !=in["file"].end(); it++) {
        i++;
        string line = *it;
        size_t found = line.find("Coala");
        while (found != string::npos) {
            add_result("Did you mean 'coala'?", i, found, 2);
             found = line.find("Coala", found+1);
        }
    }

    cout << out;

    return 0;
}
