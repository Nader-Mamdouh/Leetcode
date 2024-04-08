#include <vector>
#include <deque>
#include <stack>

using namespace std;

class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int n = students.size();
        deque<int> studentDeque(students.begin(), students.end());
        stack<int> sandwichStack;

        int st1 = 0, st0 = 0, sd1 = 0, sd0 = 0;

        for (int i = 0; i < n; i++) {
            if (students[i] == 0) {
                st0++;
            } else {
                st1++;
            }
        }

        for (int i = 0; i < n; i++) {
            if (sandwiches[i] == 0) {
                sd0++;
            } else {
                sd1++;
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            sandwichStack.push(sandwiches[i]);
        }

        int matched = 0;
        while (!studentDeque.empty()) {
            if (studentDeque.front() == sandwichStack.top()) {
                if (studentDeque.front() == 0) {
                    st0--;
                } else {
                    st1--;
                }
                studentDeque.pop_front();
                sandwichStack.pop();
                matched++;
            } else if (sandwichStack.top() == 0 && st0 == 0) {
                break;
            } else if (sandwichStack.top() == 1 && st1 == 0) {
                break;
            } else {
                int c = studentDeque.front();
                studentDeque.pop_front();
                studentDeque.push_back(c);
            }
        }
        
        return n - matched;
    }
};