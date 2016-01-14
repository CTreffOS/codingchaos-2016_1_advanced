#include <iostream>
#include <future>
#include <vector>

using namespace std;
using namespace std::chrono;

long checkPassword(string pass)
{
    string command = "./crypto " + string(pass);

    milliseconds begin = duration_cast<milliseconds>(system_clock::now().time_since_epoch());
    int returnCode = system(command.c_str());
    long time = (duration_cast<milliseconds>(system_clock::now().time_since_epoch()) - begin).count();

    if (returnCode == 0)
    {
        cout << pass.at(pass.size() - 1) << endl;
        exit(0);
    }

    return time;
}

int main()
{
    vector<future<long> > futures;
    string password = "";

    while (true)
    {
        for (char i = 'A'; i <= 'Z'; i++)
        {
            futures.push_back(async(checkPassword, password + i));
        }

        for (char i = 0; i < futures.size(); i++)
        {
            long rc = futures.at(i).get();
            if (rc > (password.size() + 1) * 100)
            {
                cout << (char) (i + 65) << flush;
                password.push_back((char) (i + 65));
                break;
            }
        }

        futures.clear();
    }
}