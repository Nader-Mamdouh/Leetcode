class BrowserHistory {
public:
    stack<string> mainStack;
    stack<string> hisStack;
    
    BrowserHistory(string homepage) {
        mainStack.push(homepage);
    }
    
    void visit(string url) {
        
        while (!hisStack.empty()) {
            hisStack.pop();
        }
        mainStack.push(url);
    }
    
    string back(int steps) {
        while (steps-- && mainStack.size() > 1) {
            hisStack.push(mainStack.top());
            mainStack.pop();
        }
        return mainStack.top();
    }
    
    string forward(int steps) {
        while (steps-- && !hisStack.empty()) {
            mainStack.push(hisStack.top());
            hisStack.pop();
        }
        return mainStack.top();
    }
};