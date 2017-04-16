

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dict_kv = {tuple(equ): value for equ, value in zip(equations, values)}
        dict_kv_reverse = {
            tuple(
                reversed(equ)): 1.0 /
                                value for equ,
                                          value in zip(
            equations,
            values) if abs(value) > 0.000001}
        dict_kv = dict(list(dict_kv.items()) + list(dict_kv_reverse.items()))
        # print(dict_kv)
        dict_route = {}
        for equ in equations:
            # print(equ[0], equ[1])
            if equ[0] != equ[1]:
                if dict_route.get(equ[0], None) is None:
                    dict_route[equ[0]] = set([equ[1]])
                else:
                    dict_route[equ[0]].add(equ[1])
                if dict_route.get(equ[1], None) is None:
                    dict_route[equ[1]] = set([equ[0]])
                else:
                    dict_route[equ[1]].add(equ[0])
                    # print(dict_route)
        # print(dict_route)
        list_result = []
        for query in queries:
            if query[0] not in dict_route.keys(
            ) or query[1] not in dict_route.keys():
                list_result.append(-1.0)
            elif query[0] == query[1]:
                list_result.append(1.0)
            elif dict_kv.get(tuple(query), None) is not None:
                list_result.append(dict_kv[tuple(query)])
            else:
                ret = self.help(
                    query[0],
                    query[1],
                    [],
                    dict_kv,
                    dict_route)
                if ret is None:
                    list_result.append(-1.0)
                else:
                    list_result.append(ret)

        return list_result

    def help(self, qs, qe, list_pass, dict_kv, dict_route):
        set_this = dict_route.get(qs, None)
        # print(set_this)
        if set_this is None:
            return None
        if qe in set_this:
            return dict_kv.get((qs, qe), None)
        for ch in set_this:
            if ch not in list_pass:
                list_pass.append(ch)
                ret = self.help(ch, qe, list_pass, dict_kv, dict_route)
                if ret is not None:
                    return ret * dict_kv[(qs, ch)]
                list_pass.pop()


mySolution = Solution()
result = mySolution.calcEquation(
    [
        [
            "x1", "x2"], [
                "x2", "x3"], [
                    "x3", "x4"], [
                        "x4", "x5"]], [
                            3.0, 4.0, 5.0, 6.0], [
                                [
                                    "x1", "x5"], [
                                        "x5", "x2"], [
                                            "x2", "x4"], [
                                                "x2", "x2"], [
                                                    "x2", "x9"], [
                                                        "x9", "x9"]])

print(result)

set_test = set(['x1', 'x2'])
print(set_test)
set_test.add('x3')
print(set_test)
