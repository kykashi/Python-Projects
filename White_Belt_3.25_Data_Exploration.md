# White Belt Testing Data Cleaning

## Installing Pandas and os, Data Frame Import


```python
import pandas as pd
import os

df = pd.read_excel(r"C:\Users\k4leu\OneDrive\Documents\white_belts_3.25.xlsx")

print(df)
```

        Test Date  Student ID Class   Rank  Kicho 1 and 2  Stances  Blocks  \
    0  2023-03-25        1704    JR  WHITE            3.0      3.0     3.5   
    1  2023-03-25        4660    JR  WHITE            4.0      4.0     3.5   
    2  2023-03-25       19110    JR  WHITE            3.5      3.0     3.5   
    3  2023-03-25        7728    JR  WHITE            4.0      3.5     3.5   
    4  2023-03-25        7665    JR  WHITE            3.0      3.0     3.5   
    5  2023-03-25        5763    JR  WHITE            3.5      3.5     3.5   
    6  2023-03-25       98910    JR  WHITE            5.0      5.0     5.0   
    7  2023-03-25       98908    JR  WHITE            3.0      3.0     3.0   
    8  2023-03-25        3017    JR  WHITE            4.0      4.5     4.0   
    9  2023-03-25       98906    JR  WHITE            4.5      4.5     5.0   
    10 2023-03-25        3123    JR  WHITE            4.5      4.0     4.0   
    
        Hand Strikes  Poomsae Kicks  High-Rising  Out-In  In-Out  Roundhouse  \
    0            3.5            4.0          4.5     3.5     3.5         3.5   
    1            3.5            4.5          4.5     4.0     4.5         4.5   
    2            3.5            3.0          4.0     4.0     4.0         3.5   
    3            4.0            4.0          5.0     4.5     4.0         4.5   
    4            3.0            3.5          2.0     3.5     3.5         5.0   
    5            3.5            3.5          3.5     3.0     3.0         4.0   
    6            5.0            5.0          5.0     5.0     5.0         5.0   
    7            3.0            4.0          4.5     4.0     4.0         4.0   
    8            4.0            4.0          3.5     4.0     3.5         4.0   
    9            4.5            5.0          NaN     NaN     NaN         4.5   
    10           4.5            4.5          5.0     3.5     3.5         5.0   
    
        Front  Kick AVG  Breaking  Sparring  Questions  
    0     3.5      3.70         5       4.5          5  
    1     4.5      4.40         5       4.5          5  
    2     4.0      3.90         5       4.5          5  
    3     5.0      4.60         4       4.5          5  
    4     5.0      3.80         5       5.0          5  
    5     4.0      3.50         5       3.0          5  
    6     5.0      5.00         5       4.5          5  
    7     4.5      4.20         5       4.0          5  
    8     4.5      3.90         5       4.5          5  
    9     5.0      4.75         5       4.5          5  
    10    4.5      4.30         5       5.0          5  
    

## Data Frame objects


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 11 entries, 0 to 10
    Data columns (total 18 columns):
     #   Column         Non-Null Count  Dtype         
    ---  ------         --------------  -----         
     0   Test Date      11 non-null     datetime64[ns]
     1   Student ID     11 non-null     int64         
     2   Class          11 non-null     object        
     3   Rank           11 non-null     object        
     4   Kicho 1 and 2  11 non-null     float64       
     5   Stances        11 non-null     float64       
     6   Blocks         11 non-null     float64       
     7   Hand Strikes   11 non-null     float64       
     8   Poomsae Kicks  11 non-null     float64       
     9   High-Rising    10 non-null     float64       
     10  Out-In         10 non-null     float64       
     11  In-Out         10 non-null     float64       
     12  Roundhouse     11 non-null     float64       
     13  Front          11 non-null     float64       
     14  Kick AVG       11 non-null     float64       
     15  Breaking       11 non-null     int64         
     16  Sparring       11 non-null     float64       
     17  Questions      11 non-null     int64         
    dtypes: datetime64[ns](1), float64(12), int64(3), object(2)
    memory usage: 1.7+ KB
    

## Checking Statistic Description for Data Frame 


```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>Kicho 1 and 2</th>
      <th>Stances</th>
      <th>Blocks</th>
      <th>Hand Strikes</th>
      <th>Poomsae Kicks</th>
      <th>High-Rising</th>
      <th>Out-In</th>
      <th>In-Out</th>
      <th>Roundhouse</th>
      <th>Front</th>
      <th>Kick AVG</th>
      <th>Breaking</th>
      <th>Sparring</th>
      <th>Questions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>11.000000</td>
      <td>11.000000</td>
      <td>11.000000</td>
      <td>11.000000</td>
      <td>11.000000</td>
      <td>11.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>11.000000</td>
      <td>11.00</td>
      <td>11.000000</td>
      <td>11.000000</td>
      <td>11.000000</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>31772.181818</td>
      <td>3.818182</td>
      <td>3.727273</td>
      <td>3.818182</td>
      <td>3.818182</td>
      <td>4.090909</td>
      <td>4.150000</td>
      <td>3.900000</td>
      <td>3.850000</td>
      <td>4.318182</td>
      <td>4.50</td>
      <td>4.186364</td>
      <td>4.909091</td>
      <td>4.409091</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>std</th>
      <td>43364.205976</td>
      <td>0.680908</td>
      <td>0.719848</td>
      <td>0.643146</td>
      <td>0.643146</td>
      <td>0.625227</td>
      <td>0.944281</td>
      <td>0.567646</td>
      <td>0.579751</td>
      <td>0.560032</td>
      <td>0.50</td>
      <td>0.472277</td>
      <td>0.301511</td>
      <td>0.539360</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1704.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.500000</td>
      <td>3.50</td>
      <td>3.500000</td>
      <td>4.000000</td>
      <td>3.000000</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3891.500000</td>
      <td>3.250000</td>
      <td>3.000000</td>
      <td>3.500000</td>
      <td>3.500000</td>
      <td>3.750000</td>
      <td>3.625000</td>
      <td>3.500000</td>
      <td>3.500000</td>
      <td>4.000000</td>
      <td>4.25</td>
      <td>3.850000</td>
      <td>5.000000</td>
      <td>4.500000</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>7665.000000</td>
      <td>4.000000</td>
      <td>3.500000</td>
      <td>3.500000</td>
      <td>3.500000</td>
      <td>4.000000</td>
      <td>4.500000</td>
      <td>4.000000</td>
      <td>3.750000</td>
      <td>4.500000</td>
      <td>4.50</td>
      <td>4.200000</td>
      <td>5.000000</td>
      <td>4.500000</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>59008.000000</td>
      <td>4.250000</td>
      <td>4.250000</td>
      <td>4.000000</td>
      <td>4.250000</td>
      <td>4.500000</td>
      <td>4.875000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.750000</td>
      <td>5.00</td>
      <td>4.500000</td>
      <td>5.000000</td>
      <td>4.500000</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>max</th>
      <td>98910.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.00</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>



## Creating data subset of all Poomsae scores


```python
psae_scores = df[['Kicho 1 and 2', 'Stances', 'Blocks', 'Hand Strikes', 'Poomsae Kicks']]
psae_scores
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Kicho 1 and 2</th>
      <th>Stances</th>
      <th>Blocks</th>
      <th>Hand Strikes</th>
      <th>Poomsae Kicks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.0</td>
      <td>4.0</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.5</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.0</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>4.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>3.0</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3.5</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>5.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4.0</td>
      <td>4.5</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>4.5</td>
      <td>4.5</td>
      <td>5.0</td>
      <td>4.5</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>4.5</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>4.5</td>
    </tr>
  </tbody>
</table>
</div>



## Separate Data Frame for average score of 'Kicho' Poomsae Patterns and Components


```python
psae_avr = pd.DataFrame(psae_scores.mean(), columns = ['Avg'])
psae_avr.index.name = 'psae Components'
psae_avr
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg</th>
    </tr>
    <tr>
      <th>psae Components</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Kicho 1 and 2</th>
      <td>3.818182</td>
    </tr>
    <tr>
      <th>Stances</th>
      <td>3.727273</td>
    </tr>
    <tr>
      <th>Blocks</th>
      <td>3.818182</td>
    </tr>
    <tr>
      <th>Hand Strikes</th>
      <td>3.818182</td>
    </tr>
    <tr>
      <th>Poomsae Kicks</th>
      <td>4.090909</td>
    </tr>
  </tbody>
</table>
</div>



## Lowest average is Poomsae component is 3.7 - Stances 


```python
psae_avr.idxmin()
psae_avr.min()
```




    Avg    3.727273
    dtype: float64



## Highest average Poomsae Component is 4.1 Poomsae Kicks


```python
psae_avr.max() 
```




    Avg    4.090909
    dtype: float64



## Creating a Column Graph of the Psae Data Frame


```python
psae_avr.plot(kind='barh', figsize=(10,5))
```




    <Axes: ylabel='psae Components'>




    
![png](output_16_1.png)
    


## Creating a subset of all kicking scores that are not related to Poomsae 


```python
kick_score = df[[ 'High-Rising', 'Out-In','In-Out', 'Roundhouse', 'Front', 'Kick AVG',]]
```

## Finding average kick scores and creating a data frame with averages


```python
kick_avr = pd.DataFrame(kick_score.mean(), columns=['Avg'])
kick_avr.index.name='Kick Type'
kick_avr
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg</th>
    </tr>
    <tr>
      <th>Kick Type</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>High-Rising</th>
      <td>4.150000</td>
    </tr>
    <tr>
      <th>Out-In</th>
      <td>3.900000</td>
    </tr>
    <tr>
      <th>In-Out</th>
      <td>3.850000</td>
    </tr>
    <tr>
      <th>Roundhouse</th>
      <td>4.318182</td>
    </tr>
    <tr>
      <th>Front</th>
      <td>4.500000</td>
    </tr>
    <tr>
      <th>Kick AVG</th>
      <td>4.186364</td>
    </tr>
  </tbody>
</table>
</div>



## Lowest average kick is the Inside-Outside Crescent Kick


```python
kick_avr.min()
```




    Avg    3.85
    dtype: float64



## Finding Highest Average kick score is the Front Kick


```python
kick_avr.max()
```




    Avg    4.5
    dtype: float64



## Creating a Column Chart with the kick_avr Data Frame


```python
kick_avr.plot(kind='barh', figsize=(10,5))
```




    <Axes: ylabel='Kick Type'>




    
![png](output_26_1.png)
    


## Exporting psae_avr and kick_avr to Excel and into Tableau


```python
path = os.path.join(os.path.expanduser("~"), "Documents", r"C:\Users\k4leu\OneDrive\Documents\BELT TESTING DATA")
kick_avr.to_csv(os.path.join(path, 'kick_avr.csv'), index = True)

path = os.path.join(os.path.expanduser("~"), "Documents", r"C:\Users\k4leu\OneDrive\Documents\BELT TESTING DATA")
psae_avr.to_csv(os.path.join(path, 'psae.csv'), index = True)
```
