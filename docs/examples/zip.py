x, *y, z = range(4)
print(x, y, z)
# 0 [1, 2] 3
python_version, file_name, topic, *output = "python3.0 hello.py betterprogramming 1 2 3 4".split()
print(python_version)
print(file_name)
print(topic)
print(output)
# python3.0
# hello.py
# betterprogramming
# ['1', '2', '3', '4']
a, b, c, *d = range(7)
print(b, d)
# 1 [3, 4, 5, 6]
