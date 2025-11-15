"""
Property Calculator - Individual calculations for each property type
Ensures land, house, building, and warehouse are calculated separately
"""

from typing import Dict, List
from property_identifier import Property, PropertyType


class PropertyCalculator:
    """Calculates investment metrics for different property types separately"""

    def __init__(self):
        # Default rates for different property types (can be customized)
        self.appreciation_rates = {
            PropertyType.LAND: 0.08,      # 8% annual appreciation
            PropertyType.HOUSE: 0.05,     # 5% annual appreciation
            PropertyType.BUILDING: 0.06,  # 6% annual appreciation
            PropertyType.WAREHOUSE: 0.04, # 4% annual appreciation
        }

        self.rental_yield_rates = {
            PropertyType.LAND: 0.0,       # Land typically doesn't generate rental income
            PropertyType.HOUSE: 0.03,     # 3% rental yield
            PropertyType.BUILDING: 0.06,  # 6% rental yield
            PropertyType.WAREHOUSE: 0.08, # 8% rental yield
        }

        self.maintenance_rates = {
            PropertyType.LAND: 0.005,     # 0.5% maintenance
            PropertyType.HOUSE: 0.02,     # 2% maintenance
            PropertyType.BUILDING: 0.025, # 2.5% maintenance
            PropertyType.WAREHOUSE: 0.03, # 3% maintenance
        }

    def calculate_land(self, property: Property, years: int = 5) -> Dict:
        """Calculate investment metrics specifically for LAND"""
        if property.property_type != PropertyType.LAND:
            raise ValueError(f"Expected LAND, got {property.property_type.value}")

        initial_value = property.value
        appreciation_rate = self.appreciation_rates[PropertyType.LAND]
        maintenance_rate = self.maintenance_rates[PropertyType.LAND]

        future_value = initial_value * ((1 + appreciation_rate) ** years)
        total_maintenance = initial_value * maintenance_rate * years
        rental_income = 0  # Land typically doesn't generate rental income
        net_profit = future_value - initial_value - total_maintenance

        return {
            'property_type': 'LAND',
            'initial_value': initial_value,
            'future_value': future_value,
            'appreciation_rate': appreciation_rate,
            'total_appreciation': future_value - initial_value,
            'rental_income': rental_income,
            'maintenance_cost': total_maintenance,
            'net_profit': net_profit,
            'roi_percentage': (net_profit / initial_value * 100) if initial_value > 0 else 0,
            'years': years
        }

    def calculate_house(self, property: Property, years: int = 5) -> Dict:
        """Calculate investment metrics specifically for HOUSE"""
        if property.property_type != PropertyType.HOUSE:
            raise ValueError(f"Expected HOUSE, got {property.property_type.value}")

        initial_value = property.value
        appreciation_rate = self.appreciation_rates[PropertyType.HOUSE]
        rental_yield = self.rental_yield_rates[PropertyType.HOUSE]
        maintenance_rate = self.maintenance_rates[PropertyType.HOUSE]

        future_value = initial_value * ((1 + appreciation_rate) ** years)
        rental_income = initial_value * rental_yield * years
        total_maintenance = initial_value * maintenance_rate * years
        net_profit = future_value - initial_value + rental_income - total_maintenance

        return {
            'property_type': 'HOUSE',
            'initial_value': initial_value,
            'future_value': future_value,
            'appreciation_rate': appreciation_rate,
            'total_appreciation': future_value - initial_value,
            'rental_yield_rate': rental_yield,
            'rental_income': rental_income,
            'maintenance_cost': total_maintenance,
            'net_profit': net_profit,
            'roi_percentage': (net_profit / initial_value * 100) if initial_value > 0 else 0,
            'years': years
        }

    def calculate_building(self, property: Property, years: int = 5) -> Dict:
        """Calculate investment metrics specifically for BUILDING"""
        if property.property_type != PropertyType.BUILDING:
            raise ValueError(f"Expected BUILDING, got {property.property_type.value}")

        initial_value = property.value
        appreciation_rate = self.appreciation_rates[PropertyType.BUILDING]
        rental_yield = self.rental_yield_rates[PropertyType.BUILDING]
        maintenance_rate = self.maintenance_rates[PropertyType.BUILDING]

        future_value = initial_value * ((1 + appreciation_rate) ** years)
        rental_income = initial_value * rental_yield * years
        total_maintenance = initial_value * maintenance_rate * years
        net_profit = future_value - initial_value + rental_income - total_maintenance

        return {
            'property_type': 'BUILDING',
            'initial_value': initial_value,
            'future_value': future_value,
            'appreciation_rate': appreciation_rate,
            'total_appreciation': future_value - initial_value,
            'rental_yield_rate': rental_yield,
            'rental_income': rental_income,
            'maintenance_cost': total_maintenance,
            'net_profit': net_profit,
            'roi_percentage': (net_profit / initial_value * 100) if initial_value > 0 else 0,
            'years': years
        }

    def calculate_warehouse(self, property: Property, years: int = 5) -> Dict:
        """Calculate investment metrics specifically for WAREHOUSE"""
        if property.property_type != PropertyType.WAREHOUSE:
            raise ValueError(f"Expected WAREHOUSE, got {property.property_type.value}")

        initial_value = property.value
        appreciation_rate = self.appreciation_rates[PropertyType.WAREHOUSE]
        rental_yield = self.rental_yield_rates[PropertyType.WAREHOUSE]
        maintenance_rate = self.maintenance_rates[PropertyType.WAREHOUSE]

        future_value = initial_value * ((1 + appreciation_rate) ** years)
        rental_income = initial_value * rental_yield * years
        total_maintenance = initial_value * maintenance_rate * years
        net_profit = future_value - initial_value + rental_income - total_maintenance

        return {
            'property_type': 'WAREHOUSE',
            'initial_value': initial_value,
            'future_value': future_value,
            'appreciation_rate': appreciation_rate,
            'total_appreciation': future_value - initial_value,
            'rental_yield_rate': rental_yield,
            'rental_income': rental_income,
            'maintenance_cost': total_maintenance,
            'net_profit': net_profit,
            'roi_percentage': (net_profit / initial_value * 100) if initial_value > 0 else 0,
            'years': years
        }

    def calculate_property(self, property: Property, years: int = 5) -> Dict:
        """
        Calculate metrics for any property type
        Routes to the appropriate calculation method based on property type
        """
        calculators = {
            PropertyType.LAND: self.calculate_land,
            PropertyType.HOUSE: self.calculate_house,
            PropertyType.BUILDING: self.calculate_building,
            PropertyType.WAREHOUSE: self.calculate_warehouse,
        }

        calculator = calculators.get(property.property_type)
        if calculator is None:
            raise ValueError(f"Unknown property type: {property.property_type}")

        return calculator(property, years)

    def calculate_multiple_properties(self, properties: List[Property], years: int = 5) -> Dict:
        """
        Calculate metrics for multiple properties SEPARATELY
        Each property is calculated individually and then aggregated
        """
        individual_calculations = []
        total_investment = 0
        total_future_value = 0
        total_rental_income = 0
        total_maintenance = 0
        total_net_profit = 0

        for prop in properties:
            calc = self.calculate_property(prop, years)
            individual_calculations.append({
                'property_description': prop.description,
                'calculation': calc
            })

            total_investment += calc['initial_value']
            total_future_value += calc['future_value']
            total_rental_income += calc['rental_income']
            total_maintenance += calc['maintenance_cost']
            total_net_profit += calc['net_profit']

        return {
            'num_properties': len(properties),
            'individual_calculations': individual_calculations,
            'aggregate': {
                'total_initial_investment': total_investment,
                'total_future_value': total_future_value,
                'total_rental_income': total_rental_income,
                'total_maintenance_cost': total_maintenance,
                'total_net_profit': total_net_profit,
                'overall_roi_percentage': (total_net_profit / total_investment * 100) if total_investment > 0 else 0,
                'years': years
            }
        }


def format_currency(amount: float) -> str:
    """Format currency for display"""
    return f"${amount:,.2f}"


def print_calculation_report(calc: Dict):
    """Print a formatted calculation report"""
    print(f"\n{'='*80}")
    print(f"PROPERTY TYPE: {calc['property_type']}")
    print(f"{'='*80}")
    print(f"Initial Value:        {format_currency(calc['initial_value'])}")
    print(f"Future Value ({calc['years']}y):   {format_currency(calc['future_value'])}")
    print(f"Appreciation:         {format_currency(calc['total_appreciation'])} ({calc['appreciation_rate']*100}% annual)")
    if 'rental_income' in calc and calc['rental_income'] > 0:
        print(f"Rental Income:        {format_currency(calc['rental_income'])}")
    print(f"Maintenance Cost:     {format_currency(calc['maintenance_cost'])}")
    print(f"Net Profit:           {format_currency(calc['net_profit'])}")
    print(f"ROI:                  {calc['roi_percentage']:.2f}%")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    # Example usage
    calculator = PropertyCalculator()

    # Test individual property calculations
    land = Property(PropertyType.LAND, "vacant land plot", area=1000, value=100000)
    house = Property(PropertyType.HOUSE, "residential house", area=2000, value=300000)
    building = Property(PropertyType.BUILDING, "commercial building", area=5000, value=500000)
    warehouse = Property(PropertyType.WAREHOUSE, "storage warehouse", area=10000, value=400000)

    print("\nINDIVIDUAL PROPERTY CALCULATIONS")
    print("Each property type is calculated with its own specific metrics\n")

    for prop in [land, house, building, warehouse]:
        calc = calculator.calculate_property(prop, years=5)
        print_calculation_report(calc)
