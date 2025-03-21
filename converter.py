
class UnitConverter:
    def __init__(self):
        self.conversions = {
            "distance": {
                "kilometers": 1.0,          
                "meters": 1000.0,
                "centimeters": 100000.0,
                "miles": 0.621371,
                "yards": 1093.61,
                "feet": 3280.84
            },
            "length": {
                "meters": 1.0,              
                "centimeters": 100.0,
                "millimeters": 1000.0,
                "inches": 39.3701,
                "feet": 3.28084,
                "yards": 1.09361
            },
            "volume": {
                "liters": 1.0,              
                "milliliters": 1000.0,
                "gallons": 0.264172,
                "quarts": 1.05669,
                "pints": 2.11338,
                "cups": 4.22675,
                "fluid ounces": 33.814,
                "tablespoons": 67.628,
                "teaspoons": 202.884
            },
            "weight": {
                "kilograms": 1.0,           
                "grams": 1000.0,
                "milligrams": 1000000.0,
                "pounds": 2.20462,
                "ounces": 35.274
            },
            "temperature": {
                "celsius": lambda x: x,              
                "fahrenheit": lambda c: (c * 9/5) + 32, # Celsius to Fahrenheit
                "kelvin": lambda c: c + 273.15          # Celsius to Kelvin
            },
            "area": {
                "square meters": 1.0,       
                "square kilometers": 0.000001,
                "square miles": 0.000000386,
                "acres": 0.000247,
                "hectares": 0.0001
            },
            "time": {
                "seconds": 1.0,        
                "minutes": 0.0166667,
                "hours": 0.000277778,
                "days": 0.0000115741,
                "weeks": 0.00000165344
            },
            "energy": {
                "joules": 1.0,             
                "calories": 0.2388459,     
                "kilowatt-hours": 0.00000027778  
            }
        }
        # Reverse functions for temperature
        self.reverse_conversions = {
            "temperature": {
                "celsius": lambda x: x,
                "fahrenheit": lambda f: (f - 32) * 5/9,
                "kelvin": lambda k: k - 273.15
            }
        }

    def convert(self, value, from_unit, to_unit, category):
        # Convert value from one unit to another
        if from_unit not in self.conversions[category] or to_unit not in self.conversions[category]:
            raise ValueError("Invalid unit type")

        # Check if the conversion involves a function
        if callable(self.conversions[category][from_unit]):
            # For function-based conversions (temperature)
            to_base = self.reverse_conversions[category][from_unit](value)  # Convert to base (Celsius)
            result = self.conversions[category][to_unit](to_base)           # Convert from base to target
        else:
            # For factor-based conversions
            base_value = value / self.conversions[category][from_unit]
            result = base_value * self.conversions[category][to_unit]
        return result

    def get_categories(self):
        return list(self.conversions.keys())

    def get_units(self, category):
        return list(self.conversions[category].keys())