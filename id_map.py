class IdMap:
    def __init__(self):
        self.id_to_int = {}
        self.int_to_id = {}

    def get_id(self, key):
        if key not in self.id_to_int:
            idx = len(self.id_to_int)
            self.id_to_int[key] = idx
            self.int_to_id[idx] = key
        return self.id_to_int[key]
