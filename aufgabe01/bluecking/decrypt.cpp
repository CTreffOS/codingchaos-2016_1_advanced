#include <iostream>
#include <algorithm>

using namespace std;

string decrypt(string cipher, string key) {
    string message = "";

    std::transform(cipher.begin(), cipher.end(), cipher.begin(), ::tolower);

    for(int i = 0; i < cipher.size(); i++) {
        int cipherletter = cipher.at(i) - 97;
        int keyletter = key.at(i % key.size()) - 97;
        int newletter = (cipherletter - keyletter) % 26;
        if(newletter < 0) {
            newletter = 26 + newletter;
        }
        message += newletter + 97;
    }

    return message;
}

int main(int argc, char** argv) {

    if(argc < 2) {
        cout << "Usage: ./decrypt <cipher>" << endl;
        exit(1);
    }
    cout << decrypt(argv[1], "chaostreffosnabrueck");
}



