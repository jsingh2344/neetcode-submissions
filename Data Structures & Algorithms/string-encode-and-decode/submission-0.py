class Solution:

    def encode(self, strs: List[str]) -> str:
        divider = "/" + "#" * 198 + "/"
        output = ""
        for s in strs:
            output += s
            output += divider
        return output

    def decode(self, s: str) -> List[str]:

        divider = "/" + "#" * 198 + "/"
        split_s = s.split(divider)

        return split_s[:-1]
