class MagicDictionary {
public:
    set<string> s;
    
    /** Initialize your data structure here. */
    MagicDictionary() {
    }
    
    void buildDict(vector<string> dictionary) {
        for(string x: dictionary) {s.insert(x);cout<<x;}
        
    }
    
    bool search(string searchWord) {
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

