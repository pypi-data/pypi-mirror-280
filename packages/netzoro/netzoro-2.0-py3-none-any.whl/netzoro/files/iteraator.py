class Iterator:
    def __next__(self):
        pass

    def __iter__(self):
        return self

class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index < len(self._collection):
            result = self._collection[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

class Aggregate:
    def create_iterator(self):
        pass

class ConcreteAggregate(Aggregate):
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def create_iterator(self):
        return ConcreteIterator(self._items)

# Usage
aggregate = ConcreteAggregate()
aggregate.add_item("Item 1")
aggregate.add_item("Item 2")
aggregate.add_item("Item 3")

iterator = aggregate.create_iterator()

for item in iterator:
    print(item)
