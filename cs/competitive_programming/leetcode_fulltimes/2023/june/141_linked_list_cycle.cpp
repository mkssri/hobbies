/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// Procedure 1:

#include <set>

class Solution {
public:
    bool hasCycle(ListNode *head) {

        ListNode* ptr = head;
        std::set<ListNode*> ptr_set;

        for(; ptr!=nullptr; ptr=ptr->next) {

            auto it = ptr_set.find(ptr);

            // ptr present in the set
            if(it!=ptr_set.end()){
                return true;
            } else {
                ptr_set.insert(ptr);
            }
        }

        return false;
    }
};

// Procedure 2:

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {

        if(head==nullptr || head->next==nullptr) {
            return false;
        }

        ListNode* s = head; //slow ptr
        ListNode* f = head->next; // fast ptr

        for(; (f!=nullptr && f->next!=nullptr && f!=s) ; s=s->next, f=f->next->next) {
            ;
        }

        if(s==f)
            return true;
        else
            return false;

    }
};
