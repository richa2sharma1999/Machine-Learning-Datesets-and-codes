Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import json
>>> data1=open("C:\\Users\\Richa Sharma\\Desktop\\z\\file1.json","r")

>>> data2=open("C:\\Users\\Richa Sharma\\Desktop\\z\\file2.json","r")
>>> data3=open("C:\\Users\\Richa Sharma\\Desktop\\z\\file3.json","r")
>>> data4=open("C:\\Users\\Richa Sharma\\Desktop\\z\\file4.json","r")
>>> data5=open("C:\\Users\\Richa Sharma\\Desktop\\z\\file5.json","r")
>>> mydata1=json.loads(data1.readlines()[0])
>>> mydata2=json.loads(data2.readlines()[0])
>>> mydata3=json.loads(data3.readlines()[0])
>>> mydata4=json.loads(data4.readlines()[0])
>>> mydata5=json.loads(data5.readlines()[0])

>>> mydata1.keys()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    mydata1.keys()
AttributeError: 'list' object has no attribute 'keys'
>>> mydata1[0].keys()
dict_keys(['results_found', 'restaurants', 'results_shown', 'results_start'])
>>> mydata1[1].keys()
dict_keys(['results_found', 'restaurants', 'results_shown', 'results_start'])
>>> mydata1[2].keys()
dict_keys(['results_found', 'restaurants', 'results_shown', 'results_start'])
>>> len(mydata1)
479
>>> mydata1[478].keys()
dict_keys(['message', 'code', 'status'])
>>> mydata1[477].keys()
dict_keys(['message', 'code', 'status'])
>>> mydata1[470].keys()
dict_keys(['message', 'code', 'status'])
>>> 
