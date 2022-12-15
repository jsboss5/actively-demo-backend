class Fake_Database:
    models: dict
    count: int

    def __init__(self):
        self.models = {}
        self.count = 0


    def store_model(self, model):
        self.models[self.count] = model
        self.count += 1
        return self.count -1

    def get_model(self, model_id):
        return self.models[model_id]

