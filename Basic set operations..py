my_set=set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
print(my_set)
your_set={1,2,3,5}
your_set.discard(5)
your_set.add(4)
print(your_set)
if my_set.issubset(your_set):
    print(f"{my_set} is a subset of {your_set}")
else:
    print(f"{my_set} is not a subset of {your_set}")
if your_set.issuperset(my_set):
    print(f"{your_set} is a superset of {my_set}.")
else:
    print(f"{your_set} is not a superset of {my_set}.")
if not your_set.isdisjoint(my_set):
    print(f"{your_set} is not a disjoint of {my_set}.")
union=my_set|your_set
print(f"The union of {your_set} and {my_set} is {union}.")
interscshn=my_set&your_set
print(f"The intersection of {your_set} and {my_set} is {interscshn}.")
sm_diff=my_set^your_set
print(f"The symetric difference of {your_set} and {my_set} is {sm_diff}.")
