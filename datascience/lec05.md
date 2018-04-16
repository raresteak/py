

```python
from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
```

## Strings


```python
'I love tennis'
```




    'I love tennis'




```python
'2.3'
```




    '2.3'




```python
'2.3' + 4
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-19-844384295a7d> in <module>()
    ----> 1 '2.3' + 4
    

    TypeError: must be str, not int



```python
'2.3' * 4
```




    '2.32.32.32.3'




```python
'be' + 'happy'
```




    'behappy'




```python
str(2.3)
```




    '2.3'




```python
int('2.3')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-23-60c0fa88ab20> in <module>()
    ----> 1 int('2.3')
    

    ValueError: invalid literal for int() with base 10: '2.3'



```python
float('2.3')
```




    2.3




```python
int('23') + float('2.3')
```




    25.3




```python
x = 12
```


```python
int(str(x) + '0')
```




    120



<br><br><br><br><br><br><br><br><br><br><br><br>

## Minard's map


```python
minard = Table.read_table('minard.csv')
```


```python
minard
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th> <th>City</th> <th>Direction</th> <th>Survivors</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td> <td>Smolensk   </td> <td>Advance  </td> <td>145000   </td>
        </tr>
    </tbody>
        <tr>
            <td>33.2     </td> <td>54.9    </td> <td>Dorogobouge</td> <td>Advance  </td> <td>140000   </td>
        </tr>
    </tbody>
        <tr>
            <td>34.4     </td> <td>55.5    </td> <td>Chjat      </td> <td>Advance  </td> <td>127100   </td>
        </tr>
    </tbody>
        <tr>
            <td>37.6     </td> <td>55.8    </td> <td>Moscou     </td> <td>Advance  </td> <td>100000   </td>
        </tr>
    </tbody>
        <tr>
            <td>34.3     </td> <td>55.2    </td> <td>Wixma      </td> <td>Retreat  </td> <td>55000    </td>
        </tr>
    </tbody>
        <tr>
            <td>32       </td> <td>54.6    </td> <td>Smolensk   </td> <td>Retreat  </td> <td>24000    </td>
        </tr>
    </tbody>
        <tr>
            <td>30.4     </td> <td>54.4    </td> <td>Orscha     </td> <td>Retreat  </td> <td>20000    </td>
        </tr>
    </tbody>
        <tr>
            <td>26.8     </td> <td>54.3    </td> <td>Moiodexno  </td> <td>Retreat  </td> <td>12000    </td>
        </tr>
    </tbody>
</table>




```python
minard.num_columns
```




    5




```python
minard.num_rows
```




    8




```python
minard.labels
```




    ('Longitude', 'Latitude', 'City', 'Direction', 'Survivors')




```python
minard.column('Survivors')
```




    array([145000, 140000, 127100, 100000,  55000,  24000,  20000,  12000])




```python
minard.column(4)
```




    array([145000, 140000, 127100, 100000,  55000,  24000,  20000,  12000])




```python
initial_size = minard.column('Survivors').item(0)
```


```python
initial_size
```




    145000




```python
percentage_surviving = minard.column('Survivors')/initial_size
```


```python
percentage_surviving
```




    array([1.        , 0.96551724, 0.87655172, 0.68965517, 0.37931034,
           0.16551724, 0.13793103, 0.08275862])




```python
with_percentages = minard.with_column('Percent Surviving', percentage_surviving)
```


```python
with_percentages
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th> <th>City</th> <th>Direction</th> <th>Survivors</th> <th>Percent Surviving</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td> <td>Smolensk   </td> <td>Advance  </td> <td>145000   </td> <td>1                </td>
        </tr>
    </tbody>
        <tr>
            <td>33.2     </td> <td>54.9    </td> <td>Dorogobouge</td> <td>Advance  </td> <td>140000   </td> <td>0.965517         </td>
        </tr>
    </tbody>
        <tr>
            <td>34.4     </td> <td>55.5    </td> <td>Chjat      </td> <td>Advance  </td> <td>127100   </td> <td>0.876552         </td>
        </tr>
    </tbody>
        <tr>
            <td>37.6     </td> <td>55.8    </td> <td>Moscou     </td> <td>Advance  </td> <td>100000   </td> <td>0.689655         </td>
        </tr>
    </tbody>
        <tr>
            <td>34.3     </td> <td>55.2    </td> <td>Wixma      </td> <td>Retreat  </td> <td>55000    </td> <td>0.37931          </td>
        </tr>
    </tbody>
        <tr>
            <td>32       </td> <td>54.6    </td> <td>Smolensk   </td> <td>Retreat  </td> <td>24000    </td> <td>0.165517         </td>
        </tr>
    </tbody>
        <tr>
            <td>30.4     </td> <td>54.4    </td> <td>Orscha     </td> <td>Retreat  </td> <td>20000    </td> <td>0.137931         </td>
        </tr>
    </tbody>
        <tr>
            <td>26.8     </td> <td>54.3    </td> <td>Moiodexno  </td> <td>Retreat  </td> <td>12000    </td> <td>0.0827586        </td>
        </tr>
    </tbody>
</table>




```python
with_percentages.set_format('Percent Surviving', PercentFormatter)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th> <th>City</th> <th>Direction</th> <th>Survivors</th> <th>Percent Surviving</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td> <td>Smolensk   </td> <td>Advance  </td> <td>145000   </td> <td>100.00%          </td>
        </tr>
    </tbody>
        <tr>
            <td>33.2     </td> <td>54.9    </td> <td>Dorogobouge</td> <td>Advance  </td> <td>140000   </td> <td>96.55%           </td>
        </tr>
    </tbody>
        <tr>
            <td>34.4     </td> <td>55.5    </td> <td>Chjat      </td> <td>Advance  </td> <td>127100   </td> <td>87.66%           </td>
        </tr>
    </tbody>
        <tr>
            <td>37.6     </td> <td>55.8    </td> <td>Moscou     </td> <td>Advance  </td> <td>100000   </td> <td>68.97%           </td>
        </tr>
    </tbody>
        <tr>
            <td>34.3     </td> <td>55.2    </td> <td>Wixma      </td> <td>Retreat  </td> <td>55000    </td> <td>37.93%           </td>
        </tr>
    </tbody>
        <tr>
            <td>32       </td> <td>54.6    </td> <td>Smolensk   </td> <td>Retreat  </td> <td>24000    </td> <td>16.55%           </td>
        </tr>
    </tbody>
        <tr>
            <td>30.4     </td> <td>54.4    </td> <td>Orscha     </td> <td>Retreat  </td> <td>20000    </td> <td>13.79%           </td>
        </tr>
    </tbody>
        <tr>
            <td>26.8     </td> <td>54.3    </td> <td>Moiodexno  </td> <td>Retreat  </td> <td>12000    </td> <td>8.28%            </td>
        </tr>
    </tbody>
</table>



<br><br><br><br><br><br><br><br><br><br><br><br>

## Lists


```python
2
```




    2




```python
2.0
```




    2.0




```python
make_array(2, 3.0)
```




    array([2., 3.])




```python
make_array(2, 3.0).item(0)
```




    2.0




```python
make_array(2, 'three')
```




    array(['2', 'three'], dtype='<U21')




```python
make_array(2, 'three').item(0)
```




    '2'




```python
[2, 'three']
```




    [2, 'three']




```python
type([2, 'three'])
```




    list




```python
flowers = Table.read_table('flowers.csv')
```


```python
flowers
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Petals</th> <th>Name</th> <th>Color</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>8     </td> <td>lotus    </td> <td>pink  </td>
        </tr>
    </tbody>
        <tr>
            <td>34    </td> <td>sunflower</td> <td>yellow</td>
        </tr>
    </tbody>
        <tr>
            <td>5     </td> <td>rose     </td> <td>red   </td>
        </tr>
    </tbody>
</table>




```python
my_favorite_flower = [5, 'morning glory', 'purple']
```


```python
flowers.with_row(my_favorite_flower)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Petals</th> <th>Name</th> <th>Color</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>8     </td> <td>lotus        </td> <td>pink  </td>
        </tr>
    </tbody>
        <tr>
            <td>34    </td> <td>sunflower    </td> <td>yellow</td>
        </tr>
    </tbody>
        <tr>
            <td>5     </td> <td>rose         </td> <td>red   </td>
        </tr>
    </tbody>
        <tr>
            <td>5     </td> <td>morning glory</td> <td>purple</td>
        </tr>
    </tbody>
</table>



## Table operations: Take


```python
minard
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th> <th>City</th> <th>Direction</th> <th>Survivors</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td> <td>Smolensk   </td> <td>Advance  </td> <td>145000   </td>
        </tr>
    </tbody>
        <tr>
            <td>33.2     </td> <td>54.9    </td> <td>Dorogobouge</td> <td>Advance  </td> <td>140000   </td>
        </tr>
    </tbody>
        <tr>
            <td>34.4     </td> <td>55.5    </td> <td>Chjat      </td> <td>Advance  </td> <td>127100   </td>
        </tr>
    </tbody>
        <tr>
            <td>37.6     </td> <td>55.8    </td> <td>Moscou     </td> <td>Advance  </td> <td>100000   </td>
        </tr>
    </tbody>
        <tr>
            <td>34.3     </td> <td>55.2    </td> <td>Wixma      </td> <td>Retreat  </td> <td>55000    </td>
        </tr>
    </tbody>
        <tr>
            <td>32       </td> <td>54.6    </td> <td>Smolensk   </td> <td>Retreat  </td> <td>24000    </td>
        </tr>
    </tbody>
        <tr>
            <td>30.4     </td> <td>54.4    </td> <td>Orscha     </td> <td>Retreat  </td> <td>20000    </td>
        </tr>
    </tbody>
        <tr>
            <td>26.8     </td> <td>54.3    </td> <td>Moiodexno  </td> <td>Retreat  </td> <td>12000    </td>
        </tr>
    </tbody>
</table>




```python
minard.take(0)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th> <th>City</th> <th>Direction</th> <th>Survivors</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td> <td>Smolensk</td> <td>Advance  </td> <td>145000   </td>
        </tr>
    </tbody>
</table>




```python
minard.take([0, 1, 2, 3])
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th> <th>City</th> <th>Direction</th> <th>Survivors</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td> <td>Smolensk   </td> <td>Advance  </td> <td>145000   </td>
        </tr>
    </tbody>
        <tr>
            <td>33.2     </td> <td>54.9    </td> <td>Dorogobouge</td> <td>Advance  </td> <td>140000   </td>
        </tr>
    </tbody>
        <tr>
            <td>34.4     </td> <td>55.5    </td> <td>Chjat      </td> <td>Advance  </td> <td>127100   </td>
        </tr>
    </tbody>
        <tr>
            <td>37.6     </td> <td>55.8    </td> <td>Moscou     </td> <td>Advance  </td> <td>100000   </td>
        </tr>
    </tbody>
</table>




```python
np.arange(0, 4)
```




    array([0, 1, 2, 3])




```python
minard.take(np.arange(0,4))
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th> <th>City</th> <th>Direction</th> <th>Survivors</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td> <td>Smolensk   </td> <td>Advance  </td> <td>145000   </td>
        </tr>
    </tbody>
        <tr>
            <td>33.2     </td> <td>54.9    </td> <td>Dorogobouge</td> <td>Advance  </td> <td>140000   </td>
        </tr>
    </tbody>
        <tr>
            <td>34.4     </td> <td>55.5    </td> <td>Chjat      </td> <td>Advance  </td> <td>127100   </td>
        </tr>
    </tbody>
        <tr>
            <td>37.6     </td> <td>55.8    </td> <td>Moscou     </td> <td>Advance  </td> <td>100000   </td>
        </tr>
    </tbody>
</table>



<br><br><br><br><br><br><br><br><br><br><br><br>

## Table operations: where


```python
# This table can be found online: https://www.statcrunch.com/app/index.php?dataid=1843341
nba = Table.read_table('nba_salaries.csv')
```


```python
nba
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>2015-2016 SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Paul Millsap    </td> <td>PF      </td> <td>Atlanta Hawks</td> <td>18.6717         </td>
        </tr>
    </tbody>
        <tr>
            <td>Al Horford      </td> <td>C       </td> <td>Atlanta Hawks</td> <td>12              </td>
        </tr>
    </tbody>
        <tr>
            <td>Tiago Splitter  </td> <td>C       </td> <td>Atlanta Hawks</td> <td>9.75625         </td>
        </tr>
    </tbody>
        <tr>
            <td>Jeff Teague     </td> <td>PG      </td> <td>Atlanta Hawks</td> <td>8               </td>
        </tr>
    </tbody>
        <tr>
            <td>Kyle Korver     </td> <td>SG      </td> <td>Atlanta Hawks</td> <td>5.74648         </td>
        </tr>
    </tbody>
        <tr>
            <td>Thabo Sefolosha </td> <td>SF      </td> <td>Atlanta Hawks</td> <td>4               </td>
        </tr>
    </tbody>
        <tr>
            <td>Mike Scott      </td> <td>PF      </td> <td>Atlanta Hawks</td> <td>3.33333         </td>
        </tr>
    </tbody>
        <tr>
            <td>Kent Bazemore   </td> <td>SF      </td> <td>Atlanta Hawks</td> <td>2               </td>
        </tr>
    </tbody>
        <tr>
            <td>Dennis Schroder </td> <td>PG      </td> <td>Atlanta Hawks</td> <td>1.7634          </td>
        </tr>
    </tbody>
        <tr>
            <td>Tim Hardaway Jr.</td> <td>SG      </td> <td>Atlanta Hawks</td> <td>1.30452         </td>
        </tr>
    </tbody>
</table>
<p>... (407 rows omitted)</p>




```python
nba.sort('2015-2016 SALARY')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>2015-2016 SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Thanasis Antetokounmpo</td> <td>SF      </td> <td>New York Knicks     </td> <td>0.030888        </td>
        </tr>
    </tbody>
        <tr>
            <td>Jordan McRae          </td> <td>SG      </td> <td>Phoenix Suns        </td> <td>0.049709        </td>
        </tr>
    </tbody>
        <tr>
            <td>Cory Jefferson        </td> <td>PF      </td> <td>Phoenix Suns        </td> <td>0.049709        </td>
        </tr>
    </tbody>
        <tr>
            <td>Elliot Williams       </td> <td>SG      </td> <td>Memphis Grizzlies   </td> <td>0.055722        </td>
        </tr>
    </tbody>
        <tr>
            <td>Orlando Johnson       </td> <td>SG      </td> <td>Phoenix Suns        </td> <td>0.055722        </td>
        </tr>
    </tbody>
        <tr>
            <td>Phil Pressey          </td> <td>PG      </td> <td>Phoenix Suns        </td> <td>0.055722        </td>
        </tr>
    </tbody>
        <tr>
            <td>Keith Appling         </td> <td>PG      </td> <td>Orlando Magic       </td> <td>0.061776        </td>
        </tr>
    </tbody>
        <tr>
            <td>Sean Kilpatrick       </td> <td>SG      </td> <td>Denver Nuggets      </td> <td>0.099418        </td>
        </tr>
    </tbody>
        <tr>
            <td>Erick Green           </td> <td>PG      </td> <td>Utah Jazz           </td> <td>0.099418        </td>
        </tr>
    </tbody>
        <tr>
            <td>Jeff Ayres            </td> <td>PF      </td> <td>Los Angeles Clippers</td> <td>0.111444        </td>
        </tr>
    </tbody>
</table>
<p>... (407 rows omitted)</p>




```python
nba = nba.relabeled('2015-2016 SALARY', 'SALARY')
```


```python
nba.sort('SALARY')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Thanasis Antetokounmpo</td> <td>SF      </td> <td>New York Knicks     </td> <td>0.030888</td>
        </tr>
    </tbody>
        <tr>
            <td>Jordan McRae          </td> <td>SG      </td> <td>Phoenix Suns        </td> <td>0.049709</td>
        </tr>
    </tbody>
        <tr>
            <td>Cory Jefferson        </td> <td>PF      </td> <td>Phoenix Suns        </td> <td>0.049709</td>
        </tr>
    </tbody>
        <tr>
            <td>Elliot Williams       </td> <td>SG      </td> <td>Memphis Grizzlies   </td> <td>0.055722</td>
        </tr>
    </tbody>
        <tr>
            <td>Orlando Johnson       </td> <td>SG      </td> <td>Phoenix Suns        </td> <td>0.055722</td>
        </tr>
    </tbody>
        <tr>
            <td>Phil Pressey          </td> <td>PG      </td> <td>Phoenix Suns        </td> <td>0.055722</td>
        </tr>
    </tbody>
        <tr>
            <td>Keith Appling         </td> <td>PG      </td> <td>Orlando Magic       </td> <td>0.061776</td>
        </tr>
    </tbody>
        <tr>
            <td>Sean Kilpatrick       </td> <td>SG      </td> <td>Denver Nuggets      </td> <td>0.099418</td>
        </tr>
    </tbody>
        <tr>
            <td>Erick Green           </td> <td>PG      </td> <td>Utah Jazz           </td> <td>0.099418</td>
        </tr>
    </tbody>
        <tr>
            <td>Jeff Ayres            </td> <td>PF      </td> <td>Los Angeles Clippers</td> <td>0.111444</td>
        </tr>
    </tbody>
</table>
<p>... (407 rows omitted)</p>




```python
nba.where('SALARY', are.above(10))
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Paul Millsap  </td> <td>PF      </td> <td>Atlanta Hawks    </td> <td>18.6717</td>
        </tr>
    </tbody>
        <tr>
            <td>Al Horford    </td> <td>C       </td> <td>Atlanta Hawks    </td> <td>12     </td>
        </tr>
    </tbody>
        <tr>
            <td>Joe Johnson   </td> <td>SF      </td> <td>Brooklyn Nets    </td> <td>24.8949</td>
        </tr>
    </tbody>
        <tr>
            <td>Thaddeus Young</td> <td>PF      </td> <td>Brooklyn Nets    </td> <td>11.236 </td>
        </tr>
    </tbody>
        <tr>
            <td>Al Jefferson  </td> <td>C       </td> <td>Charlotte Hornets</td> <td>13.5   </td>
        </tr>
    </tbody>
        <tr>
            <td>Nicolas Batum </td> <td>SG      </td> <td>Charlotte Hornets</td> <td>13.1253</td>
        </tr>
    </tbody>
        <tr>
            <td>Kemba Walker  </td> <td>PG      </td> <td>Charlotte Hornets</td> <td>12     </td>
        </tr>
    </tbody>
        <tr>
            <td>Derrick Rose  </td> <td>PG      </td> <td>Chicago Bulls    </td> <td>20.0931</td>
        </tr>
    </tbody>
        <tr>
            <td>Jimmy Butler  </td> <td>SG      </td> <td>Chicago Bulls    </td> <td>16.4075</td>
        </tr>
    </tbody>
        <tr>
            <td>Joakim Noah   </td> <td>C       </td> <td>Chicago Bulls    </td> <td>13.4   </td>
        </tr>
    </tbody>
</table>
<p>... (59 rows omitted)</p>




```python
nba.where('SALARY', are.above(10)).sort('SALARY')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>DeMar DeRozan  </td> <td>SG      </td> <td>Toronto Raptors     </td> <td>10.05  </td>
        </tr>
    </tbody>
        <tr>
            <td>Gerald Wallace </td> <td>SF      </td> <td>Philadelphia 76ers  </td> <td>10.1059</td>
        </tr>
    </tbody>
        <tr>
            <td>Luol Deng      </td> <td>SF      </td> <td>Miami Heat          </td> <td>10.1516</td>
        </tr>
    </tbody>
        <tr>
            <td>Monta Ellis    </td> <td>SG      </td> <td>Indiana Pacers      </td> <td>10.3   </td>
        </tr>
    </tbody>
        <tr>
            <td>Wilson Chandler</td> <td>SF      </td> <td>Denver Nuggets      </td> <td>10.4494</td>
        </tr>
    </tbody>
        <tr>
            <td>Brendan Haywood</td> <td>C       </td> <td>Cleveland Cavaliers </td> <td>10.5225</td>
        </tr>
    </tbody>
        <tr>
            <td>Jrue Holiday   </td> <td>PG      </td> <td>New Orleans Pelicans</td> <td>10.5955</td>
        </tr>
    </tbody>
        <tr>
            <td>Tyreke Evans   </td> <td>SG      </td> <td>New Orleans Pelicans</td> <td>10.7346</td>
        </tr>
    </tbody>
        <tr>
            <td>Marcin Gortat  </td> <td>C       </td> <td>Washington Wizards  </td> <td>11.2174</td>
        </tr>
    </tbody>
        <tr>
            <td>Thaddeus Young </td> <td>PF      </td> <td>Brooklyn Nets       </td> <td>11.236 </td>
        </tr>
    </tbody>
</table>
<p>... (59 rows omitted)</p>




```python
nba.where('SALARY', are.between(10, 11))
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Brendan Haywood</td> <td>C       </td> <td>Cleveland Cavaliers </td> <td>10.5225</td>
        </tr>
    </tbody>
        <tr>
            <td>Wilson Chandler</td> <td>SF      </td> <td>Denver Nuggets      </td> <td>10.4494</td>
        </tr>
    </tbody>
        <tr>
            <td>Monta Ellis    </td> <td>SG      </td> <td>Indiana Pacers      </td> <td>10.3   </td>
        </tr>
    </tbody>
        <tr>
            <td>Luol Deng      </td> <td>SF      </td> <td>Miami Heat          </td> <td>10.1516</td>
        </tr>
    </tbody>
        <tr>
            <td>Tyreke Evans   </td> <td>SG      </td> <td>New Orleans Pelicans</td> <td>10.7346</td>
        </tr>
    </tbody>
        <tr>
            <td>Jrue Holiday   </td> <td>PG      </td> <td>New Orleans Pelicans</td> <td>10.5955</td>
        </tr>
    </tbody>
        <tr>
            <td>Gerald Wallace </td> <td>SF      </td> <td>Philadelphia 76ers  </td> <td>10.1059</td>
        </tr>
    </tbody>
        <tr>
            <td>Danny Green    </td> <td>SG      </td> <td>San Antonio Spurs   </td> <td>10     </td>
        </tr>
    </tbody>
        <tr>
            <td>DeMar DeRozan  </td> <td>SG      </td> <td>Toronto Raptors     </td> <td>10.05  </td>
        </tr>
    </tbody>
</table>




```python
nba.where('TEAM', are.equal_to('Toronto Raptors'))
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>DeMarre Carroll  </td> <td>SF      </td> <td>Toronto Raptors</td> <td>13.6   </td>
        </tr>
    </tbody>
        <tr>
            <td>Kyle Lowry       </td> <td>PG      </td> <td>Toronto Raptors</td> <td>12     </td>
        </tr>
    </tbody>
        <tr>
            <td>DeMar DeRozan    </td> <td>SG      </td> <td>Toronto Raptors</td> <td>10.05  </td>
        </tr>
    </tbody>
        <tr>
            <td>Cory Joseph      </td> <td>PG      </td> <td>Toronto Raptors</td> <td>7      </td>
        </tr>
    </tbody>
        <tr>
            <td>Patrick Patterson</td> <td>PF      </td> <td>Toronto Raptors</td> <td>6.26867</td>
        </tr>
    </tbody>
        <tr>
            <td>Jonas Valanciunas</td> <td>C       </td> <td>Toronto Raptors</td> <td>4.66048</td>
        </tr>
    </tbody>
        <tr>
            <td>Terrence Ross    </td> <td>SF      </td> <td>Toronto Raptors</td> <td>3.55392</td>
        </tr>
    </tbody>
        <tr>
            <td>Luis Scola       </td> <td>PF      </td> <td>Toronto Raptors</td> <td>2.9    </td>
        </tr>
    </tbody>
        <tr>
            <td>Bismack Biyombo  </td> <td>C       </td> <td>Toronto Raptors</td> <td>2.814  </td>
        </tr>
    </tbody>
        <tr>
            <td>Luke Ridnour     </td> <td>PG      </td> <td>Toronto Raptors</td> <td>2.75   </td>
        </tr>
    </tbody>
</table>
<p>... (7 rows omitted)</p>




```python
nba.where('TEAM', 'Toronto Raptors')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>DeMarre Carroll  </td> <td>SF      </td> <td>Toronto Raptors</td> <td>13.6   </td>
        </tr>
    </tbody>
        <tr>
            <td>Kyle Lowry       </td> <td>PG      </td> <td>Toronto Raptors</td> <td>12     </td>
        </tr>
    </tbody>
        <tr>
            <td>DeMar DeRozan    </td> <td>SG      </td> <td>Toronto Raptors</td> <td>10.05  </td>
        </tr>
    </tbody>
        <tr>
            <td>Cory Joseph      </td> <td>PG      </td> <td>Toronto Raptors</td> <td>7      </td>
        </tr>
    </tbody>
        <tr>
            <td>Patrick Patterson</td> <td>PF      </td> <td>Toronto Raptors</td> <td>6.26867</td>
        </tr>
    </tbody>
        <tr>
            <td>Jonas Valanciunas</td> <td>C       </td> <td>Toronto Raptors</td> <td>4.66048</td>
        </tr>
    </tbody>
        <tr>
            <td>Terrence Ross    </td> <td>SF      </td> <td>Toronto Raptors</td> <td>3.55392</td>
        </tr>
    </tbody>
        <tr>
            <td>Luis Scola       </td> <td>PF      </td> <td>Toronto Raptors</td> <td>2.9    </td>
        </tr>
    </tbody>
        <tr>
            <td>Bismack Biyombo  </td> <td>C       </td> <td>Toronto Raptors</td> <td>2.814  </td>
        </tr>
    </tbody>
        <tr>
            <td>Luke Ridnour     </td> <td>PG      </td> <td>Toronto Raptors</td> <td>2.75   </td>
        </tr>
    </tbody>
</table>
<p>... (7 rows omitted)</p>




```python
nba.where('TEAM', are.containing('Raptors'))
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>DeMarre Carroll  </td> <td>SF      </td> <td>Toronto Raptors</td> <td>13.6   </td>
        </tr>
    </tbody>
        <tr>
            <td>Kyle Lowry       </td> <td>PG      </td> <td>Toronto Raptors</td> <td>12     </td>
        </tr>
    </tbody>
        <tr>
            <td>DeMar DeRozan    </td> <td>SG      </td> <td>Toronto Raptors</td> <td>10.05  </td>
        </tr>
    </tbody>
        <tr>
            <td>Cory Joseph      </td> <td>PG      </td> <td>Toronto Raptors</td> <td>7      </td>
        </tr>
    </tbody>
        <tr>
            <td>Patrick Patterson</td> <td>PF      </td> <td>Toronto Raptors</td> <td>6.26867</td>
        </tr>
    </tbody>
        <tr>
            <td>Jonas Valanciunas</td> <td>C       </td> <td>Toronto Raptors</td> <td>4.66048</td>
        </tr>
    </tbody>
        <tr>
            <td>Terrence Ross    </td> <td>SF      </td> <td>Toronto Raptors</td> <td>3.55392</td>
        </tr>
    </tbody>
        <tr>
            <td>Luis Scola       </td> <td>PF      </td> <td>Toronto Raptors</td> <td>2.9    </td>
        </tr>
    </tbody>
        <tr>
            <td>Bismack Biyombo  </td> <td>C       </td> <td>Toronto Raptors</td> <td>2.814  </td>
        </tr>
    </tbody>
        <tr>
            <td>Luke Ridnour     </td> <td>PG      </td> <td>Toronto Raptors</td> <td>2.75   </td>
        </tr>
    </tbody>
</table>
<p>... (7 rows omitted)</p>




```python
nba.where('PLAYER', are.equal_to('Stephen Curry'))
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Stephen Curry</td> <td>PG      </td> <td>Golden State Warriors</td> <td>11.3708</td>
        </tr>
    </tbody>
</table>




```python
nba.where('TEAM', are.equal_to('Golden State Warriors'))
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Klay Thompson    </td> <td>SG      </td> <td>Golden State Warriors</td> <td>15.501 </td>
        </tr>
    </tbody>
        <tr>
            <td>Draymond Green   </td> <td>PF      </td> <td>Golden State Warriors</td> <td>14.2609</td>
        </tr>
    </tbody>
        <tr>
            <td>Andrew Bogut     </td> <td>C       </td> <td>Golden State Warriors</td> <td>13.8   </td>
        </tr>
    </tbody>
        <tr>
            <td>Andre Iguodala   </td> <td>SF      </td> <td>Golden State Warriors</td> <td>11.7105</td>
        </tr>
    </tbody>
        <tr>
            <td>Stephen Curry    </td> <td>PG      </td> <td>Golden State Warriors</td> <td>11.3708</td>
        </tr>
    </tbody>
        <tr>
            <td>Jason Thompson   </td> <td>PF      </td> <td>Golden State Warriors</td> <td>7.00847</td>
        </tr>
    </tbody>
        <tr>
            <td>Shaun Livingston </td> <td>PG      </td> <td>Golden State Warriors</td> <td>5.54373</td>
        </tr>
    </tbody>
        <tr>
            <td>Harrison Barnes  </td> <td>SF      </td> <td>Golden State Warriors</td> <td>3.8734 </td>
        </tr>
    </tbody>
        <tr>
            <td>Marreese Speights</td> <td>C       </td> <td>Golden State Warriors</td> <td>3.815  </td>
        </tr>
    </tbody>
        <tr>
            <td>Leandro Barbosa  </td> <td>SG      </td> <td>Golden State Warriors</td> <td>2.5    </td>
        </tr>
    </tbody>
</table>
<p>... (4 rows omitted)</p>




```python
nba.where('TEAM', are.equal_to('Golden State Warriors')).sort('SALARY', descending=True)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Klay Thompson    </td> <td>SG      </td> <td>Golden State Warriors</td> <td>15.501 </td>
        </tr>
    </tbody>
        <tr>
            <td>Draymond Green   </td> <td>PF      </td> <td>Golden State Warriors</td> <td>14.2609</td>
        </tr>
    </tbody>
        <tr>
            <td>Andrew Bogut     </td> <td>C       </td> <td>Golden State Warriors</td> <td>13.8   </td>
        </tr>
    </tbody>
        <tr>
            <td>Andre Iguodala   </td> <td>SF      </td> <td>Golden State Warriors</td> <td>11.7105</td>
        </tr>
    </tbody>
        <tr>
            <td>Stephen Curry    </td> <td>PG      </td> <td>Golden State Warriors</td> <td>11.3708</td>
        </tr>
    </tbody>
        <tr>
            <td>Jason Thompson   </td> <td>PF      </td> <td>Golden State Warriors</td> <td>7.00847</td>
        </tr>
    </tbody>
        <tr>
            <td>Shaun Livingston </td> <td>PG      </td> <td>Golden State Warriors</td> <td>5.54373</td>
        </tr>
    </tbody>
        <tr>
            <td>Harrison Barnes  </td> <td>SF      </td> <td>Golden State Warriors</td> <td>3.8734 </td>
        </tr>
    </tbody>
        <tr>
            <td>Marreese Speights</td> <td>C       </td> <td>Golden State Warriors</td> <td>3.815  </td>
        </tr>
    </tbody>
        <tr>
            <td>Leandro Barbosa  </td> <td>SG      </td> <td>Golden State Warriors</td> <td>2.5    </td>
        </tr>
    </tbody>
</table>
<p>... (4 rows omitted)</p>




```python
nba.where('SALARY', are.between(10, 12))
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Thaddeus Young </td> <td>PF      </td> <td>Brooklyn Nets        </td> <td>11.236 </td>
        </tr>
    </tbody>
        <tr>
            <td>Brendan Haywood</td> <td>C       </td> <td>Cleveland Cavaliers  </td> <td>10.5225</td>
        </tr>
    </tbody>
        <tr>
            <td>Kenneth Faried </td> <td>PF      </td> <td>Denver Nuggets       </td> <td>11.236 </td>
        </tr>
    </tbody>
        <tr>
            <td>Wilson Chandler</td> <td>SF      </td> <td>Denver Nuggets       </td> <td>10.4494</td>
        </tr>
    </tbody>
        <tr>
            <td>Andre Iguodala </td> <td>SF      </td> <td>Golden State Warriors</td> <td>11.7105</td>
        </tr>
    </tbody>
        <tr>
            <td>Stephen Curry  </td> <td>PG      </td> <td>Golden State Warriors</td> <td>11.3708</td>
        </tr>
    </tbody>
        <tr>
            <td>Monta Ellis    </td> <td>SG      </td> <td>Indiana Pacers       </td> <td>10.3   </td>
        </tr>
    </tbody>
        <tr>
            <td>Luol Deng      </td> <td>SF      </td> <td>Miami Heat           </td> <td>10.1516</td>
        </tr>
    </tbody>
        <tr>
            <td>Tyreke Evans   </td> <td>SG      </td> <td>New Orleans Pelicans </td> <td>10.7346</td>
        </tr>
    </tbody>
        <tr>
            <td>Jrue Holiday   </td> <td>PG      </td> <td>New Orleans Pelicans </td> <td>10.5955</td>
        </tr>
    </tbody>
</table>
<p>... (5 rows omitted)</p>


