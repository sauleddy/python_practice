import functools


print(int('10', 2))

int2 = functools.partial(int, base=2)
print(int2('10'))
print(int2('10', base=16))


def draw_person(head, hand, leg, body):
    print(head, hand, leg, body)


func_draw_head = functools.partial(draw_person, hand='little_hands', leg='long_legs', body='no_body')
func_draw_head('big_head')






