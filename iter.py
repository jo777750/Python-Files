import itertools
from dataclasses import dataclass

@dataclass
class c:
    value:object
    def __iter__(self):
        while True:
            yield self.value

#print(type(__iter()__))
z=list(itertools.islice(c(9),5))
    
print(z)
