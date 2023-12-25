#!/usr/bin/python3

from ipaddress import ip_address, IPv6Address

"""
Standard method but not valid solution now
"""
class Solution0(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        
        try:
            return "IPv6" if type(ip_address(IP)) is IPv6Address else "IPv4"
        except ValueError:
            return "Neither"

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        
        if "." in IP:
            IP = IP.split(".")
            ans = self.ipv4Check(IP)
        elif ":" in IP:
            
            ipv6_addr_bits = ['a','b','c','d','e','f'] + ['A', 'B', 'C', 'D', 'E', 'F']
        
            for t in range(0,10):
                ipv6_addr_bits.append(str(t)) 
                
            print("ENTER IPv6")
            IP = IP.split(":")
            ans = self.ipv6Check(IP, ipv6_addr_bits)
        else:
            return "Neither"
        return ans


                
    def ipv4Check(self, IP):
        
        if len(IP) != 4:
            return "Neither" 

        for x in IP:
            
            try:
                if x[0] == "0" and len(x) > 1:
                    return "Neither" 
            except:
                return "Neither"  
            try:
                x = int(x)
                
                if x >=0 and x <=255:
                    continue
                else:
                    return "Neither"            

            except:
                return "Neither"
        
        return "IPv4"
    
    
    def ipv6Check(self, IP, ipv6_addr_bits):
        
           
        print("len(IP) = {}".format(len(IP)))
        if len(IP) != 8:
            return "Neither" 

        for x in IP:
            
            print("x = {}".format(x))
            print("len(x) = {}".format(len(x)))
            
            if len(x) < 1  or len(x) > 4:
                return "Neither"
            
            for y in x:
                print("y = {}".format(y))
                if y in ipv6_addr_bits:
                    continue
                else:
                    return "Neither"
        
        return "IPv6"

"""
Time Complexity - O(N) 
Space Complexity - O(1)
"""   
class Solution1:
    def validate_IPv4(self, IP: str) -> str:
        nums = IP.split('.')
        for x in nums:
            # Validate integer in range (0, 255):
            # 1. length of chunk is between 1 and 3
            if len(x) == 0 or len(x) > 3:
                return "Neither"
            # 2. no extra leading zeros
            # 3. only digits are allowed
            # 4. less than 255
            if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
                return "Neither"
        return "IPv4"
    
    def validate_IPv6(self, IP: str) -> str:
        nums = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        for x in nums:
            # Validate hexadecimal in range (0, 2**16):
            # 1. at least one and not more than 4 hexdigits in one chunk
            # 2. only hexdigits are allowed: 0-9, a-f, A-F
            if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                return "Neither"
        return "IPv6"
        
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            return self.validate_IPv4(IP)
        elif IP.count(':') == 7:
            return self.validate_IPv6(IP)
        else:
            return "Neither"

if __name__ == "__main__":
    
    # obj = Solution()
    obj = Solution1()

    """
    IPv4
    """
    # # IP = "172.16.254.1"
    # IP = "256.256.256.256"
    # IP = "1e1.4.5.6"
    # IP = "12..33.4"
    # IP = "" 
    # IP = "192.0.0.1"
    """
    IPv6
    """
    # IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
    
    out = obj.validIPAddress(IP)
    print(out)
    
