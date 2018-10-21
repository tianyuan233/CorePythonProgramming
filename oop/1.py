class AddrBookEntry():
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print('created instance for {}'.format(self.name))

    def updatePhone(self, newph):
        self.phone = newph
        print('update phone for {}'.format(self.name))


# zty = AddrBookEntry('zty','123123123123')

# print(zty)
# print(zty.name)
# print(zty.phone)
# zty.updatePhone('789789978')
# print(zty.phone)

# 创建子类


class EmplAddrBookEntry(AddrBookEntry):
    def __init__(self, nm, ph, eid, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = eid
        self.email = em

    def updateEmail(self, newem):
        self.email = newem
    def __repr__(self):
        return self.empid


qwe = EmplAddrBookEntry('qwe', '213', '1', '111@qq.com')

print(qwe)
print(qwe.empid)
print(qwe.email)
