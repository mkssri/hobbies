class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        res = set()

        for e in emails:

            extract = e.split('@')
            local_name = extract[0]
            domain_name = extract[1]

            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".", "")

            res.add(local_name+"@"+domain_name)

        return len(res)
