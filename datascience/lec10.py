
# coding: utf-8

# In[1]:


from datascience import *
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')


# ## One Attribute Group

# * Grouping by column
# * The grop method aggregates all rows with the same value for a column info a single row 
# * First agrument: Which column by
# * second arg: (Optional how to combin values
#   ** len - number of groupsed values (default)
#   ** list - list of all grouped vals
#   ** sum - total of all grouped vals
#   

# In[2]:


all_cones = Table.read_table('cones.csv')
cones = all_cones.drop('Color').exclude(5)
cones


# In[3]:


cones.group('Flavor')


# In[4]:


cones.group('Flavor', list)


# In[5]:


cones.group('Flavor', len)


# In[6]:


cones.group('Flavor', min)


# In[7]:


min(cones.where('Flavor', 'chocolate').column('Price'))


# In[8]:


cones.group('Flavor', np.average)


# In[9]:


def data_range(x):
    return max(x) - min(x)
# returns the difference between the most expensive and least expensive


# In[10]:


cones.group('Flavor', data_range)


# In[11]:


nba = Table.read_table('nba_salaries.csv').relabeled(3, 'SALARY')
nba


# In[12]:


teams_and_money = nba.select('TEAM', 'SALARY')
# focus on variables of interest!!!!!!!!!!!!!!!!!!!!
teams_and_money.group('TEAM', sum).sort(1, descending=True)
# returns how much each team spent on salaries.


# In[13]:


nba.group('TEAM', sum)
# same results as above but the table messy with the empty columns due to trying to 
# sum player names in 1 and position sums 2 which don't make sense


# In[14]:


# if we were interested by position
position_and_money = nba.select('POSITION', 'SALARY')
position_and_money.group('POSITION')


# In[15]:


position_and_money.group('POSITION', np.average)


# ## Cross Classification

# * classifying indiviuals by more than one attribute; aggregates all rows that share the combination of values
# * first arg( licolumns to group by)
# * second arg optioal

# In[16]:


all_cones
# using a small daatset is easier to see what is happening behind the scenes


# In[17]:


all_cones.group('Flavor')


# In[18]:


all_cones.group(['Flavor', 'Color'])


# In[19]:


all_cones.group(['Flavor', 'Color'], max)


# In[20]:


nba
# looking at a larger dataset


# In[21]:


# see how much each team pays per position
# drop get's rid of player column
nba.drop(0).group(['TEAM', 'POSITION'], np.average)


# In[22]:


nba.drop(0, 2).group('POSITION', np.average)


# In[23]:


# Looking at another table income by education, gender, age
full_table = Table.read_table('educ_inc.csv')
ca_2014 = full_table.where('Year', are.equal_to('1/1/14 0:00')).where('Age', are.not_equal_to('00 to 17')).drop(0).sort('Population Count')
ca_2014


# In[24]:


# look at table without ages tag
no_ages = ca_2014.drop(0)
no_ages


# In[25]:


no_ages.group([0, 1, 2], sum)
# cross classified by three variables resulting in 64 combinbations in the results


# ## Example 1: NBA Salaries with group

# **Please run all cells before this cell, including the previous example cells and the import cell at the top of the notebook.**

# In[26]:


nba


# In[27]:


starter_salaries = nba.drop(0).group(['TEAM', 'POSITION'], max)
# Which team spent the most on their starters?
# A starter is assumed to be the highest paid player is said position.
starter_salaries


# In[28]:


starter_salaries.drop(1).group('TEAM', sum).sort(1, descending=True)
# and this is the answer...


# ## Pivot Tables

# * When cross classifying by two variables it is better to use pivot tables than groups.
# * produces a grid of counts or agregated valutes
# * two required values

# In[29]:


all_cones


# In[30]:


all_cones.group(['Flavor', 'Color'])


# In[33]:


all_cones.pivot('Flavor', 'Color')   # pivot table, aka contingency table in Statistics


# In[35]:


all_cones.pivot('Color', 'Flavor') # Notice that first arg forms the columns, second forms the rows


# In[39]:


all_cones.pivot('Color', 'Flavor', values = 'Price', collect = max)
# Instead of counts, show price (max in this case)
# shorthand way of writing this is too is all_cones.pivot('Color', 'Flavor', 'Price', max)


# In[40]:


nba


# In[41]:


nba.drop(0).group(['TEAM', 'POSITION'], np.average)


# In[42]:


nba.pivot('POSITION', 'TEAM', 'SALARY', np.average)


# ## Example 2: NBA Salaries with pivot

# * Identify the highest paid salary by position

# In[43]:


step_1 = nba.pivot('POSITION', 'TEAM', 'SALARY', max)
step_1


# In[46]:


totals = step_1.drop(0).apply(sum) # add upp the row totals and make array
totals 


# In[47]:


step_1.with_columns('TOTAL', totals).sort(6, descending=True)
# tac on the totals tables to the step1 table


# ## Comparing Distributions

# * Performing an analysis using several techniques so far
# * Population of cross classified by age, geners, edu, and income
# * Goal: to see if there's an association of edu level and income

# In[48]:


ca_2014


# In[49]:


educ_income = ca_2014.pivot(2, 3, 4, sum)
educ_income


# In[50]:


def percent(x):
    """Convert an array of counts into percents"""
    return np.round((x / sum(x)) * 100, 2)


# In[54]:


distributions = educ_income.select(0).with_columns(
    'Bachelors or Higher', percent(educ_income.column(1)),
    'High School', percent(educ_income.column(3))
)
distributions


# In[55]:


sum(distributions.column(1))


# In[56]:


distributions.barh(0)

