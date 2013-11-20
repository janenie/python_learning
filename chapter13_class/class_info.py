class AddrBookEntry(object):
  'address book entry class'
  def __init__(self, nm, ph):
    self.name = nm
    self.phone = ph
    print 'Created instance for:', self.name
  def updatePhone(self, newph):
    self.phone = newph
    print 'Updated phone: ', self.name
    
class EmplAddrBookEntry(AddrBookEntry):
  'Employee Address Book Entry class'
  def __init__(self, nm, ph, id, em):
    AddrBookEntry.__init__(self, nm, ph)
    self.empid = id
    self.email = em
    
  def updateEmail(self, newem):
    self.email = newem
    print 'Updated email address for :', self.name


if __name__ == '__main__':
  john = AddrBookEntry('John A', '1112222')
  Json = EmplAddrBookEntry('Json B', '1111113333', 
              '12345', 'json@gmail.com')
  print Json.email
  print Json.name
  print dir(john)
  print EmplAddrBookEntry.__bases__
  
  