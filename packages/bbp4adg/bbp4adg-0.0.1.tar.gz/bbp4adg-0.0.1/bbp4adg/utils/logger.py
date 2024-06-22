class Logger:
    def __init__(self, level='INFO'):
        self.log_levels = dict()
        self.log_levels['DEBUG'] = 0
        self.log_levels['INFO'] = 1
        self.log_levels['WARNING'] = 2
        self.log_levels['ERROR'] = 3
        self.log_level = self.log_levels[level]
    def set_log_level(self, level):
        self.log_level = self.log_levels[level]
    def log(self, message, level):
        if self.log_levels[level] >= 1:
            print(message, end='\r', flush=True)
        elif self.log_levels[level] >= self.log_level:
            print(message)