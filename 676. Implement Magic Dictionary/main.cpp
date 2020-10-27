#include <string>
#include <set>
#include <vector>
#include <iostream>

using namespace std;

class MagicDictionary {
public:
    set<string> s;
    
    /** Initialize your data structure here. */
    MagicDictionary() {
    }
    
    void buildDict(vector<string> dictionary) {
        for(string x: dictionary) {s.insert(x);cout<<x<<'\n';;}
        
    }
    
    bool search(string searchWord) {
        cout<<searchWord<<'\n';
        for(int i=0;i<searchWord.size();i++){
            auto c=searchWord[i];
            for(int j=0;j<26;j++){
                if(c==j+'a') continue;
                searchWord[i]=j+'a';
                if (s.count(searchWord)) return 1;
            }
            searchWord[i]=c;
        }
        return 0;
    }
};


int main(){
    MagicDictionary m;
    vector<string> v={"aaa", "bbb"};
    m.buildDict(v);
    cout<<m.search("aaa")<<'\n';
    cout<<m.search("aac")<<'\n';
    cout<<m.search("acc")<<'\n';
}
