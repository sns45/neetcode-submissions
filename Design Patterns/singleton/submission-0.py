class Singleton:
    _uniq_instance = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls._uniq_instance is None:
            cls._uniq_instance = super(Singleton, cls).__new__(cls)
        return cls._uniq_instance

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value
