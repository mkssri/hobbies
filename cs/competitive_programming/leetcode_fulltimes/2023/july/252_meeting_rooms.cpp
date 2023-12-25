class Solution {
    public: bool canAttendMeetings(vector < vector < int >> & intervals) {

            int si = intervals.size();

            // sort intervals in ascending order based on start time using comparator's
            std::sort( intervals.begin(), intervals.end(), [](std::vector<int> &a, std::vector<int> &b) {
                return a[0] < b[0];
            });


            for(int idx = 0; idx < si-1; idx++) {
                if(intervals[idx][1] > intervals[idx+1][0])
                    return false;
            } 

            return true;

    }
};
