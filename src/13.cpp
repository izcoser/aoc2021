#include <iostream>
#include <string>
#include <set>
using namespace std;
typedef pair<int, int> pint;

pint points[1000];

void fold(pint* arr, int size, int at, char along){
    for(int i = 0; i < size; i++){
        if(arr[i].first > at and along == 'x'){
            arr[i].first = at - (arr[i].first - at);
        }
        else if(arr[i].second > at and along == 'y'){
            arr[i].second = at - (arr[i].second - at);
        }
    }
}

int main(){
    int visible = 0;
    int n = 0;
    string input;
    while(1){
        int x, y;
        cin >> input;
        if (input.find(',') != string::npos){
            x = stoi(input.substr(0, input.find(',')));
            input.erase(0, input.find(',') + 1);
            y = stoi(input);
            points[n++] = pint(x, y);
        }
        else if(input[0] == 'f'){
            cin >> input;
            cin >> input;
            
            int foldAt = stoi(input.substr(2));
            fold(points, n, foldAt, input[0]);
            set<pint> unique_points = set(points, points + n);
            cout << unique_points.size() << endl;

            return 0;
            
        }
        else{
            continue;
        }
    }
    
    return 0;
}
