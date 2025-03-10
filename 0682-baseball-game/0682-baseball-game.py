class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = []
        
        for op in operations:
            if op == "C":
                record.pop()
            elif op == "D":
                record.append(2*record[-1])
            elif op == "+":
                record.append(record[-2]+record[-1])
            else:
                record.append(int(op))
        return sum(record)
        