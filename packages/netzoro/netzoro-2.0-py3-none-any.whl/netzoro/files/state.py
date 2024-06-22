class State:
    def handle(self, context):
        pass

class ConcreteStateA(State):
    def handle(self, context):
        print("State A handling request and changing state to B")
        context.state = ConcreteStateB()

class ConcreteStateB(State):
    def handle(self, context):
        print("State B handling request and changing state to A")
        context.state = ConcreteStateA()

class Context:
    def __init__(self, state: State):
        self.state = state

    def request(self):
        self.state.handle(self)

# Usage
context = Context(ConcreteStateA())
context.request()  # Output: State A handling request and changing state to B
context.request()  # Output: State B handling request and changing state to A
