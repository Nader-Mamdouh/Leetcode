class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) 
    {
        int n = tickets.size();
        queue<pair<int, int>> q;  

        for (int i = 0; i < n; i++) 
        {
            q.push({ tickets[i], i });
        }

        int time = 0;

        while (!q.empty()) 
        {
            int ticketsLeft = q.front().first;
            int position = q.front().second;
            q.pop();

            if (ticketsLeft > 0) 
            {
                if (position == k && ticketsLeft == 1) 
                {
                    time++; 
                    break;
                }

                time++;  
                q.push({ ticketsLeft - 1, position });
            }
        }

        return time;
        
    }
};