class RealSubject:
    def request(self):
        return "RealSubject: Handling request."

class Proxy:
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        if self.check_access():
            result = self.real_subject.request()
            self.log_access()
            return result

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")

# Usage
real_subject = RealSubject()
proxy = Proxy(real_subject)
print(proxy.request())
