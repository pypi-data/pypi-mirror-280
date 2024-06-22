class Strategy:
    def execute(self, data):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return f"Strategy A executed with {data}"

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return f"Strategy B executed with {data}"

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.execute(data)

# Usage
context = Context(ConcreteStrategyA())
print(context.execute_strategy("data"))  # Output: Strategy A executed with data

context.set_strategy(ConcreteStrategyB())
print(context.execute_strategy("data"))  # Output: Strategy B executed with data
