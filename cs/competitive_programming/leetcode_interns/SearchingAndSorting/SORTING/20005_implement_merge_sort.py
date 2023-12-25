#!/usr/bin/python3


def merge_sort(arr):
    
    if len(arr) > 1:
        
        mid = len(arr)//2
        
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        
        merge_sort(lefthalf)
        merge_sort(righthalf)
        
        
        i,j,k = 0,0,0
        
        while i < len(lefthalf) and j < len(righthalf):
            
            if lefthalf[i] < righthalf[i]:
                arr[k] = lefthalf[i]
                
                i += 1
                
            else:
                arr[k] = righthalf[j]
                j += 1

            k += 1
        
        
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
        
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1
    return arr
            
if __name__ == "__main__":
    
    arr = [11,2,5,4,7,56,2,12,23]
    out = merge_sort(arr)
    print(out)
    
    
https://leetcode.com/problems/merge-k-sorted-lists/

ListNode -> LL

*ptr1 = 10

ptr1(1000) -> 10
              1000

ListNode *ptr2
ListNode *ptr1 = ptr2

int *ptr1 = 10


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 /
class Solution {
public:
    ListNode mergeList(ListNode *head1, ListNode *head2) {
        if(head1 == NULL && head2 == NULL) {
            return NULL;
        }
        if(head1 == NULL) {
            return head2;
        }
        if(head2 == NULL) {
            return head1;
        }
        ListNode *ptr1 = head1, *ptr2 = head2;
        ListNode *newHead = (ptr1->val > ptr2->val)?ptr2:ptr1;
        if(newHead == ptr1)
            ptr1 = ptr1->next;
        else
            ptr2 = ptr2->next;
        ListNode temp = newHead;
        while(ptr1 != NULL && ptr2 != NULL) {
            if(ptr1->val > ptr2->val){
                temp->next = ptr2;
                ptr2 = ptr2->next;
            }
            else {
                temp->next = ptr1;
                ptr1 = ptr1->next;
            }
            temp = temp->next;
        }
        if(ptr1!= NULL) {
            temp->next = ptr1;
        }
        if(ptr2!=NULL)
            temp->next = ptr2;
        
        return newHead;
    }
    ListNode mergeKLists(vector<ListNode*>& lists) {
        if(lists.size() == 0) {
            return NULL;
        }
        ListNode newHead = lists[0];
        int numLists = lists.size();
        int interval = 1;
        while(interval < numLists) {
            for(int i = 0; i < numLists - interval; i += interval2)
                lists[i] = mergeList(lists[i], lists[i+interval]);
            interval = interval * 2;
        }
        return lists[0];
    }
};