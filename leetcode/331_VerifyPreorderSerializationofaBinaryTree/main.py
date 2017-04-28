class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        list_str = preorder.split(',')
        len_list_str = len(list_str)
        list_stack = []
        for idx in range(len_list_str-1, -1, -1):
            if list_str[idx] == '#':
                list_stack.append(list_str[idx])
            elif len(list_stack) >= 2:
                if list_stack[len(list_stack)-1] == '#' and list_stack[len(list_stack)-2] == '#':
                    list_stack.pop()
                else:
                    return False
            else:
                return False
        if len(list_stack) == 1 and list_stack[0] == '#':
            return True
        else:
            return False

str_test = '1,#,2,#'
list_test = str_test.split(',')
print(list_test)
