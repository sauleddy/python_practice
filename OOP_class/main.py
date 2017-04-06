import Calculate.op_base
import Calculate.add
import Calculate.sub

obj_add = Calculate.add.Add(30, 100)
print(obj_add.calculate())

# print(Calculate.op_base.OpBase.name)
# print(Calculate.add.Add.name)
# print(obj_add.name)

Calculate.op_base.OpBase.name = 'static variable'

# print(Calculate.op_base.OpBase.name)
# print(Calculate.add.Add.name)
# print(obj_add.name)

obj_sub = Calculate.sub.Sub(300, 100)
print(obj_sub.calculate())

# print(obj_add.inner_func())

# print(obj_add._Add__num1)

