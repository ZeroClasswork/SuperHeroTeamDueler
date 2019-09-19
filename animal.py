class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration

    def sleep(self):
        print(
            "{} sleeps for {} hours".format(
                self.name,
                self.sleep_duration))
    
    def eat(self):
        print('{} is eating'.format(self.name))

    def drink(self):
        print('{} is drinking'.format(self.name))

        