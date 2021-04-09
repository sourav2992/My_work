# Databricks notebook source
departments = spark.read.option("header", "true").option("InferSchema", "true").csv('/FileStore/tables/Departments.csv')
salaries = spark.read.option("header", "true").option("InferSchema", "true").csv('/FileStore/tables/salaries.csv')
titles = spark.read.option("header", "true").option("InferSchema", "true").csv('/FileStore/tables/title.csv')
dept_emp = spark.read.option("header", "true").option("InferSchema", "true").csv('/FileStore/tables/dept_emp.csv')

# COMMAND ----------

#dbutils.fs.rm("/FileStore/tables/dept_emp.csv")

# COMMAND ----------

# Q1
df1 = salaries.join(titles, ["emp_no"])
df2 = df1.join(dept_emp, ["emp_no"])
df = df2.join(departments, ["dept_no"])
df.show()

# COMMAND ----------

df.sort("salary").show()

# COMMAND ----------

from pyspark.sql.functions import first, last, kurtosis, min, mean, skewness
df.select("dept_name", "title", "salary")\
.sort("salary")\
.limit(1)\
.show()

# COMMAND ----------

df.groupBy("dept_name","title").min("salary").filter(col("title")=='Manager').show()

# COMMAND ----------

# Q2
df3 = df.select("dept_name", "title", "salary")\
.groupBy("dept_name", "title")\
.min("salary")\
.filter(col("title") == "Manager")
df4 = df.select("dept_name", "title", "salary")\
.groupBy("dept_name", "title")\
.max()\
.filter(df["title"] == "Manager")
df5 = df4.join(df3, ["dept_name", "title"])
df5.show()

# COMMAND ----------

from pyspark.sql.functions import *
df5 = df5.withColumn('salary_range', concat(coalesce(col('min(salary)'), lit('')), lit('-'), coalesce(col('max(salary)'), lit(''))))
df5.show()

# COMMAND ----------

df5.select("dept_name", "title", "salary_range")\
.show()

# COMMAND ----------

# Q3
df6 = df.select("dept_name", "salary").groupby("dept_name").max("salary")
df7 = df.select("dept_name", "title", "salary").groupby("dept_name", "title").max("salary")

# COMMAND ----------

df6.show()

# COMMAND ----------

df7.show()

# COMMAND ----------

df8 = df6.join(df7, ["dept_name", "max(salary)"])
df8.show()

# COMMAND ----------

# Q5
df.select("dept_name", "title")\
.groupby("title")\
.count()\
.show()

# COMMAND ----------

df10 = df.select("dept_name", "title", "salary").groupby("dept_name", "title").count()
df10.show()

# COMMAND ----------

df10.orderBy(df10['count'].desc()).limit(10).show()

# COMMAND ----------


