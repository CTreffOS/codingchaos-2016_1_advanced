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

        long max = -1;
        char c;

        for (char i = 0; i < futures.size(); i++)
        {
            long time = futures.at(i).get();
            if (time > max)
            {
                max = time;
                c = (char) (i + 65);
            }
        }

        cout << c << flush;
        password.push_back(c);

        futures.clear();
    }
}