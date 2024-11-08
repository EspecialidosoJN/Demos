class Solution {
    vector<vector<char>> board;
    int Vlen;
    int Hlen;
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        this->board = board;
        vector<string> answer;
        this->Vlen = board.size();
        this->Hlen = board[0].size();
        int Nwords = words.size();
        int wordLen = 0;
        // cout << Nwords << endl;
        for (int y = 0; y<this->Vlen; y++){
            for(int x = 0; x<this->Hlen; x++){
                for(int Nw = 0; Nw<Nwords; Nw++){
                    wordLen = words[Nw].length()-1;
                    cout << words[Nw] << endl;
                    if(findNextCharacter(words[Nw], wordLen, 0, 5, x, y)){
                        answer.push_back(words[Nw]);
                    }
                    
                }
            }
        }
        return answer;
    }
    bool findNextCharacter(string & word,int wordLen, int currentChar, int sourceDir,int x,int y){ //0 = left, 1 = up, 2 = right, 3 = down
            cout << currentChar << endl;
            cout << word[currentChar] << endl;
        if (word[currentChar] != this->board[y][x]){
            cout << "false because letter different " << endl;
            return false;
        }
        if (currentChar==wordLen){
            return true;
        }
        cout<< "word len: " << wordLen << " current char: " << currentChar << endl;
        bool left = false;
        bool up = false;
        bool right = false;
        bool down = false;
        currentChar++;
        if (sourceDir != 0 && x-1 >= 0){
            left = findNextCharacter(word, wordLen, currentChar, 2, x-1, y);
        }
        if (sourceDir != 1 && y-1 >= 0){
            up = findNextCharacter(word, wordLen, currentChar, 3, x, y-1);
        }
        if (sourceDir != 2 && x+1 < this->Hlen){
            right = findNextCharacter(word, wordLen, currentChar, 0, x+1, y);
        }
        if (sourceDir !=3 && y+1 < this->Vlen){
            down = findNextCharacter(word, wordLen, currentChar, 1, x, y+1);
        }
        cout << left << up << right << down << endl;
        return (left || up) || (right || down);
    }
}; //known issues, this can find repeated words, this can cicle to build a word by repeating a letter if it finds it again during traversal
