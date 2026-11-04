# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def status(self, percent):    # this parameter should be self
        return percent
#you did'nt add self as the first parameter of the status method.
r = Record()
print(r.status(95))
