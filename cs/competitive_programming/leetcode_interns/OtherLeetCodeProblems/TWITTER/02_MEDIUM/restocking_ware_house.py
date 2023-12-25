#!/usr/bin/python3

# https://1o24bbs.com/t/topic/12945


class Solution():

    def method1(self, item_count, target):
        
        count = 0

        for x in item_count:
            
            if count < target:
                count += x
            else:
                break

        print("count - {}".format(count))
        # if count < target:
        #     return target-count
        # else:
        #     return count-target

        return abs(count-target)




obj1 = Solution()

item_count, target = [10, 20, 30, 40, 15], 80

out = obj1.method1(item_count, target)
print(out)


item_count, target = [10, 20, 30, 40, 15], 130

out = obj1.method1(item_count, target)
print(out)

