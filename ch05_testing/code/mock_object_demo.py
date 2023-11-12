from unittest import mock

dummy = mock.Mock()

print(dummy.hello())
# <Mock name='mock.hello()' id='140433175985104'>

print(dummy.test)
# <Mock name='mock.test' id='139787934776400'>

dummy.name = 'Fred'
print(dummy.name)
# Fred

dummy.process.monthly.report = 5
print(dummy.process.monthly.report)
#  5
