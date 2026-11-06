class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        vector<int> g(gain.size() + 1);
        g[0] = 0;
        for(int i = 1 ; i<g.size();i++){
            g[i] = g[i-1] + gain[i-1];
        }
        int largest = 0;
        for( int i = 0; i < g.size();i++){
            if (g[i] >= largest){
            largest = g[i];
            }
        }
        return largest;
    }
};