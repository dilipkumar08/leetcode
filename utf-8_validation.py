import re
class Solution:
    def __init__(self):
        L = ["0b(0|1[01]{0,6})",
            "0b110.....(0b10......)",
            "0b1110....(0b10......){2}",
            "0b11110...(0b10......){3}" ]
        regexp = "(" + \
            ("|".join(L)) + \
            ")+" 
        self.R = re.compile(regexp)
        
    def validUtf8(self, data: List[int]) -> bool:
        return bool(re.fullmatch(self.R, "".join(map(bin, data))))
