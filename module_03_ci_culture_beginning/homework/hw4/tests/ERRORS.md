  File "/home/kirill/Studies/python_advanced/module_03_ci_culture_beginning/homework/hw4/person.py", line 11, in get_age
    now: datetime.datetime = datetime.datetime.now()
                             ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'
  
import datetime



File "/home/kirill/Studies/python_advanced/module_03_ci_culture_beginning/homework/hw4/person.py", line 30, in is_homeless
    return address is None
           ^^^^^^^
NameError: name 'address' is not defined. Did you mean: 'self.address'?

return self.address is None




File "/home/kirill/Studies/python_advanced/module_03_ci_culture_beginning/homework/hw4/tests/test_person.py", line 72, in test_set_adress
    self.assertEqual(self.person.address, "Krilenko")
AssertionError: 'Lenina' != 'Krilenko'
- Lenina
+ Krilenko

 def set_name(self, name: str) -> None:
        self.name = name





File "/home/kirill/Studies/python_advanced/module_03_ci_culture_beginning/homework/hw4/tests/test_person.py", line 68, in test_set_name
    self.assertEqual(self.person.name, "Boba")
AssertionError: 'Bob' != 'Boba'
- Bob
+ Boba
?    +
+ 
 def set_name(self, name: str) -> None:
        self.name = name





File "/home/kirill/Studies/python_advanced/module_03_ci_culture_beginning/homework/hw4/tests/test_person.py", line 81, in test_get_age
    self.assertEqual(self.person.get_age(), datetime.now().year - 2020)
AssertionError: -4 != 4

return now.year - self.yob