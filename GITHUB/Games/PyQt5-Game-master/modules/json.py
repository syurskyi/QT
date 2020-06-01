# class json wroted by: Omar Othman



class Json:
    def __init__(self):
        self.json = None
        
    def set_json(self, json):
        self.json = json

    def get(self, key):
        if self.json is None:
            print("You need to set json via function set_json(json: dict)")
            return None
        if key in self.json:
            return self.json[key]
        return None
