class AbstractClass:
    def template_method(self):
        self.base_operation_1()
        self.required_operations_1()
        self.base_operation_2()
        self.required_operations_2()
        self.hook()

    def base_operation_1(self):
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation_2(self):
        print("AbstractClass says: But I let subclasses override some operations")

    def required_operations_1(self):
        pass

    def required_operations_2(self):
        pass

    def hook(self):
        pass

class ConcreteClass1(AbstractClass):
    def required_operations_1(self):
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations_2(self):
        print("ConcreteClass1 says: Implemented Operation2")

class ConcreteClass2(AbstractClass):
    def required_operations_1(self):
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations_2(self):
        print("ConcreteClass2 says: Implemented Operation2")

    def hook(self):
        print("ConcreteClass2 says: Overridden Hook")

# Usage
concrete_class1 = ConcreteClass1()
concrete_class1.template_method()
# Output:
# AbstractClass says: I am doing the bulk of the work
# ConcreteClass1 says: Implemented Operation1
# AbstractClass says: But I let subclasses override some operations
# ConcreteClass1 says: Implemented Operation2

concrete_class2 = ConcreteClass2()
concrete_class2.template_method()
# Output:
# AbstractClass says: I am doing the bulk of the work
# ConcreteClass2 says: Implemented Operation1
# AbstractClass says: But I let subclasses override some operations
# ConcreteClass2 says: Implemented Operation2
# ConcreteClass2 says: Overridden Hook
