Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=1/0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=1/0
ZeroDivisionError: division by zero
>>> try
SyntaxError: invalid syntax
>>> try:
	a=1/0
except ZeroDivisionError
SyntaxError: invalid syntax
>>> try:
	a=1/0
except ZeroDivisionError:
	print('bhagyashree')

bhagyashree
>>> try:
	a=1/0
except ZeroDivisionError:
	print('error')

error
>>> try:
	list[1,2,3,4]
	print(list[20])
except IndexError:
	print("error")

	
Traceback (most recent call last):
  File "<pyshell#21>", line 2, in <module>
    list[1,2,3,4]
TypeError: 'type' object is not subscriptable
>>> try:
	list[1,2,3,4]
	print(list[20])
except IndexError:
	print("error")
else:
	print('error')

	
Traceback (most recent call last):
  File "<pyshell#25>", line 2, in <module>
    list[1,2,3,4]
TypeError: 'type' object is not subscriptable
>>> try:
	list[1,2,3,4]
	print(list[20])
except IndexError:
	print("error")
else:
	print('error')

Traceback (most recent call last):
  File "<pyshell#27>", line 2, in <module>
    list[1,2,3,4]
TypeError: 'type' object is not subscriptable
>>> try:
	list=[1,2,3,4]
	print(list[20])
except IndexError:
	print("error")

	
error
>>> try:
	list=[1,2,3,4]
	print(list[1])
except IndexError:
	print("error")
else:
	print('no error')
finally:
	print('finally')

2
no error
finally
>>> try:
	list=[1,2,3,4]
	print(list[9])
except IndexError:
	print("error")
else:
	print('no error')
finally:
	print('finally')

	
error
finally
>>> import sys
>>> sys.path
['', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\idlelib', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages']
>>> try:
	import sys
	sys.path
except IndexError:
	print('index error')
except ZeroDivisionError:
	print('zero division error')
else:
	print('no  error')
finally:
	print("no error")

['', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\idlelib', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages']
no  error
no error
>>> import sys
>>> print(sys.path)
['', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\idlelib', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages']
>>> try:
	import sys
	sys.path
except IndexError:
	print('index error')
except ZeroDivisionError:
	print('zero division error')
else:
	print('no  error')
finally:
	print("no error")

['', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\idlelib', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32', 'C:\\Users\\Richa Sharma\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages']
no  error
no error
>>> l=['b',0,2]
>>> for i in range(len(l)):
	a[i]=1/l[i]
	sys.exe_info

Traceback (most recent call last):
  File "<pyshell#61>", line 2, in <module>
    a[i]=1/l[i]
TypeError: unsupported operand type(s) for /: 'int' and 'str'
>>> for i in range(len(l)):
	a[i]=1/l[i]
	sys.exc_info

Traceback (most recent call last):
  File "<pyshell#63>", line 2, in <module>
    a[i]=1/l[i]
TypeError: unsupported operand type(s) for /: 'int' and 'str'
>>> for i in range(len(l)):
	a[i]=1/l[i]

Traceback (most recent call last):
  File "<pyshell#64>", line 2, in <module>
    a[i]=1/l[i]
TypeError: unsupported operand type(s) for /: 'int' and 'str'
>>> for i in range(len(l)):
	a[i]=1/l[i]
sys.exc_info()
SyntaxError: invalid syntax
>>> l.reciprocal()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    l.reciprocal()
AttributeError: 'list' object has no attribute 'reciprocal'
>>> l.reciprocal(0)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    l.reciprocal(0)
AttributeError: 'list' object has no attribute 'reciprocal'
>>> import sys
>>> sys.exc_info()
(None, None, None)
>>> for i in range(len(l)):
	a[i]=1/l[i]
	import sys
	sys.exe_info()

Traceback (most recent call last):
  File "<pyshell#72>", line 2, in <module>
    a[i]=1/l[i]
TypeError: unsupported operand type(s) for /: 'int' and 'str'
>>> for i in range(len(l)):
	a[i]=1/l[i]
	import sys
	sys.exc_info()

Traceback (most recent call last):
  File "<pyshell#74>", line 2, in <module>
    a[i]=1/l[i]
TypeError: unsupported operand type(s) for /: 'int' and 'str'
>>> a=1/0
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a=1/0
ZeroDivisionError: division by zero
>>> sys.exc_info()
(None, None, None)
>>> for i in range(len(l)):
	a[i]=1/l[i]
	import sys
	sys.exe_info()

Traceback (most recent call last):
  File "<pyshell#78>", line 2, in <module>
    a[i]=1/l[i]
TypeError: unsupported operand type(s) for /: 'int' and 'str'
>>> for i in range(len(l)):
	try:
		a[i]=1/l[i]
	except:
		sys.exe_info()

Traceback (most recent call last):
  File "<pyshell#80>", line 3, in <module>
    a[i]=1/l[i]
TypeError: unsupported operand type(s) for /: 'int' and 'str'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#80>", line 5, in <module>
    sys.exe_info()
AttributeError: module 'sys' has no attribute 'exe_info'
>>> for i in range(len(l)):
	try:
		a[i]=1/l[i]
	except sys.exc_info():
		print("error")

Traceback (most recent call last):
  File "<pyshell#83>", line 3, in <module>
    a[i]=1/l[i]
TypeError: unsupported operand type(s) for /: 'int' and 'str'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#83>", line 4, in <module>
    except sys.exc_info():
TypeError: catching classes that do not inherit from BaseException is not allowed
>>> try:
	a=1/0
except sys.exc_info():
	print("error")

Traceback (most recent call last):
  File "<pyshell#85>", line 2, in <module>
    a=1/0
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#85>", line 3, in <module>
    except sys.exc_info():
TypeError: catching classes that do not inherit from BaseException is not allowed
>>> try:
	list=[1,2,3,4]
	print(list[9])
except sys.exc_info():
	print("error")
else:
	print('no error')
finally:
	print('finally')

	
finally
Traceback (most recent call last):
  File "<pyshell#87>", line 3, in <module>
    print(list[9])
IndexError: list index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#87>", line 4, in <module>
    except sys.exc_info():
TypeError: catching classes that do not inherit from BaseException is not allowed
>>> for i in range(len(l)):
	try:
		print(1/l[i])
	except:
		sys.exc_info()

		
(<class 'TypeError'>, TypeError("unsupported operand type(s) for /: 'int' and 'str'",), <traceback object at 0x05FB0C60>)
(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero',), <traceback object at 0x05FB0C88>)
0.5
>>> for i in range(len(l)):
	try:
		a[i]=(1/l[i])
		print (a[i])
	except:
		sys.exc_info()

		
(<class 'TypeError'>, TypeError("unsupported operand type(s) for /: 'int' and 'str'",), <traceback object at 0x05FB0C38>)
(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero',), <traceback object at 0x05FB0E40>)
(<class 'NameError'>, NameError("name 'a' is not defined",), <traceback object at 0x05FB0C38>)
>>> for i in range(len(l)):
	try:
		a=(1/l[i])
		print (a)
	except:
		sys.exc_info()

		
(<class 'TypeError'>, TypeError("unsupported operand type(s) for /: 'int' and 'str'",), <traceback object at 0x05FB0D50>)
(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero',), <traceback object at 0x05FB0EB8>)
0.5
>>> a=[]
>>> for i in range(len(l)):
	try:
		a[i]=(1/l[i])
		print (a[i])
	except:
		sys.exc_info()

		
(<class 'TypeError'>, TypeError("unsupported operand type(s) for /: 'int' and 'str'",), <traceback object at 0x05FB0C38>)
(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero',), <traceback object at 0x05FB0C88>)
(<class 'IndexError'>, IndexError('list assignment index out of range',), <traceback object at 0x05FB0C38>)
>>> for i in range(len(l)-1):
	try:
		a[i]=(1/l[i])
		print (a[i])
	except:
		sys.exc_info()

		
(<class 'TypeError'>, TypeError("unsupported operand type(s) for /: 'int' and 'str'",), <traceback object at 0x05FB0E40>)
(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero',), <traceback object at 0x05FB0E18>)
>>> for i in range(1,len(l)):
	try:
		a[i]=(1/l[i])
		print (a[i])
	except:
		sys.exc_info()

		
(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero',), <traceback object at 0x05FB0EB8>)
(<class 'IndexError'>, IndexError('list assignment index out of range',), <traceback object at 0x05FB0E18>)
>>> for i in range(len(l)):
	try:
		a=(1/l[i])
		print (a)
	except:
		sys.exc_info(0)

		
Traceback (most recent call last):
  File "<pyshell#103>", line 3, in <module>
    a=(1/l[i])
TypeError: unsupported operand type(s) for /: 'int' and 'str'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#103>", line 6, in <module>
    sys.exc_info(0)
TypeError: exc_info() takes no arguments (1 given)
>>> 
>>> for i in range(len(l)):
	try:
		a=(1/l[i])
		print (a)
	except:
		sys.exc_info()

		
(<class 'TypeError'>, TypeError("unsupported operand type(s) for /: 'int' and 'str'",), <traceback object at 0x05FB0800>)
(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero',), <traceback object at 0x05FB0E18>)
0.5
>>> for i in range(len(l)):
	try:
		a=(1/l[i])
		print (a)
	except:
		sys.exc_info('0')

		
Traceback (most recent call last):
  File "<pyshell#108>", line 3, in <module>
    a=(1/l[i])
TypeError: unsupported operand type(s) for /: 'int' and 'str'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#108>", line 6, in <module>
    sys.exc_info('0')
TypeError: exc_info() takes no arguments (1 given)
>>> for i in range(len(l)):
	try:
		a=(1/l[i])
		print (a[0])
	except:
		sys.exc_info()

		
(<class 'TypeError'>, TypeError("unsupported operand type(s) for /: 'int' and 'str'",), <traceback object at 0x05FB0E40>)
(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero',), <traceback object at 0x05FB0E18>)
(<class 'TypeError'>, TypeError("'float' object is not subscriptable",), <traceback object at 0x05FB0E40>)
>>> for i in range(len(l)):
	try:
		a=(1/l[i])
		print (a)
	except:
		sys.exc_info()[0]

		
<class 'TypeError'>
<class 'ZeroDivisionError'>
0.5
>>> open("C:\Users\Richa Sharma\Desktop.json","r")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> open("C:\\Users\\Richa Sharma\\Desktop.json","r")
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    open("C:\\Users\\Richa Sharma\\Desktop.json","r")
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Richa Sharma\\Desktop.json'
>>> open("C:\\Users\\Richa Sharma\\Desktop\\json","r")
<_io.TextIOWrapper name='C:\\Users\\Richa Sharma\\Desktop\\json' mode='r' encoding='cp1252'>
>>> import json
>>> data=json.readlines()
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    data=json.readlines()
AttributeError: module 'json' has no attribute 'readlines'
>>> json.readlines
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    json.readlines
AttributeError: module 'json' has no attribute 'readlines'
>>> json.readlines()
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    json.readlines()
AttributeError: module 'json' has no attribute 'readlines'
>>> data=open("C:\\Users\\Richa Sharma\\Desktop\\json","r")
>>> data=open("C:\\Users\\Richa Sharma\\Desktop\\json.json","r")
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    data=open("C:\\Users\\Richa Sharma\\Desktop\\json.json","r")
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Richa Sharma\\Desktop\\json.json'
>>> data=open("C:\\Users\\Richa Sharma\\Desktop\\json","r")
>>> mydata=json.loads(data.readlines()[0])
>>> mydata
{'fields': [{'id': 'a', 'label': 'State', 'type': 'string'}, {'id': 'b', 'label': 'Professor and Equivalent - Male', 'type': 'string'}, {'id': 'c', 'label': 'Professor and Equivalent - Female', 'type': 'string'}, {'id': 'd', 'label': 'Professor and Equivalent - Total', 'type': 'string'}, {'id': 'e', 'label': 'Reader and Associate Professor - Male', 'type': 'string'}, {'id': 'f', 'label': 'Reader and Associate Professor - Female', 'type': 'string'}, {'id': 'g', 'label': 'Reader and Associate Professor - Total', 'type': 'string'}, {'id': 'h', 'label': 'Lecturer/ Assistant Professor - Male', 'type': 'string'}, {'id': 'i', 'label': 'Lecturer/ Assistant Professor - Female', 'type': 'string'}, {'id': 'j', 'label': 'Lecturer/ Assistant Professor - Total', 'type': 'string'}, {'id': 'k', 'label': 'Demonstrator/ Tutor - Male', 'type': 'string'}, {'id': 'l', 'label': 'Demonstrator/ Tutor - Female', 'type': 'string'}, {'id': 'm', 'label': 'Demonstrator/ Tutor - Total', 'type': 'string'}, {'id': 'n', 'label': 'Temporary Teacher etc - Male', 'type': 'string'}, {'id': 'o', 'label': 'Temporary Teacher etc - Female', 'type': 'string'}, {'id': 'p', 'label': 'Temporary Teacher etc - Total', 'type': 'string'}, {'id': 'q', 'label': 'Grand Total - Male', 'type': 'string'}, {'id': 'r', 'label': 'Grand Total - Female', 'type': 'string'}, {'id': 's', 'label': 'Grand Total - Total', 'type': 'string'}], 'data': [['Andaman and Nicobar Islands', '5', '0', '5', '32', '2', '34', '47', '28', '75', '5', '1', '6', '15', '21', '36', '104', '52', '156'], ['Andhra Pradesh', '12297', '3960', '16257', '11862', '4566', '16428', '62414', '35589', '98003', '1001', '3779', '4780', '4638', '3014', '7652', '92212', '50908', '143120'], ['Arunachal Pradesh', '215', '34', '249', '282', '38', '320', '1128', '251', '1379', '0', '0', '0', '6', '14', '20', '1631', '337', '1968'], ['Assam', '672', '164', '836', '1555', '822', '2377', '3078', '1785', '4863', '223', '278', '501', '386', '290', '676', '5914', '3339', '9253'], ['Bihar', '2162', '320', '2482', '4040', '634', '4674', '12433', '2403', '14836', '808', '192', '1000', '1736', '372', '2108', '21179', '3921', '25100'], ['Chandigarh', '126', '74', '200', '209', '261', '470', '344', '494', '838', '3', '5', '8', '65', '134', '199', '747', '968', '1715'], ['Chhatisgarh', '718', '239', '957', '913', '449', '1362', '4609', '3308', '7917', '142', '160', '302', '869', '753', '1622', '7251', '4909', '12160'], ['Dadra and Nagar Haveli', '1', '2', '3', '0', '0', '0', '26', '9', '35', '1', '5', '6', '0', '0', '0', '28', '16', '44'], ['Daman and Diu', '3', '1', '4', '13', '4', '17', '18', '8', '26', '0', '0', '0', '83', '24', '107', '117', '37', '154'], ['Delhi', '1490', '552', '2042', '1965', '2087', '4052', '3053', '3671', '6724', '164', '460', '624', '439', '499', '938', '7111', '7269', '14380'], ['Goa', '106', '35', '141', '252', '203', '455', '342', '447', '789', '37', '43', '80', '153', '319', '472', '890', '1047', '1937'], ['Gujarat', '3273', '1292', '4565', '4611', '1953', '6564', '18321', '10346', '28667', '1186', '1093', '2279', '3521', '1895', '5416', '30912', '16579', '47491'], ['Haryana', '1605', '433', '2038', '1099', '767', '1866', '6914', '4451', '11365', '480', '272', '752', '520', '875', '1395', '10618', '6798', '17416'], ['Himachal Pradesh', '737', '267', '1004', '676', '265', '941', '2598', '1947', '4545', '84', '112', '196', '435', '301', '736', '4530', '2892', '7422'], ['Jammu and Kashmir', '306', '205', '511', '469', '218', '687', '1309', '1520', '2829', '63', '51', '114', '653', '508', '1161', '2800', '2502', '5302'], ['Jharkhand', '241', '21', '262', '394', '112', '506', '1277', '548', '1825', '16', '4', '20', '150', '240', '390', '2078', '925', '3003'], ['Karnataka', '13148', '5687', '18835', '9807', '4424', '14231', '36968', '27531', '64499', '4545', '7299', '11844', '6686', '4842', '11528', '71154', '49783', '120937'], ['Kerala', '1743', '1484', '3227', '2905', '2293', '5198', '7004', '8977', '15981', '613', '1933', '2546', '953', '1958', '2911', '13218', '16645', '29863'], ['Lakshadweep', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['Madhya Pradesh', '1403', '704', '2107', '531', '242', '773', '3916', '2503', '6419', '280', '437', '717', '564', '331', '895', '6694', '4217', '10911'], ['Maharashtra', '7059', '2318', '9377', '9320', '3202', '12522', '33293', '19475', '52768', '1526', '1329', '2855', '5442', '3951', '9393', '56640', '30275', '86915'], ['Manipur', '125', '33', '158', '307', '155', '462', '506', '339', '845', '53', '33', '86', '66', '100', '166', '1057', '660', '1717'], ['Meghalaya', '66', '43', '109', '125', '96', '221', '543', '709', '1252', '5', '63', '68', '46', '58', '104', '785', '969', '1754'], ['Mizoram', '50', '12', '62', '287', '141', '428', '312', '255', '567', '7', '48', '55', '88', '85', '173', '744', '541', '1285'], ['Nagaland', '80', '9', '89', '144', '95', '239', '704', '806', '1510', '8', '2', '10', '78', '59', '137', '1014', '971', '1985'], ['Odisha', '1392', '287', '1679', '1632', '587', '2219', '9857', '4086', '13943', '813', '293', '1106', '589', '271', '860', '14283', '5524', '19807'], ['Puducherry', '444', '130', '574', '477', '208', '685', '1545', '1077', '2622', '217', '128', '345', '86', '56', '142', '2769', '1599', '4368'], ['Punjab', '1439', '482', '1921', '1438', '870', '2308', '9751', '6099', '15850', '359', '545', '904', '518', '632', '1150', '13505', '8628', '22133'], ['Rajasthan', '2222', '534', '2756', '1247', '519', '1766', '11173', '6800', '17973', '61', '20', '81', '490', '390', '880', '15193', '8263', '23456'], ['Sikkim', '61', '5', '66', '62', '35', '97', '292', '196', '488', '30', '37', '67', '24', '37', '61', '469', '310', '779'], ['Tamil Nadu', '6583', '2157', '8740', '4148', '2316', '6464', '38105', '27967', '66072', '979', '714', '1693', '905', '1060', '1965', '50720', '34214', '84934'], ['Tripura', '201', '44', '245', '121', '61', '182', '730', '372', '1102', '111', '115', '226', '187', '142', '329', '1350', '734', '2084'], ['Uttar Pradesh', '3791', '826', '4617', '3641', '1580', '5221', '10992', '5567', '16559', '639', '273', '912', '2266', '1250', '3516', '21329', '9496', '30825'], ['Uttrakhand', '1234', '246', '1480', '759', '369', '1128', '2796', '1550', '4346', '382', '322', '704', '807', '452', '1259', '5978', '2939', '8917'], ['West Bengal', '2374', '426', '2800', '2404', '991', '3395', '7593', '3176', '10769', '953', '323', '1276', '2207', '1611', '3818', '15531', '6527', '22058']]}
>>> mydata.split('[]')
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    mydata.split('[]')
AttributeError: 'dict' object has no attribute 'split'
>>> data2=mydata.keys('data')
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    data2=mydata.keys('data')
TypeError: keys() takes no arguments (1 given)
>>> data2=mydata.keys['data']
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    data2=mydata.keys['data']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> mydata.keys['data']
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    mydata.keys['data']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> mydata['data']
[['Andaman and Nicobar Islands', '5', '0', '5', '32', '2', '34', '47', '28', '75', '5', '1', '6', '15', '21', '36', '104', '52', '156'], ['Andhra Pradesh', '12297', '3960', '16257', '11862', '4566', '16428', '62414', '35589', '98003', '1001', '3779', '4780', '4638', '3014', '7652', '92212', '50908', '143120'], ['Arunachal Pradesh', '215', '34', '249', '282', '38', '320', '1128', '251', '1379', '0', '0', '0', '6', '14', '20', '1631', '337', '1968'], ['Assam', '672', '164', '836', '1555', '822', '2377', '3078', '1785', '4863', '223', '278', '501', '386', '290', '676', '5914', '3339', '9253'], ['Bihar', '2162', '320', '2482', '4040', '634', '4674', '12433', '2403', '14836', '808', '192', '1000', '1736', '372', '2108', '21179', '3921', '25100'], ['Chandigarh', '126', '74', '200', '209', '261', '470', '344', '494', '838', '3', '5', '8', '65', '134', '199', '747', '968', '1715'], ['Chhatisgarh', '718', '239', '957', '913', '449', '1362', '4609', '3308', '7917', '142', '160', '302', '869', '753', '1622', '7251', '4909', '12160'], ['Dadra and Nagar Haveli', '1', '2', '3', '0', '0', '0', '26', '9', '35', '1', '5', '6', '0', '0', '0', '28', '16', '44'], ['Daman and Diu', '3', '1', '4', '13', '4', '17', '18', '8', '26', '0', '0', '0', '83', '24', '107', '117', '37', '154'], ['Delhi', '1490', '552', '2042', '1965', '2087', '4052', '3053', '3671', '6724', '164', '460', '624', '439', '499', '938', '7111', '7269', '14380'], ['Goa', '106', '35', '141', '252', '203', '455', '342', '447', '789', '37', '43', '80', '153', '319', '472', '890', '1047', '1937'], ['Gujarat', '3273', '1292', '4565', '4611', '1953', '6564', '18321', '10346', '28667', '1186', '1093', '2279', '3521', '1895', '5416', '30912', '16579', '47491'], ['Haryana', '1605', '433', '2038', '1099', '767', '1866', '6914', '4451', '11365', '480', '272', '752', '520', '875', '1395', '10618', '6798', '17416'], ['Himachal Pradesh', '737', '267', '1004', '676', '265', '941', '2598', '1947', '4545', '84', '112', '196', '435', '301', '736', '4530', '2892', '7422'], ['Jammu and Kashmir', '306', '205', '511', '469', '218', '687', '1309', '1520', '2829', '63', '51', '114', '653', '508', '1161', '2800', '2502', '5302'], ['Jharkhand', '241', '21', '262', '394', '112', '506', '1277', '548', '1825', '16', '4', '20', '150', '240', '390', '2078', '925', '3003'], ['Karnataka', '13148', '5687', '18835', '9807', '4424', '14231', '36968', '27531', '64499', '4545', '7299', '11844', '6686', '4842', '11528', '71154', '49783', '120937'], ['Kerala', '1743', '1484', '3227', '2905', '2293', '5198', '7004', '8977', '15981', '613', '1933', '2546', '953', '1958', '2911', '13218', '16645', '29863'], ['Lakshadweep', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['Madhya Pradesh', '1403', '704', '2107', '531', '242', '773', '3916', '2503', '6419', '280', '437', '717', '564', '331', '895', '6694', '4217', '10911'], ['Maharashtra', '7059', '2318', '9377', '9320', '3202', '12522', '33293', '19475', '52768', '1526', '1329', '2855', '5442', '3951', '9393', '56640', '30275', '86915'], ['Manipur', '125', '33', '158', '307', '155', '462', '506', '339', '845', '53', '33', '86', '66', '100', '166', '1057', '660', '1717'], ['Meghalaya', '66', '43', '109', '125', '96', '221', '543', '709', '1252', '5', '63', '68', '46', '58', '104', '785', '969', '1754'], ['Mizoram', '50', '12', '62', '287', '141', '428', '312', '255', '567', '7', '48', '55', '88', '85', '173', '744', '541', '1285'], ['Nagaland', '80', '9', '89', '144', '95', '239', '704', '806', '1510', '8', '2', '10', '78', '59', '137', '1014', '971', '1985'], ['Odisha', '1392', '287', '1679', '1632', '587', '2219', '9857', '4086', '13943', '813', '293', '1106', '589', '271', '860', '14283', '5524', '19807'], ['Puducherry', '444', '130', '574', '477', '208', '685', '1545', '1077', '2622', '217', '128', '345', '86', '56', '142', '2769', '1599', '4368'], ['Punjab', '1439', '482', '1921', '1438', '870', '2308', '9751', '6099', '15850', '359', '545', '904', '518', '632', '1150', '13505', '8628', '22133'], ['Rajasthan', '2222', '534', '2756', '1247', '519', '1766', '11173', '6800', '17973', '61', '20', '81', '490', '390', '880', '15193', '8263', '23456'], ['Sikkim', '61', '5', '66', '62', '35', '97', '292', '196', '488', '30', '37', '67', '24', '37', '61', '469', '310', '779'], ['Tamil Nadu', '6583', '2157', '8740', '4148', '2316', '6464', '38105', '27967', '66072', '979', '714', '1693', '905', '1060', '1965', '50720', '34214', '84934'], ['Tripura', '201', '44', '245', '121', '61', '182', '730', '372', '1102', '111', '115', '226', '187', '142', '329', '1350', '734', '2084'], ['Uttar Pradesh', '3791', '826', '4617', '3641', '1580', '5221', '10992', '5567', '16559', '639', '273', '912', '2266', '1250', '3516', '21329', '9496', '30825'], ['Uttrakhand', '1234', '246', '1480', '759', '369', '1128', '2796', '1550', '4346', '382', '322', '704', '807', '452', '1259', '5978', '2939', '8917'], ['West Bengal', '2374', '426', '2800', '2404', '991', '3395', '7593', '3176', '10769', '953', '323', '1276', '2207', '1611', '3818', '15531', '6527', '22058']]
>>> f=mydata['data']
>>> len(f)
35
>>> mydata["data"][0]
['Andaman and Nicobar Islands', '5', '0', '5', '32', '2', '34', '47', '28', '75', '5', '1', '6', '15', '21', '36', '104', '52', '156']
>>> mydata["data"][0][0]
'Andaman and Nicobar Islands'
>>> for i in range(len(f)):
	d[mydata["data"][i][0]]=mydata[i][3]

Traceback (most recent call last):
  File "<pyshell#138>", line 2, in <module>
    d[mydata["data"][i][0]]=mydata[i][3]
KeyError: 0
>>> for i in range(len(f)):
	d[mydata["data"][i][0]]=mydata["data"][i][3]

Traceback (most recent call last):
  File "<pyshell#140>", line 2, in <module>
    d[mydata["data"][i][0]]=mydata["data"][i][3]
NameError: name 'd' is not defined
>>> d=
SyntaxError: invalid syntax
>>> d={}
>>> for i in range(len(f)):
	d[mydata["data"][i][0]]=mydata["data"][i][3]

>>> d
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
>>> for i in range(len(f)):
	d[mydata["data"][i][0]]=mydata["data"][i][3]
	print(d)

{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
{'Andaman and Nicobar Islands': '5', 'Andhra Pradesh': '16257', 'Arunachal Pradesh': '249', 'Assam': '836', 'Bihar': '2482', 'Chandigarh': '200', 'Chhatisgarh': '957', 'Dadra and Nagar Haveli': '3', 'Daman and Diu': '4', 'Delhi': '2042', 'Goa': '141', 'Gujarat': '4565', 'Haryana': '2038', 'Himachal Pradesh': '1004', 'Jammu and Kashmir': '511', 'Jharkhand': '262', 'Karnataka': '18835', 'Kerala': '3227', 'Lakshadweep': '0', 'Madhya Pradesh': '2107', 'Maharashtra': '9377', 'Manipur': '158', 'Meghalaya': '109', 'Mizoram': '62', 'Nagaland': '89', 'Odisha': '1679', 'Puducherry': '574', 'Punjab': '1921', 'Rajasthan': '2756', 'Sikkim': '66', 'Tamil Nadu': '8740', 'Tripura': '245', 'Uttar Pradesh': '4617', 'Uttrakhand': '1480', 'West Bengal': '2800'}
>>> for i in range(len(f)):
	d[mydata["data"][i][0]]=mydata["data"][i][3]+"\n"

	
>>> d
{'Andaman and Nicobar Islands': '5\n', 'Andhra Pradesh': '16257\n', 'Arunachal Pradesh': '249\n', 'Assam': '836\n', 'Bihar': '2482\n', 'Chandigarh': '200\n', 'Chhatisgarh': '957\n', 'Dadra and Nagar Haveli': '3\n', 'Daman and Diu': '4\n', 'Delhi': '2042\n', 'Goa': '141\n', 'Gujarat': '4565\n', 'Haryana': '2038\n', 'Himachal Pradesh': '1004\n', 'Jammu and Kashmir': '511\n', 'Jharkhand': '262\n', 'Karnataka': '18835\n', 'Kerala': '3227\n', 'Lakshadweep': '0\n', 'Madhya Pradesh': '2107\n', 'Maharashtra': '9377\n', 'Manipur': '158\n', 'Meghalaya': '109\n', 'Mizoram': '62\n', 'Nagaland': '89\n', 'Odisha': '1679\n', 'Puducherry': '574\n', 'Punjab': '1921\n', 'Rajasthan': '2756\n', 'Sikkim': '66\n', 'Tamil Nadu': '8740\n', 'Tripura': '245\n', 'Uttar Pradesh': '4617\n', 'Uttrakhand': '1480\n', 'West Bengal': '2800\n'}
>>> for i in range(len(f)):
	d[mydata["data"][i][0]]=mydata["data"][i][3]+\n
	
SyntaxError: unexpected character after line continuation character
>>> for i in range(len(f)):
	d[mydata["data"][i][0]]=mydata["data"][i][3]+'''
								'''

>>> d
{'Andaman and Nicobar Islands': '5\n\t\t\t\t\t\t\t\t', 'Andhra Pradesh': '16257\n\t\t\t\t\t\t\t\t', 'Arunachal Pradesh': '249\n\t\t\t\t\t\t\t\t', 'Assam': '836\n\t\t\t\t\t\t\t\t', 'Bihar': '2482\n\t\t\t\t\t\t\t\t', 'Chandigarh': '200\n\t\t\t\t\t\t\t\t', 'Chhatisgarh': '957\n\t\t\t\t\t\t\t\t', 'Dadra and Nagar Haveli': '3\n\t\t\t\t\t\t\t\t', 'Daman and Diu': '4\n\t\t\t\t\t\t\t\t', 'Delhi': '2042\n\t\t\t\t\t\t\t\t', 'Goa': '141\n\t\t\t\t\t\t\t\t', 'Gujarat': '4565\n\t\t\t\t\t\t\t\t', 'Haryana': '2038\n\t\t\t\t\t\t\t\t', 'Himachal Pradesh': '1004\n\t\t\t\t\t\t\t\t', 'Jammu and Kashmir': '511\n\t\t\t\t\t\t\t\t', 'Jharkhand': '262\n\t\t\t\t\t\t\t\t', 'Karnataka': '18835\n\t\t\t\t\t\t\t\t', 'Kerala': '3227\n\t\t\t\t\t\t\t\t', 'Lakshadweep': '0\n\t\t\t\t\t\t\t\t', 'Madhya Pradesh': '2107\n\t\t\t\t\t\t\t\t', 'Maharashtra': '9377\n\t\t\t\t\t\t\t\t', 'Manipur': '158\n\t\t\t\t\t\t\t\t', 'Meghalaya': '109\n\t\t\t\t\t\t\t\t', 'Mizoram': '62\n\t\t\t\t\t\t\t\t', 'Nagaland': '89\n\t\t\t\t\t\t\t\t', 'Odisha': '1679\n\t\t\t\t\t\t\t\t', 'Puducherry': '574\n\t\t\t\t\t\t\t\t', 'Punjab': '1921\n\t\t\t\t\t\t\t\t', 'Rajasthan': '2756\n\t\t\t\t\t\t\t\t', 'Sikkim': '66\n\t\t\t\t\t\t\t\t', 'Tamil Nadu': '8740\n\t\t\t\t\t\t\t\t', 'Tripura': '245\n\t\t\t\t\t\t\t\t', 'Uttar Pradesh': '4617\n\t\t\t\t\t\t\t\t', 'Uttrakhand': '1480\n\t\t\t\t\t\t\t\t', 'West Bengal': '2800\n\t\t\t\t\t\t\t\t'}
>>> import urllib.request
>>> 
>>> with urllib.request.urlopen("https://ekcovation.com") as resp:
	html=response.read()

Traceback (most recent call last):
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1318, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1239, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1285, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1234, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1026, in _send_output
    self.send(msg)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 964, in send
    self.connect()
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1392, in connect
    super().connect()
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 936, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\socket.py", line 704, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\socket.py", line 745, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    with urllib.request.urlopen("https://ekcovation.com") as resp:
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 526, in open
    response = self._open(req, data)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 544, in _open
    '_open', req)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 504, in _call_chain
    result = func(*args)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1361, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1320, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>
>>> with urllib.request.urlopen("https://ekcovation.com") as resp:
	html=resp.read()

	
Traceback (most recent call last):
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1318, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1239, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1285, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1234, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1026, in _send_output
    self.send(msg)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 964, in send
    self.connect()
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1392, in connect
    super().connect()
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 936, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\socket.py", line 704, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\socket.py", line 745, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    with urllib.request.urlopen("https://ekcovation.com") as resp:
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 526, in open
    response = self._open(req, data)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 544, in _open
    '_open', req)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 504, in _call_chain
    result = func(*args)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1361, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "C:\Users\Richa Sharma\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1320, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>
>>> with urllib.request.urlopen("https://google.com") as resp:
	html=resp.read()

	
>>> 
>>> html
b'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-IN"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/logos/doodles/2018/world-cup-2018-day-9-5987135852118016-5669283816275968-ssw.png" itemprop="image"><meta content="World Cup 2018 - Day 9" property="twitter:title"><meta content="Let the matches begin! Celebrate &#9917; around the &#127758;&#127757;&#127759; in today\'s #GoogleDoodle!" property="twitter:description"><meta content="Let the matches begin! Celebrate &#9917; around the &#127758;&#127757;&#127759; in today\'s #GoogleDoodle!" property="og:description"><meta content="summary_large_image" property="twitter:card"><meta content="@GoogleDoodles" property="twitter:site"><meta content="https://www.google.com/logos/doodles/2018/world-cup-2018-day-9-5987135852118016.2-2xa.gif" property="twitter:image"><meta content="https://www.google.com/logos/doodles/2018/world-cup-2018-day-9-5987135852118016.2-2xa.gif" property="og:image"><meta content="1067" property="og:image:width"><meta content="460" property="og:image:height"><meta content="https://www.google.com/logos/doodles/2018/world-cup-2018-day-9-5987135852118016.2-2xa.gif" property="og:url"><meta content="video.other" property="og:type"><title>Google</title><script nonce="T2t3DABh/+lWLoHSV/hwcQ==">(function(){window.google={kEI:\'jbssW6fEH8TrvAT_56foCw\',kEXPI:\'0,18167,183669,1151124,786,58,1958,1017,280,710,900,735,5,195,59,33,218,102,45,206,68,2339727,205,222,32,21,302968,26305,1294,12383,2349,2506,32692,15247,867,42,275,1251,7,7356,3232,6381,3335,2,2,2138,4663,364,553,664,2102,113,1149,1052,3191,224,502,5,1711,130,130,3742,886,202,2,14,261,444,131,1119,2,1306,311,3,298,1819,59,2,2,2,61,1236,1343,369,1376,507,728,377,26,1214,479,608,56,630,8,300,507,762,222,552,94,1137,1020,280,2,694,148,282,1666,35,428,330,28,850,393,132,22,180,419,5,2,2,151,506,443,392,255,550,127,2,65,3,540,397,3,391,29,32,2,238,33,108,756,508,1328,260,214,82,512,130,417,285,204,164,311,62,127,11,43,169,28,211,123,115,8,7,326,23,316,211,235,128,100,5,386,8,806,96,182,7,3,26,26,45,792,219,29,705,189,4,4,4,4,79,135,20,2,105,5,139,108,350,119,24,368,2329567,3685999,1874,671,9,5997613,2800173,4,1572,549,332,445,1,2,1,1,77,1,1,900,207,1,1,1,1,1,371,1,312,6,3,1,2,1,1,1482,41,8,7,22,19,1,17,21,1,1,1,10,5,18,10,22310272\',authuser:0,kscs:\'c9c918f0_jbssW6fEH8TrvAT_56foCw\',kGL:\'IN\'};google.kHL=\'en-IN\';})();google.time=function(){return(new Date).getTime()};(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b};google.https=function(){return"https:"==window.location.protocol};google.ml=function(){return null};google.wl=function(a,b){try{google.ml(Error(a),!1,b)}catch(d){}};google.log=function(a,b,d,c,g){if(a=google.logUrl(a,b,d,c,g)){b=new Image;var e=google.lc,f=google.li;e[f]=b;b.onerror=b.onload=b.onabort=function(){delete e[f]};google.vel&&google.vel.lu&&google.vel.lu(a);b.src=a;google.li=f+1}};google.logUrl=function(a,b,d,c,g){var e="",f=google.ls||"";d||-1!=b.search("&ei=")||(e="&ei="+google.getEI(c),-1==b.search("&lei=")&&(c=google.getLEI(c))&&(e+="&lei="+c));c="";!d&&google.cshid&&-1==b.search("&cshid=")&&"slh"!=a&&(c="&cshid="+google.cshid);a=d||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+e+f+"&zx="+google.time()+c;/^http:/i.test(a)&&google.https()&&(google.ml(Error("a"),!1,{src:a,glmm:1}),a="");return a};}).call(this);(function(){google.y={};google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};var a=window.location,b=a.href.indexOf("#");if(0<=b){var c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}\n</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}.ts td{padding:0}.ts{border-collapse:collapse}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}a.gb1,a.gb2,a.gb3,a.gb4{color:#11c !important}body{background:#fff;color:black}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}a.gb1,a.gb4{text-decoration:underline}a.gb3:hover{text-decoration:none}#ghead a.gb2:hover{color:#fff !important}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#eee;border:solid 1px;border-color:#ccc #999 #999 #ccc;height:30px}.lsbb{display:block}.ftl,#fll a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}</style><script nonce="T2t3DABh/+lWLoHSV/hwcQ=="></script><link href="/images/branding/product/ico/googleg_lodp.ico" rel="shortcut icon"></head><body bgcolor="#fff"><script nonce="T2t3DABh/+lWLoHSV/hwcQ==">(function(){var src=\'/images/nav_logo229.png\';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}\nif (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}\n}\n})();</script><div id="mngb"> <div id=gbar><nobr><b class=gb1>Search</b> <a class=gb1 href="https://www.google.co.in/imghp?hl=en&tab=wi">Images</a> <a class=gb1 href="https://maps.google.co.in/maps?hl=en&tab=wl">Maps</a> <a class=gb1 href="https://play.google.com/?hl=en&tab=w8">Play</a> <a class=gb1 href="https://www.youtube.com/?gl=IN&tab=w1">YouTube</a> <a class=gb1 href="https://news.google.co.in/nwshp?hl=en&tab=wn">News</a> <a class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a> <a class=gb1 href="https://drive.google.com/?tab=wo">Drive</a> <a class=gb1 style="text-decoration:none" href="https://www.google.co.in/intl/en/options/"><u>More</u> &raquo;</a></nobr></div><div id=guser width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a href="http://www.google.co.in/history/optout?hl=en" class=gb4>Web History</a> | <a  href="/preferences?hl=en" class=gb4>Settings</a> | <a target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/" class=gb4>Sign in</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div> </div><center><br clear="all" id="lgpd"><div id="lga"><a href="/search?site=&amp;ie=UTF-8&amp;q=World+Cup+2018&amp;oi=ddle&amp;ct=world-cup-2018-day-9-5987135852118016&amp;hl=en&amp;sa=X&amp;ved=0ahUKEwjnvtCG9ebbAhXENY8KHf_zCb0QPQgD"><img alt="World Cup 2018 - Day 9" border="0" height="220" src="/logos/doodles/2018/world-cup-2018-day-9-5987135852118016-5669283816275968-ssw.png" title="World Cup 2018 - Day 9" width="510" id="hplogo" onload="window.lol&&lol()"><br></a><br></div><form action="/search" name="f"><table cellpadding="0" cellspacing="0"><tr valign="top"><td width="25%">&nbsp;</td><td align="center" nowrap=""><input name="ie" value="ISO-8859-1" type="hidden"><input value="en-IN" name="hl" type="hidden"><input name="source" type="hidden" value="hp"><input name="biw" type="hidden"><input name="bih" type="hidden"><div class="ds" style="height:32px;margin:4px 0"><input style="color:#000;margin:0;padding:5px 8px 0 6px;vertical-align:top" autocomplete="off" class="lst" value="" title="Google Search" maxlength="2048" name="q" size="57"></div><br style="line-height:0"><span class="ds"><span class="lsbb"><input class="lsb" value="Google Search" name="btnG" type="submit"></span></span><span class="ds"><span class="lsbb"><input class="lsb" value="I\'m Feeling Lucky" name="btnI" onclick="if(this.form.q.value)this.checked=1; else top.location=\'/doodles/\'" type="submit"></span></span></td><td class="fl sblc" align="left" nowrap="" width="25%"><a href="/advanced_search?hl=en-IN&amp;authuser=0">Advanced search</a><a href="/language_tools?hl=en-IN&amp;authuser=0">Language tools</a></td></tr></table><input id="gbv" name="gbv" type="hidden" value="1"></form><div id="gac_scont"></div><div style="font-size:83%;min-height:3.5em"><br><div id="prm"><style>.szppmdbYutt__middle-slot-promo{font-size:small;margin-bottom:32px}.szppmdbYutt__middle-slot-promo a.ZIeIlb{display:inline-block;text-decoration:none}.szppmdbYutt__middle-slot-promo img{border:none;margin-right:5px;vertical-align:middle}</style><div class="szppmdbYutt__middle-slot-promo" data-ved="0ahUKEwjnvtCG9ebbAhXENY8KHf_zCb0QnIcBCAQ"><img height="42" src="/images/hpp/logo-myaccount-callout-68px.png" width="42"><a class="NKcBbd" href="https://www.google.com/url?q=https://myaccount.google.com/smartlink/home%3Futm_source%3Dgoogle%26utm_medium%3Dhpp-desktop-unauth%26utm_campaign%3Dglobal-google-account-q2&amp;source=hpp&amp;id=19006840&amp;ct=3&amp;usg=AFQjCNG8ZEtLCI-m8PitVgH9Dui9us_raA&amp;sa=X&amp;ved=0ahUKEwjnvtCG9ebbAhXENY8KHf_zCb0Q8IcBCAU" rel="nofollow">Visit your Google account</a><span> to manage your privacy and security, all in one place </span></div></div><div id="gws-output-pages-elements-homepage_additional_languages__als"><style>#gws-output-pages-elements-homepage_additional_languages__als{font-size:small;margin-bottom:24px}#SIvCob{display:inline-block;line-height:28px;}#SIvCob a{padding:0 3px;}.H6sW5{display:inline-block;margin:0 2px;white-space:nowrap}.z4hgWe{display:inline-block;margin:0 2px}</style><div id="SIvCob">Google offered in:  <a href="https://www.google.com/setprefs?sig=0_qPRhsEPbM28vsxuKv519J6dzArM%3D&amp;hl=hi&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjnvtCG9ebbAhXENY8KHf_zCb0Q2ZgBCAc">&#2361;&#2367;&#2344;&#2381;&#2342;&#2368;</a>    <a href="https://www.google.com/setprefs?sig=0_qPRhsEPbM28vsxuKv519J6dzArM%3D&amp;hl=bn&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjnvtCG9ebbAhXENY8KHf_zCb0Q2ZgBCAg">&#2476;&#2494;&#2434;&#2482;&#2494;</a>    <a href="https://www.google.com/setprefs?sig=0_qPRhsEPbM28vsxuKv519J6dzArM%3D&amp;hl=te&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjnvtCG9ebbAhXENY8KHf_zCb0Q2ZgBCAk">&#3108;&#3142;&#3122;&#3137;&#3095;&#3137;</a>    <a href="https://www.google.com/setprefs?sig=0_qPRhsEPbM28vsxuKv519J6dzArM%3D&amp;hl=mr&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjnvtCG9ebbAhXENY8KHf_zCb0Q2ZgBCAo">&#2350;&#2352;&#2366;&#2336;&#2368;</a>    <a href="https://www.google.com/setprefs?sig=0_qPRhsEPbM28vsxuKv519J6dzArM%3D&amp;hl=ta&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjnvtCG9ebbAhXENY8KHf_zCb0Q2ZgBCAs">&#2980;&#2990;&#3007;&#2996;&#3021;</a>    <a href="https://www.google.com/setprefs?sig=0_qPRhsEPbM28vsxuKv519J6dzArM%3D&amp;hl=gu&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjnvtCG9ebbAhXENY8KHf_zCb0Q2ZgBCAw">&#2711;&#2753;&#2716;&#2736;&#2750;&#2724;&#2752;</a>    <a href="https://www.google.com/setprefs?sig=0_qPRhsEPbM28vsxuKv519J6dzArM%3D&amp;hl=kn&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjnvtCG9ebbAhXENY8KHf_zCb0Q2ZgBCA0">&#3221;&#3240;&#3277;&#3240;&#3233;</a>    <a href="https://www.google.com/setprefs?sig=0_qPRhsEPbM28vsxuKv519J6dzArM%3D&amp;hl=ml&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjnvtCG9ebbAhXENY8KHf_zCb0Q2ZgBCA4">&#3374;&#3378;&#3375;&#3390;&#3379;&#3330;</a>    <a href="https://www.google.com/setprefs?sig=0_qPRhsEPbM28vsxuKv519J6dzArM%3D&amp;hl=pa&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjnvtCG9ebbAhXENY8KHf_zCb0Q2ZgBCA8">&#2602;&#2672;&#2588;&#2622;&#2604;&#2624;</a>  </div></div></div><span id="footer"><div style="font-size:10pt"><div style="margin:19px auto;text-align:center" id="fll"><a href="/intl/en/ads/">Advertising\xa0Programs</a><a href="http://www.google.co.in/services/">Business Solutions</a><a href="https://plus.google.com/104205742743787718296" rel="publisher">+Google</a><a href="/intl/en/about.html">About Google</a><a href="https://www.google.com/setprefdomain?prefdom=IN&amp;prev=https://www.google.co.in/&amp;sig=__iRgC3jiRPy_zNHbQa4tCaiq4LNQ%3D">Google.co.in</a></div></div><p style="color:#767676;font-size:8pt">&copy; 2018 - <a href="/intl/en/policies/privacy/">Privacy</a> - <a href="/intl/en/policies/terms/">Terms</a></p></span></center><script nonce="T2t3DABh/+lWLoHSV/hwcQ==">(function(){window.google.cdo={height:0,width:0};(function(){var a=window.innerWidth,b=window.innerHeight;if(!a||!b){var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();</script><div id="xjsd"></div><div id="xjsi"><script nonce="T2t3DABh/+lWLoHSV/hwcQ==">(function(){function c(b){window.setTimeout(function(){var a=document.createElement("script");a.src=b;google.timers&&google.timers.load.t&&google.tick&&google.tick("load",{gen204:"xjsls",clearcut:31});document.getElementById("xjsd").appendChild(a)},0)}google.dljp=function(b,a){google.xjsu=b;c(a)};google.dlj=c;}).call(this);if(!google.xjs){window._=window._||{};window._DumpException=window._._DumpException=function(e){throw e};window._F_installCss=window._._F_installCss=function(c){};google.dljp(\'/xjs/_/js/k\\x3dxjs.hp.en.a2it3LcX-Tc.O/m\\x3dsb_he,d/am\\x3dVGFs/rt\\x3dj/d\\x3d1/rs\\x3dACT90oHwkwNntPAOIhKLsbFldVm4cpRypQ\',\'/xjs/_/js/k\\x3dxjs.hp.en.a2it3LcX-Tc.O/m\\x3dsb_he,d/am\\x3dVGFs/rt\\x3dj/d\\x3d1/rs\\x3dACT90oHwkwNntPAOIhKLsbFldVm4cpRypQ\');google.xjs=1;}google.pmc={"sb_he":{"agen":true,"cgen":true,"client":"heirloom-hp","dh":true,"dhqt":true,"ds":"","ffql":"en","fl":true,"host":"google.com","isbh":28,"jsonp":true,"msgs":{"cibl":"Clear Search","dym":"Did you mean:","lcky":"I\\u0026#39;m Feeling Lucky","lml":"Learn more","oskt":"Input tools","psrc":"This search was removed from your \\u003Ca href=\\"/history\\"\\u003EWeb History\\u003C/a\\u003E","psrl":"Remove","sbit":"Search by image","srch":"Google Search"},"nds":true,"ovr":{},"pq":"","refpd":true,"rfs":[],"sbpl":24,"sbpr":24,"scd":10,"sce":5,"stok":"QT-9nvNip0tlHfEGvzeip8dlHJ0"},"d":{},"ZI/YVQ":{},"Qnk92g":{},"U5B21g":{},"DPBNMg":{},"YFCs/g":{}};google.x(null,function(){});(function(){var r=[];google.plm(r);})();(function(){var m=[]\n;google.jsc && google.jsc.m(m);})();</script></div></body></html>'
>>> 
