One liner printing a List of tuples

```
myListOfTuples=[('a','b','c'),('d','e','f')]
```

```
print myListOfTuples
```

[('a', 'b', 'c'), ('d', 'e', 'f')]

```
print('\n'.join(str(x) for x in myListOfTuples))
```

('a', 'b', 'c')

('d', 'e', 'f')
