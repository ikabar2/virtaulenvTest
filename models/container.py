class Shaker:
    def __init__(self,contents, name):
        self.contents=contents
        self.name=name
        pass
    def __repr__(self) -> str:
        return f"shaker {self.name}: content---{self.contents}"