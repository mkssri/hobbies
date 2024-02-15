// program1: accepted in leetcode
class Solution {
public:
    int helper (int l, int r, int target, vector<int>& numbers)
    {
        int m = 0;
        while (l<=r)
        {
            m = l + (r-l)/2;
            if (numbers[m] == target)
            {
                return m+1;
            } else if (numbers[m] > target) 
            {
                r = m-1;
            } else
            {
                l = m+1;
            }
        }

        return -1;
    }
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n           = numbers.size();
        int num1        = 0; 
        int num2        = 0;
        int idx_num2    = 0;
        vector<int> res = {0,0};
        for (int i=0; i<n; i++)
        {
            num1    = numbers[i];
            num2    = target-num1;
            
            if (num2>=num1)
            {
                idx_num2 = helper(i+1, n-1, num2, numbers);
            } else
            {
                continue;
            }

            if (idx_num2 != -1)
            {
                res[0] = i+1;
                res[1] = idx_num2;
                break;
            }

        }
        return res;
    }
};

// program 2: TLE (and leetcode did not accept the solution)
class Solution {
public:
    int helper (int l, int r, int target, vector<int> numbers)
    {
        int m = 0;
        while (l<=r)
        {
            m = l + (r-l)/2;
            if (numbers[m] == target)
            {
                return m+1;
            } else if (numbers[m] > target) 
            {
                r = m-1;
            } else
            {
                l = m+1;
            }
        }

        return -1;
    }
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n           = numbers.size();
        int num1        = 0; 
        int num2        = 0;
        int idx_num2    = 0;
        vector<int> res = {0,0};
        for (int i=0; i<n; i++)
        {
            num1    = numbers[i];
            num2    = target-num1;
            
            if (num2>=num1)
            {
                idx_num2 = helper(i+1, n-1, num2, numbers);
            } else
            {
                continue;
            }

            if (idx_num2 != -1)
            {
                res[0] = i+1;
                res[1] = idx_num2;
                break;
            }

        }
        return res;
    }
};

// question: program1 accepted in leetcode & program2 not accepted in leetcode ? why ?
