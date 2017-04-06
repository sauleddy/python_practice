from collections import deque

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack_num = deque()
        stack_char = deque()
        str_result = ''
        str_this = ''
        for idx in range(len(s)):
            if s[idx] == '[':
                stack_num.append(int(str_this))
                stack_char.append(s[idx])
                str_this = ''
                continue
            if s[idx].isdigit():
                if not str_this.isdigit() and len(str_this) > 0:
                    stack_char.append(str_this)
                    str_this = ''
            if s[idx] == ']':
                if len(str_this) > 0:
                    stack_char.append(str_this)
                    str_this = ''
                print(stack_num)
                print(stack_char)
                num = stack_num.pop()
                string_this = ''
                while stack_char[len(stack_char) - 1] != '[':
                    char_pop = stack_char.pop()
                    string_this = char_pop + string_this
                stack_char.pop()
                string_this = string_this * num
                if len(stack_num) == 0:
                    str_result += string_this
                else:
                    stack_char.append(string_this)
            else:
                str_this += s[idx]
        str_result += str_this
        print(str_result)


mySolution = Solution()
# mySolution.decodeString('3[a2[c]]')
mySolution.decodeString('2[abc]3[cd]ef')
# mySolution.decodeString('3[a]2[bc]')


