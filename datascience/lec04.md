

```python
from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
```

## Arithmetic


```python
2 + 3
```




    5




```python
2 * 3
```




    6




```python
2 ** 3
```




    8




```python
2 * * 3
```


      File "<ipython-input-6-0f343c0fc354>", line 1
        2 * * 3
            ^
    SyntaxError: invalid syntax




```python
10 * 2 ** 3
```


```python
2 + 3 * 4 + 5
```


```python
2 / 3
```


```python
2 / 0
```


```python
2 / 3000
```


```python
2 / 3000000
```


```python
0.6666666666666666 - 0.6666666666666666123456789
```


```python
0.000000000000000123456789
```


```python
0.000000000000000000000000000000000000000000000000000000000000000000000123456789
```


```python
2 ** 0.5
```


```python
2 ** 0.5 * 2 ** 0.5
```


```python
2 ** 0.5 * 2 ** 0.5 - 2
```

## Growth


```python
sept_7 = 4366
aug_7 = 1830
growth_per_month = (sept_7 / aug_7) - 1
growth_per_month
```


```python
sept_7 * (1 + growth_per_month) ** 12
```


```python
fed_budget_2002 = 2370000000000
fed_budget_2012 = 3380000000000
fed_budget_2012 - fed_budget_2002
```


```python
g = (fed_budget_2012 / fed_budget_2002) ** (1/10) - 1
g
```


```python
fed_budget_2002 * (1 + g) ** 16 # Actual 2018 budget: $4.1 trillion
```

## Arrays


```python
make_array(1, 2, 3)
```


```python
make_array(1, 2, 3) * 2
```


```python
a = make_array(1, 2, 3)
```


```python
a + 5
```


```python
a + make_array(10, 100, 1000)
```


```python
a
```


```python
sum(a)
```


```python
max(a)
```


```python
min(a)
```


```python
fed_budget_2002 * (1 + g) ** a
```

## Columns


```python
# From http://www.boxofficemojo.com/alltime/adjusted.htm
movies = Table.read_table('top_movies_2017.csv')
movies
```


```python
movies.column('Gross')
```


```python
adjustment = movies.column('Gross (Adjusted)') / movies.column('Gross')
adjustment
```


```python
movies.with_column('Adjustment', adjustment)
```


```python
movies.with_column('Adjustment', adjustment).scatter('Year', 'Adjustment')
```


```python
movies.column('Year')
```


```python
age = 2017 - movies.column('Year')
movies = movies.with_column('Age', age)
movies
```


```python
movies = movies.with_column('Growth rate', adjustment ** (1 / age) - 1)
movies
```


```python
movies.scatter('Year', 'Growth rate')
```


```python
movies.sort('Age').show(20)
```


```python
movies.sort('Year').show(20)
```


```python
# http://www.boxofficemojo.com/about/adjuster.htm
```
