/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        ListNode start = ListNode();
        ListNode* dummy = &start;
        ListNode* ptr1 = list1;
        ListNode* ptr2 = list2;
        ListNode* res = dummy;

        while(ptr1!=nullptr && ptr2!=nullptr) {

            if(ptr1->val < ptr2->val) {
                res->next = ptr1;
                ptr1 = ptr1->next;
            } else {
                res->next = ptr2;
                ptr2 = ptr2->next;
            }

            res = res->next;

        }

        if(ptr1) {
            res->next = ptr1;
        }

        if(ptr2) {
            res->next = ptr2;
        }
        
        return dummy->next;
    }
};
