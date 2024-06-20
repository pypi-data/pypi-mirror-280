# Bang PG
> As fast as a bullet 

This packeges implementes a faster alternative `to_sql()` method for PostgreSQL that support COPY FROM.

There are two ways to use it:

1. 

```python
import bangpg
bangpg.to_sql(df, 'table', engine,  if_exists='append', index=False)

```

2.

```python
import bangpg
df.to_sql('table', engine,  if_exists='append', index=False, method=bangpg.psql_insert_copy)

```




references: https://pandas.pydata.org/docs/user_guide/io.html#io-sql-method