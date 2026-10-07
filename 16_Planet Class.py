class Planet:
    def __init__(self, name, planet_type, star):
        if not all(isinstance(arg, str) for arg in (name, planet_type, star)):
            raise TypeError('name, planet type, and star must be strings')
            return
        elif any(arg == "" for arg in (name, planet_type, star)):
            raise ValueError('name, planet_type, and star must be non-empty strings')
            return

        self.name = name
        self.planet_type = planet_type
        self.star = star
        
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'
    
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'
    
planet_1 = Planet('Earth', 'Normal', 'Sun')
planet_2 = Planet('Venus', 'Normal', 'Sun')
planet_3 = Planet('Jupiter', 'Normal', 'Sun')
print(planet_1)
print(planet_2)
print(planet_3)
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())