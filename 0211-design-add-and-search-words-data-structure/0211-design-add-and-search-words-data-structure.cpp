class TrieNode {
public:
    bool isWord;
    TrieNode* children[26];

    TrieNode() {
        isWord = false;
        for (int i = 0; i < 26; i++) {
            children[i] = NULL;
        }
    }
};

class WordDictionary {

private:
    TrieNode* root;

public:
    WordDictionary() { root = new TrieNode(); }

    void addWord(string word) {
        int curr = 0;
        TrieNode* node = root;

        for (char ch : word) {
            if (!node->children[ch - 'a']) {
                node->children[ch - 'a'] = new TrieNode();
            }
            node = node->children[ch - 'a'];
        }

        node->isWord = true;
    }

    bool search(string word) { return searchHelper(word, 0, root); }

    bool searchHelper(string& word, int index, TrieNode* node) {
        if (!node) {
            return false;
        }

        if (index == word.size()) {
            return node->isWord;
        }

        char ch = word[index];

        if (ch != '.') {
            int indx = ch - 'a';

            return searchHelper(word, index + 1, node->children[indx]);
        } else {
            for (int i = 0; i < 26; i++) {
                if (searchHelper(word, index + 1, node->children[i])) {
                    return true;
                }
            }
        }
        return false;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */