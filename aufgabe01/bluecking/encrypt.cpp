#include <iostream>
#include <algorithm>

using namespace std;

string encrypt(string message, string key) {
    string cipher = "";

    std::transform(message.begin(), message.end(), message.begin(), ::tolower);

    for(int i = 0; i < message.size(); i++) {
        int cipherletter = message.at(i) - 97;
        int keyletter = key.at(i % key.size()) - 97;
        int newletter = (cipherletter + keyletter) % 26;
        cipher += newletter + 97;
    }

    return cipher;
}

int main(int argc, char** argv) {

    if(argc < 2) {
        cout << "Usage: ./decrypt <message>" << endl;
        exit(1);
    }

    cout << encrypt(argv[1], "chaostreffosnabrueck");
}



