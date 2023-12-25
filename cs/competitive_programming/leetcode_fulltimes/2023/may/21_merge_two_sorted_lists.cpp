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

        ListNode* dummy_node = new ListNode();
        ListNode* res = dummy_node;


        while(list1!=nullptr && list2!=nullptr) {

            if(list1->val<=list2->val){
                dummy_node->next = list1;
                list1=list1->next;
            } else {
                dummy_node->next = list2;
                list2=list2->next;
            }
            dummy_node = dummy_node->next;
        }
        if(list1){
            dummy_node->next = list1;
        }
        if(list2){
            dummy_node->next = list2;
        }
        return res->next;
        
    }
};
