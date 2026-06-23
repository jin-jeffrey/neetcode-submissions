class Solution:

    def encode(self, strs: List[str]) -> str:
        # need to know length of strs and how to split the array
        length = len(strs)
        return str(length) + "##" + ":;=".join(strs)

    def decode(self, s: str) -> List[str]:
        print(s)
        length, encoded = s.split("##", 1)
        if length == "0":
            return []
        else:
            return encoded.split(":;=")
