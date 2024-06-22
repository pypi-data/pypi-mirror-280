import relationalai as rai
from relationalai.std import rel

model = rai.Model(name=globals().get("name", "test_ordering"), config=globals().get("config"))
A = model.Type("A")
B = model.Type("B")
with model.rule():
    A.add(name="A1").set(x = 0, y = 0)
    A.add(name="A2").set(x = 0, y = 1)
    B.add(name="B1").set(x = 1, y = 1)
    B.add(name="B2").set(x = 1, y = 0)

# calculate distance between each combination of A and B
D = model.Type("D")
with model.rule():
    a = A()
    b = B()
    d = D.add(A = a, B = b)
    dx = a.x - b.x
    dy = a.y - b.y
    distance = rel.sqrt(dx**2 + dy**2)
    d.set(distance = distance)

with model.query() as select:
    d = D()
    res = select(d.A.name, d.B.name, d.distance)
print(res.results)
