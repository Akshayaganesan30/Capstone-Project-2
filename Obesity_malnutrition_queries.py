#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sqlalchemy import *
import matplotlib.pyplot as plt


# In[4]:


username = "root"
password = "Pgnkka#"
host = "localhost"
port = 3306
database = "obesity_malnutrition"
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# ### QUESTION 1 : Top 5 regions with the highest average obesity levels in the most recent year(2022)

def qn1():
    ans=[]
    qt1 = """SELECT AVG(Mean_Estimate),Region
             FROM obesity
             WHERE Year = 2012
             GROUP BY Region
             ORDER BY AVG(Mean_Estimate) DESC LIMIT 5
             """
    with engine.connect() as conn:
        for row in conn.execute(text(qt1)):
            ans.append(row[1])
    return pd.DataFrame({"Country":ans})

# ### QUESTION 2 : Top 5 countries with highest obesity estimates

def qn2():
    ans=[]
    qt2 = """SELECT AVG(Mean_Estimate),Country
         FROM obesity
         GROUP BY Country
         ORDER BY AVG(Mean_Estimate) DESC LIMIT 5
         """
    with engine.connect() as conn:
        for row in conn.execute(text(qt2)):
            ans.append(row[1])
    return pd.DataFrame({"Country":ans})



# ### QUESTION 3 : Obesity trend in India over the years(Mean_estimate)

def qn3():
    ans=[]
    qt3 = """SELECT Year,ROUND(AVG(Mean_Estimate),2) AS Obesity_level
             FROM obesity
             WHERE Country = "India"
             GROUP BY Year
             ORDER BY Year
             """
    with engine.connect() as conn:
        for row in conn.execute(text(qt3)):
            ans.append(row._mapping)
    return ans

# ### QUESTION 4 : Average obesity by gender

def qn4():
    ans=[]
    qt4 = """SELECT Gender,ROUND(AVG(Mean_Estimate),2) AS Avg_Obesity
             FROM obesity
             GROUP BY Gender
             """
    with engine.connect() as conn:
        for row in conn.execute(text(qt4)):
            ans.append(row._mapping)
    return ans


# ### QUESTION 5 : Country count by obesity level category and age group

def qn5():
    ans=[]
    qt5 = """SELECT COUNT(Country) as No_of_Countries,Obesity_Level,Age_group
             FROM obesity
             GROUP BY Obesity_Level,Age_group
             ORDER BY Age_group
             """
    with engine.connect() as conn:
        for row in conn.execute(text(qt5)):
            ans.append(row._mapping)
    return ans

# ### QUESTION 6 : Top 5 countries least reliable countries(with highest CI_Width) and Top 5 most consistent countries (smallest average CI_Width)

def qn6():
    ans=[]
    ans1=[]
    qt6 = """SELECT Country
         FROM obesity
         GROUP BY Country
         ORDER BY AVG(CI_width) DESC LIMIT 5"""
    with engine.connect() as conn:
        for row in conn.execute(text(qt6)):
            ans.append(row._mapping)
    qt6a = """SELECT Country
         FROM obesity
         GROUP BY Country
         ORDER BY AVG(CI_width) LIMIT 5"""
    with engine.connect() as conn:
        for row in conn.execute(text(qt6a)):
            ans1.append(row._mapping)
    return ans,ans1


# ### QUESTION 7 : Average obesity by age group

def qn7():
    ans=[]
    qt7 = """SELECT ROUND(AVG(Mean_Estimate),2) AS Average_obesity,Age_group
             FROM obesity
             GROUP BY Age_group"""
    with engine.connect() as conn:
        for row in conn.execute(text(qt7)):
            ans.append(row._mapping)
    return ans


# ### QUESTION 8 : Top 10 Countries with consistent low obesity (low average + low CI)over the years

def qn8():
    ans=[]
    qt8 = """SELECT A.Country FROM
             (SELECT Country,AVG(Mean_Estimate),AVG(CI_width)
             FROM obesity
             GROUP BY Country
             ORDER BY AVG(Mean_Estimate),AVG(CI_width) ASC LIMIT 10) AS A
             """
    with engine.connect() as conn:
        for row in conn.execute(text(qt8)):
            ans.append(row[0])
    return pd.DataFrame({"Country":ans})

# ### QUESTION 9 : Countries where female obesity exceeds male by large margin (same       year)

def qn9():
    ans = []
    qt9 = """SELECT A.Country
             FROM
             (SELECT ROUND(AVG(Mean_Estimate),2) as Female_Ob,Year,Country
             FROM obesity
             WHERE Gender = 'Female'
             GROUP BY Gender,Year,Country
             ORDER BY Country,Year) AS a
             LEFT OUTER JOIN
             (SELECT ROUND(AVG(Mean_Estimate),2) as Male_Ob,Year,Country
             FROM obesity
             WHERE Gender = 'Male'
             GROUP BY Gender,Year,Country
             ORDER BY Country,Year) AS B
             ON A.Country = B.Country
             AND A.Year = B.Year
             WHERE A.Female_Ob>B.Male_Ob
             """
    with engine.connect() as conn:
        for row in conn.execute(text(qt9)):
            if row[0] not in ans:
                ans.append(row[0])
    return ans


# ### QUESTION 10 : Global average obesity percentage per year
def qn10():
    ans=[]
    qt10 = """SELECT Year,AVG(Mean_Estimate) as Obesity_Percentage
              FROM obesity
              GROUP BY Year
              ORDER BY Year
              """
    with engine.connect() as conn:
        for row in conn.execute(text(qt10)):
            ans.append(row._mapping)
    return ans

############################################################################################################################################

                     ##### MALNUTRITION QUERIES

############################################################################################################################################

# ### QUESTION 1 : Avg. malnutrition by age group

def qn11():
    ans=[]
    qt11 = """SELECT ROUND(AVG(Mean_Estimate),2) as Average_Malnutrition,Age_group
              FROM malnutrition
              GROUP BY Age_group
              """
    with engine.connect() as conn:
        for row in conn.execute(text(qt11)):
            ans.append(row._mapping)
    return ans


# ### QUESTION 2 : Top 5 countries with highest malnutrition(mean_estimate)

def qn12():
    ans=[]
    qt12 = """SELECT Country,AVG(Mean_Estimate)
              FROM malnutrition
              GROUP BY Country
              ORDER BY AVG(Mean_Estimate) DESC LIMIT 5
              """
    with engine.connect() as conn:
        for row in conn.execute(text(qt12)):
            ans.append(row[0])
    return pd.DataFrame({"Country":ans})


# ### QUESTION 3 : Malnutrition trend in African region over the years

def qn13():
    ans=[]
    qt13 = """SELECT ROUND(AVG(Mean_Estimate),2) AS Malnutrition_Level,Year
              FROM malnutrition
              WHERE Region ='Africa'
              GROUP BY Year
              ORDER BY Year
              """
    with engine.connect() as conn:
        for row in conn.execute(text(qt13)):
            ans.append(row)
    return ans


# ### QUESTION 4 : Gender-based average malnutrition

def qn14():
    ans=[]
    qt14 = """SELECT ROUND(AVG(Mean_Estimate),2) as Average_Malnutrition,Gender
              FROM Malnutrition
              GROUP BY Gender
              """
    with engine.connect() as conn:
        for row in conn.execute(text(qt14)):
            ans.append(row._mapping)
    return ans


# ### QUESTION 5 : Malnutrition level-wise (average CI_Width by age group)

def qn15():
    ans=[]
    qt15 = """SELECT ROUND(AVG(CI_width),2) AS Malnutrition_Level,Age_group
              FROM malnutrition
              GROUP BY Age_group"""
    with engine.connect() as conn:
        for row in conn.execute(text(qt15)):
            ans.append(row._mapping)
    return ans

# ### QUESTION 6 : Yearly malnutrition change in specific countries(India, Nigeria, Brazil)

def qn16():
    ans=[]
    qt16 = """SELECT ROUND(AVG(Mean_Estimate),2) AS Malnutrition_Level,Year,Country
              FROM malnutrition
              WHERE Country = 'India' or Country ='Nigeria' or Country = 'Brazil'
              GROUP BY Year,Country
              ORDER BY Country,Year
              """
    with engine.connect() as conn:
        for row in conn.execute(text(qt16)):
            ans.append(row._mapping)
    return ans


# ### QUESTION 7 : Regions with lowest malnutrition averages

def qn17():
    ans=[]
    qt17 = """SELECT Region
              FROM malnutrition
              GROUP BY Region
              ORDER BY AVG(Mean_Estimate) LIMIT 3
              """
    with engine.connect() as conn:
        for row in conn.execute(text(qt17)):
            ans.append(row._mapping)
    return ans


# ### QUESTION 8 : Countries with increasing malnutrition 
# ### (Use MIN() and MAX() on Mean_Estimate per country to compare early vs. recent malnutrition levels, and filter 
# ### where the difference is positive using HAVING.)

def qn18():
    ans=[]
    qt18 = """SELECT A.Country FROM
          (SELECT ROUND(MIN(Mean_Estimate),2) AS Nutrition_Level_Min_2012,
                 ROUND(MAX(Mean_Estimate),2) AS Nutrition_Level_Max_2012,
                 Country
          FROM malnutrition
          WHERE Year = 2012
          GROUP BY Country,Year
          ORDER BY Country,Year) AS A
          INNER JOIN
          (SELECT ROUND(MIN(Mean_Estimate),2) AS Nutrition_Level_Min_2022,
                 ROUND(MAX(Mean_Estimate),2) AS Nutrition_Level_Max_2022,
                 Country
          FROM malnutrition
          WHERE Year = 2022
          GROUP BY Country,Year
          ORDER BY Country,Year) AS B
          ON A.Country = B.Country
          WHERE Nutrition_Level_Max_2022 > Nutrition_Level_Max_2012
          AND Nutrition_Level_Min_2022 > Nutrition_Level_Min_2012
          """
    with engine.connect() as conn:
        for row in conn.execute(text(qt18)):
            ans.append(row[0])
    return pd.DataFrame({"Country":ans})


# ### QUESTION 9 :  Min/Max malnutrition levels year-wise comparison

# In[332]:

def qn19():
    ans=[]
    qt19 = """SELECT MIN(Mean_Estimate) as Malnutrition_Level_Min,
                     MAX(Mean_Estimate) as Malnutrition_Level_Max,
                     Year
              FROM malnutrition
              GROUP BY Year
              ORDER BY Year
              """
    with engine.connect() as conn:
        for row in conn.execute(text(qt19)):
            ans.append(row._mapping)
    return ans
                

# ### QUESTION 10 : High CI_Width flags for monitoring(CI_width > 5)

# In[529]:

def qn20():
    ans=[]
    qt20 = """SELECT *
              FROM malnutrition
              WHERE CI_width > 5
              """
    with engine.connect() as conn:
        for row in conn.execute(text(qt20)):
            ans.append(row)
    return ans

############################################################################################################################################

                                    #### QUERIES BASED ON BOTH TABLE COMBINED

############################################################################################################################################

# ### QUESTION 1 : Obesity vs malnutrition comparison by country(any 5 countries)

def qn21():
    ans=[]
    qt21="""SELECT o.Country,AVG(o.mean_Estimate) as Obesity,AVG(ml.Mean_Estimate) as Malnutrition
             FROM obesity as o
             INNER JOIN malnutrition as ml
             ON o.Country=ml.Country
             WHERE o.Country IN ('India',"China","Germany","Japan","Americas Region")
             GROUP BY o.Country
             """
    with engine.connect() as conn:
        for row in conn.execute(text(qt21)):
            ans.append(row._mapping)
    return ans


# ### QUESTION 2 : Gender-based disparity in both obesity and malnutrition

def qn22():
    dis_lt=[]
    qt22 = """SELECT A.Gender,Obesity,Malnutrition
              FROM
              (SELECT ROUND(AVG(Mean_Estimate),2) as Obesity,Gender
              FROM obesity
              GROUP BY Gender) AS A
              INNER JOIN
              (SELECT ROUND(AVG(Mean_Estimate),2) as Malnutrition,Gender
              FROM malnutrition
              GROUP BY Gender) AS B
              ON A.Gender = B.Gender
              """
    with engine.connect() as conn:
        for row in conn.execute(text(qt22)):
            dis_lt.append(row._mapping)
    return pd.DataFrame(dis_lt)


# ### QUESTION 3 : Region-wise avg estimates side-by-side(Africa and America)

def qn23():
    ans=[]
    qt23 = """SELECT o.Region,AVG(o.Mean_Estimate) as obesity,AVG(ml.Mean_Estimate) as Malnutrition
              FROM obesity as o
              INNER JOIN malnutrition as ml
              on o.Region = ml.Region
              WHERE o.Region IN ("Africa","Americas")
              GROUP BY Region
              """
    with engine.connect() as conn:
        for row in conn.execute(text(qt23)):
            ans.append(row._mapping)
    return ans


# ### QUESTION 4 : Countries with obesity up & malnutrition down

def qn24():
    qt24 = """SELECT o.Country,AVG(o.Mean_Estimate) as Obesity_Value,
                     AVG(ml.Mean_Estimate) as Malnutrition_Value
              FROM obesity as o
              INNER JOIN malnutrition as ml
              ON o.Country = mL.Country
              GROUP BY Country
              """
    with engine.connect() as conn:
        op_list=[]
        for row in conn.execute(text(qt24)):
            if row[1]>row[2]:
                op_list.append(row[0])
            #print(row)
            #print(row._mapping)
    return pd.DataFrame({"Country":op_list})

# ### QUESTION 5 : Age-wise trend analysis

def qn25():
    qt25 = """SELECT ROUND(AVG(Mean_Estimate),2),"Obesity" as Record_Type,Age_group,Year
              FROM obesity
              GROUP BY Year,Age_Group
              UNION ALL
              SELECT ROUND(AVG(Mean_Estimate),2),"Malnutrition" as Record_Type,Age_group,Year
              FROM malnutrition
              GROUP BY Year,Age_Group
              ORDER BY Year
              """
    with engine.connect() as conn:
        yr=[]
        ob_chd = []
        ob_adt = []
        ml_chd = []
        ml_adt = []
        for row in conn.execute(text(qt25)):
            if(row[1] == 'Obesity' and row[2] =='Child'):
                ob_chd.append(row[0])
                yr.append(row[3])
            if(row[1] == 'Obesity' and row[2] =='Adult'):
                ob_adt.append(row[0])
            if(row[1] == 'Malnutrition' and row[2] =='Child'):
                ml_chd.append(row[0])
            if(row[1] == 'Malnutrition' and row[2] =='Adult'):
                ml_adt.append(row[0])
        return yr,ob_chd,ob_adt,ml_chd,ml_adt




