from exceptions.Exceptions import MaxSizeReached, QueueEmpty

class PyQueue():
    def __init__(self, max_len: int = 0):
        self.max = max_len
        self.queue = []
        self.noelem = False
        self.returntype = tuple

    def add(self, *elements):
        for element in elements:
            if len(self.queue) < self.max or self.max == 0:
                self.queue.append(element)

            elif len(self.queue) >= self.max:
                raise MaxSizeReached()
        
    def get(self, amount: int = 1):
        if not self.queue:
            raise QueueEmpty()
        
        if amount == -1:
            temp = self.returntype(self.queue)
            self.queue = []
            return temp

        ls= []
        for _ in range(amount):
            if self.queue:
                ls.append(self.queue.pop(0))
            else:
                if self.noelem is not False:
                    ls.append(self.noelem)
                break
        return self.returntype(ls)

    def wipe(self):
        self.queue = []


if __name__ == "__main__":
    pass