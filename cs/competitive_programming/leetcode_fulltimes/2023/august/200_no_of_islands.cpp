#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int rows=0, cols=0;

    void helper(int x, int y, vector<vector <char>> & grid) {
        if((x>=0) && (y>=0) && (x<rows) && (y<cols) && (grid[x][y]=='1')) {
            grid[x][y] = '0';
            helper(x+1, y, grid);
            helper(x, y+1, grid);
            helper(x, y-1, grid);
            helper(x-1, y, grid);
        }
    }
    
    int numIslands(vector<vector<char>>& grid) {

        int res=0;
        rows=grid.size();
        cols=grid[0].size();

        for(int r=0; r<rows; r++) {
            for(int c=0; c<cols; c++) {
                if(grid[r][c]=='1') {
                    res+=1;
                    helper(r, c, grid);
                }
            }
        }

        return res;
    }
};

int main( ) {

    vector<vector <char>> grid;
    vector<char> temp;

    /*
     * [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
     */
    temp.clear();
    temp.push_back('1');
    temp.push_back('1');
    temp.push_back('1');
    temp.push_back('1');
    temp.push_back('0');
    grid.push_back(temp);

    temp.clear();
    temp.push_back('1');
    temp.push_back('1');
    temp.push_back('0');
    temp.push_back('1');
    temp.push_back('0');
    grid.push_back(temp);

    temp.clear();
    temp.push_back('1');
    temp.push_back('1');
    temp.push_back('0');
    temp.push_back('0');
    temp.push_back('0');
    grid.push_back(temp);
    
    temp.clear();
    temp.push_back('0');
    temp.push_back('0');
    temp.push_back('0');
    temp.push_back('0');
    temp.push_back('0');
    grid.push_back(temp);


    Solution obj = Solution();
    cout << "number of islands: " << obj.numIslands(grid) << endl;

   // [['1','1',"0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

    grid.clear();
    
    temp.clear();
    temp.push_back('1');
    temp.push_back('1');
    temp.push_back('0');
    temp.push_back('0');
    temp.push_back('0');
    grid.push_back(temp);

    temp.clear();
    temp.push_back('1');
    temp.push_back('1');
    temp.push_back('0');
    temp.push_back('0');
    temp.push_back('0');
    grid.push_back(temp);

    temp.clear();
    temp.push_back('0');
    temp.push_back('0');
    temp.push_back('1');
    temp.push_back('0');
    temp.push_back('0');
    grid.push_back(temp);
    
    temp.clear();
    temp.push_back('0');
    temp.push_back('0');
    temp.push_back('0');
    temp.push_back('1');
    temp.push_back('1');
    grid.push_back(temp);

    cout << "number of islands: " << obj.numIslands(grid) << endl;
    return 0;
}
