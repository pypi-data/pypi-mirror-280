class Repository:
    def __init__(self, name: str, tags: dict):
        self.name = name
        self.tags = tags


class ECRRepository(Repository):
    def __init__(self, name: str, tags: dict, registry_id: str):
        super().__init__(name, tags)
        self.registry_id = registry_id
