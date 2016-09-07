# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> **Similarities**: 
- Lists and tuples both store a list of information. 
- Each value is numbered starting from zero for both lists and tuples 
- Recalling values from ilsts is exactly the same as you do with tuples ("print VARIABLENAME").  

>> **Differences**: 
- List is mutable and tuples is immutable. In other words, you can't change the values of tuples. 
- List is created using brackets and tuples using parentheses 

>> #### Tuples can be used as keys to dictionaries, while lists cannot. This is because to be used as a dictionary key, an object must support the hash function (e.g., through_hash_). Because lists are containers, hashing lists by their id would produce unexpected behavior. 
---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>>**Similarities** 
- Lists and sets both contain a list or collection of items 
- Lists and sets can store any type of data 

>> **Differences**: 
- **Sets** do not allow duplicates, while **lists** do. 
- A list keeps order, while a set doesn't. 
- Set requires items to be hashable, while list doesn't. If you have non-hashable items, then you cannot use set and must use list. 

>> **Examples**: 
- **Set**: when you want the set of all the words used in a document 
- **List**: when you want to append new phone numbers to an ordered list 

>> - For iterating, **lists** are faster. **Sets** are faster when it comes to determining if an object is present or when storing unique values to check for their existence. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> **Lambda** allows you to have anonymous functions (functions with no names). It is essentially a one-statement function. 

>> **Example**: 
```
student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)] 
sorted(student_tuples, key=lambda student: student[2])
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> **List comprehension**: List comprehensions are a tool for transforming one list into another list. Every list comprehension can be rewritten as a for loop but not every for loop can be rewritten as a list comprehension.

>>- **Map and Filter Example**: 
```
numbers = [1,2,3,4,5] 
doubled_odds = map(lambda n: n * 2, filter(lambda n: n % 2 == 1, numbers))
doubled_odds = [n * 2 for n in numbers if n % 2 == 1]
```

>>- **List Comprehension Example**: 
```
numbers = [1, 2, 3, 4, 5]
doubled_odds = [n * 2 for n in numbers if n % 2 == 1]
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





