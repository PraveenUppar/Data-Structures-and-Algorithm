class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        div_path = path.split("/")  

        # tokenize/split the string based on "/"
        # Eg: "/.../a/../b/c/../d/./" ---> ["...","a","..","b","c","..","d","."]

        for c in div_path:
            if c == "..":
                if stack:
                    stack.pop()
            elif c != "" and c != ".":
                stack.append(c)
        return "/" + "/".join(stack)

        # RULES: 
        # 1. "/" Means root dir and start of the path
        # 2. "." No effect
        # 3. ".." Move to parent dir that is remove elements
        # 4. "/" Path not end with "/"