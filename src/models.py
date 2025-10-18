# Example fix - actual content depends on the failure log
class Model:
    def __init__(self, name):
        self.name = name
    
    def process(self, data):
        if data is None:
            raise ValueError("Data cannot be None")
        return data
