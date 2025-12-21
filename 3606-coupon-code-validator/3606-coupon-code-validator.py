import re
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
        line_order = {line: idx for idx, line in enumerate(valid_lines)}
        
        valid_coupons = []
        
        for c, b, active in zip(code, businessLine, isActive):
            if not active:
                continue
            if b not in line_order:
                continue
            if not c or not re.fullmatch(r"[A-Za-z0-9_]+", c):
                continue    
            valid_coupons.append((b, c))
        
        valid_coupons.sort(key=lambda x: (line_order[x[0]], x[1]))
        return [c for _, c in valid_coupons]
