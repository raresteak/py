

```python
from datascience import *
import numpy as np
```

## Table methods

##### Table method review
* t.select(column, ...) or t.drop(column, ...)
* t.take([row, ..]) or t.exclude([row, ...])
* t.sort(column, descending=False,  distinct=False)
* t.where(column, are.condition(...))
* t.apply(function, column, ...) applies a function to a column. one arg function, one column.   two arg function you need two columns, etc.
* t.group([column, ...]) or t.group([column, ...], function)
* t. join(column, otherTable, otherTableColumn)

** http://data8.org/datascience/tables.html



```python
# Discussion Question
# Generaate a table with one row per cafe that has the name oand discounted price 
# of it's cheapiscounted drink.
```


```python
drinks = Table(['Drink', 'Cafe', 'Price']).with_rows([
    ['Milk Tea', 'Tea One', 4],
    ['Espresso', 'Nefeli',  2],
    ['Coffee',    'Nefeli', 3],
    ['Espresso', "Abe's",   2]
])
drinks
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Drink</th> <th>Cafe</th> <th>Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Milk Tea</td> <td>Tea One</td> <td>4    </td>
        </tr>
    </tbody>
        <tr>
            <td>Espresso</td> <td>Nefeli </td> <td>2    </td>
        </tr>
    </tbody>
        <tr>
            <td>Coffee  </td> <td>Nefeli </td> <td>3    </td>
        </tr>
    </tbody>
        <tr>
            <td>Espresso</td> <td>Abe's  </td> <td>2    </td>
        </tr>
    </tbody>
</table>




```python
discounts = Table().with_columns(
    'Coupon % off', make_array(5, 50, 25),
    'Location', make_array('Tea One', 'Nefeli', 'Tea One')
)
discounts
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Coupon % off</th> <th>Location</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>5           </td> <td>Tea One </td>
        </tr>
    </tbody>
        <tr>
            <td>50          </td> <td>Nefeli  </td>
        </tr>
    </tbody>
        <tr>
            <td>25          </td> <td>Tea One </td>
        </tr>
    </tbody>
</table>




```python
# Step 1:
drinks.join('Cafe', discounts, 'Location')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Cafe</th> <th>Drink</th> <th>Price</th> <th>Coupon % off</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Nefeli </td> <td>Espresso</td> <td>2    </td> <td>50          </td>
        </tr>
    </tbody>
        <tr>
            <td>Nefeli </td> <td>Coffee  </td> <td>3    </td> <td>50          </td>
        </tr>
    </tbody>
        <tr>
            <td>Tea One</td> <td>Milk Tea</td> <td>4    </td> <td>5           </td>
        </tr>
    </tbody>
        <tr>
            <td>Tea One</td> <td>Milk Tea</td> <td>4    </td> <td>25          </td>
        </tr>
    </tbody>
</table>




```python
# Step 2, compute discounted price, and drop unneeed columns
a = drinks.join('Cafe', discounts, 'Location')
a = a.with_column('Discounted Price', a.column(2) * (1 - a.column(3)/100) )
a = a.drop(2, 3)
a
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Cafe</th> <th>Drink</th> <th>Discounted Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Nefeli </td> <td>Espresso</td> <td>1               </td>
        </tr>
    </tbody>
        <tr>
            <td>Nefeli </td> <td>Coffee  </td> <td>1.5             </td>
        </tr>
    </tbody>
        <tr>
            <td>Tea One</td> <td>Milk Tea</td> <td>3.8             </td>
        </tr>
    </tbody>
        <tr>
            <td>Tea One</td> <td>Milk Tea</td> <td>3               </td>
        </tr>
    </tbody>
</table>




```python
a.sort('Discounted Price').sort('Cafe') # Now we need to see cheapest price and one per cafe.
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Cafe</th> <th>Drink</th> <th>Discounted Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Nefeli </td> <td>Espresso</td> <td>1               </td>
        </tr>
    </tbody>
        <tr>
            <td>Nefeli </td> <td>Coffee  </td> <td>1.5             </td>
        </tr>
    </tbody>
        <tr>
            <td>Tea One</td> <td>Milk Tea</td> <td>3               </td>
        </tr>
    </tbody>
        <tr>
            <td>Tea One</td> <td>Milk Tea</td> <td>3.8             </td>
        </tr>
    </tbody>
</table>




```python
# next
a.sort('Discounted Price').sort('Cafe', distinct=True) # Correct, Espresso is cheaper
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Cafe</th> <th>Drink</th> <th>Discounted Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Nefeli </td> <td>Espresso</td> <td>1               </td>
        </tr>
    </tbody>
        <tr>
            <td>Tea One</td> <td>Milk Tea</td> <td>3               </td>
        </tr>
    </tbody>
</table>




```python
print(a.group('Cafe', min))
print("")
print(a.group('Cafe', list)) # Incorrect, Coffee is first alphabetically and 
# has the wrong price because of how we sorted, see with list.  Expresso is 3 or 1.5 with 50% coupon


```

    Cafe    | Drink min | Discounted Price min
    Nefeli  | Coffee    | 1
    Tea One | Milk Tea  | 3
    
    Cafe    | Drink list              | Discounted Price list
    Nefeli  | ['Espresso' 'Coffee']   | [1.  1.5]
    Tea One | ['Milk Tea' 'Milk Tea'] | [3.8 3. ]


## Spring 2016 Midterm, Question 2(b)

* Each row of the trip table below describes a single bicycle rental in the San Francisco area.
* Durations are integers representing times in seconds.
* The first three rows out of 338343 appear below.
* Write a Python expresion be each of the following decriptions that computes its value.  The first one is provided for you.   You may use up to two lines and introduce variables. 
* *The average durage of a rental:
* * total_duration = sum(trip.column(2))
* * total_duration / trip.num_rows


```python
total_duration = sum(trip.column(2))

```


```python
total_duration / trip.num_rows
```




    550.001433456581




```python
trip = Table.read_table('trip.csv').where('Duration', are.below(1800)).select(3, 6, 1).relabeled(0, 'Start').relabeled(1, 'End')
trip.show(3)
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Start</th> <th>End</th> <th>Duration</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Harry Bridges Plaza (Ferry Building)</td> <td>San Francisco Caltrain (Townsend at 4th)</td> <td>765     </td>
        </tr>
    </tbody>
        <tr>
            <td>San Antonio Shopping Center         </td> <td>Mountain View City Hall                 </td> <td>1036    </td>
        </tr>
    </tbody>
        <tr>
            <td>Post at Kearny                      </td> <td>2nd at South Park                       </td> <td>307     </td>
        </tr>
    </tbody>
</table>
<p>... (338340 rows omitted)</p>



```python
# Question: Computethe name of the station where the most rentals ended (assume no ties).
trip.group('End').sort('count', descending=True).column(0).item(0)
```




    'San Francisco Caltrain (Townsend at 4th)'




```python
# Questiono: Compute the number of stations for which the average duration ending 
# at that station was more than 10 minutes.
trip.group('End', np.average).where(2, are.above(10*60)).num_rows
```




    21



## Advanced Where

**Please run all cells before this cell, including the previous example cells and the import cell at the top of the notebook.**


```python
3 > 2
```




    True




```python
1 > 2
```




    False




```python
np.arange(5) > 2
```




    array([False, False, False,  True,  True])




```python
# the array contains, 0,1,2,3,4 only 3,4 are greater than 2 thus the True value there.
```


```python
# As of Jan 2017, this census file is online here: 
# http://www2.census.gov/programs-surveys/popest/datasets/2010-2015/national/asrh/nc-est2015-agesex-res.csv

full_census_table = Table.read_table('nc-est2015-agesex-res.csv')
partial = full_census_table.select('SEX', 'AGE', 'POPESTIMATE2010', 'POPESTIMATE2015')
us_pop = partial.relabeled(2, '2010').relabeled(3, '2015')
us_pop
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2010</th> <th>2015</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0   </td> <td>0   </td> <td>3951330</td> <td>3978038</td>
        </tr>
    </tbody>
        <tr>
            <td>0   </td> <td>1   </td> <td>3957888</td> <td>3968564</td>
        </tr>
    </tbody>
        <tr>
            <td>0   </td> <td>2   </td> <td>4090862</td> <td>3966583</td>
        </tr>
    </tbody>
        <tr>
            <td>0   </td> <td>3   </td> <td>4111920</td> <td>3974061</td>
        </tr>
    </tbody>
        <tr>
            <td>0   </td> <td>4   </td> <td>4077551</td> <td>4020035</td>
        </tr>
    </tbody>
        <tr>
            <td>0   </td> <td>5   </td> <td>4064653</td> <td>4018158</td>
        </tr>
    </tbody>
        <tr>
            <td>0   </td> <td>6   </td> <td>4073013</td> <td>4019207</td>
        </tr>
    </tbody>
        <tr>
            <td>0   </td> <td>7   </td> <td>4043046</td> <td>4148360</td>
        </tr>
    </tbody>
        <tr>
            <td>0   </td> <td>8   </td> <td>4025604</td> <td>4167887</td>
        </tr>
    </tbody>
        <tr>
            <td>0   </td> <td>9   </td> <td>4125415</td> <td>4133564</td>
        </tr>
    </tbody>
</table>
<p>... (296 rows omitted)</p>




```python
us_pop.where('AGE', 70)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2010</th> <th>2015</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0   </td> <td>70  </td> <td>2062577</td> <td>2492490</td>
        </tr>
    </tbody>
        <tr>
            <td>1   </td> <td>70  </td> <td>954073 </td> <td>1162672</td>
        </tr>
    </tbody>
        <tr>
            <td>2   </td> <td>70  </td> <td>1108504</td> <td>1329818</td>
        </tr>
    </tbody>
</table>




```python
us_pop.where('AGE', 70).where([False, True, True])
# this illustrates that if you don't want row 0, set to false, row 1 and 2 are true.
# kind of impractical to do this but illustrates how an array can be used with where
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2010</th> <th>2015</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1   </td> <td>70  </td> <td>954073 </td> <td>1162672</td>
        </tr>
    </tbody>
        <tr>
            <td>2   </td> <td>70  </td> <td>1108504</td> <td>1329818</td>
        </tr>
    </tbody>
</table>




```python
seventy = us_pop.where('AGE', 70)
seventy.column('2010') < 2000000
```




    array([False,  True,  True])




```python
seventy.where(seventy.column('2010') < 2000000)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2010</th> <th>2015</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1   </td> <td>70  </td> <td>954073 </td> <td>1162672</td>
        </tr>
    </tbody>
        <tr>
            <td>2   </td> <td>70  </td> <td>1108504</td> <td>1329818</td>
        </tr>
    </tbody>
</table>




```python
us_pop.column('2015') / us_pop.column('2010') > 1.5
```




    array([False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False,  True,  True,
           False,  True,  True,  True,  True, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False])




```python
us_pop.where(us_pop.column('2015') / us_pop.column('2010') > 1.5)
# taking that same ratio from above and putting it in a where now shows which rows are True.
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2010</th> <th>2015</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1   </td> <td>94  </td> <td>43827</td> <td>68135</td>
        </tr>
    </tbody>
        <tr>
            <td>1   </td> <td>95  </td> <td>31736</td> <td>48015</td>
        </tr>
    </tbody>
        <tr>
            <td>1   </td> <td>97  </td> <td>14775</td> <td>23092</td>
        </tr>
    </tbody>
        <tr>
            <td>1   </td> <td>98  </td> <td>9505 </td> <td>14719</td>
        </tr>
    </tbody>
        <tr>
            <td>1   </td> <td>99  </td> <td>6104 </td> <td>9577 </td>
        </tr>
    </tbody>
        <tr>
            <td>1   </td> <td>100 </td> <td>9352 </td> <td>15088</td>
        </tr>
    </tbody>
</table>




```python
trip.show(3)
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Start</th> <th>End</th> <th>Duration</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Harry Bridges Plaza (Ferry Building)</td> <td>San Francisco Caltrain (Townsend at 4th)</td> <td>765     </td>
        </tr>
    </tbody>
        <tr>
            <td>San Antonio Shopping Center         </td> <td>Mountain View City Hall                 </td> <td>1036    </td>
        </tr>
    </tbody>
        <tr>
            <td>Post at Kearny                      </td> <td>2nd at South Park                       </td> <td>307     </td>
        </tr>
    </tbody>
</table>
<p>... (338340 rows omitted)</p>



```python
# The average duration of all trips
np.average(trip.column('Duration'))
```




    550.001433456581




```python
trip.where(trip.column('Start') == trip.column('End')).num_rows
# number of trips starting and stopping at same place
```




    4987




```python
# The average duration of trips that started and ended at the same station
np.average(trip.where(trip.column('Start') == trip.column('End')).column('Duration'))
```




    758.612993783838




```python
trip.where(trip.column('Start') != trip.column('End')).num_rows
# number of trips NOT starting and stopping at same place
```




    333356




```python
# The average duration of trips that started and ended at different stations
np.average(trip.where(trip.column('Start') != trip.column('End')).column('Duration'))
```




    546.880608118648


