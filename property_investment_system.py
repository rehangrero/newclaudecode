"""
Property Investment Profiler System
Complete end-to-end system for natural language property investment analysis

This system:
1. Takes natural language input (e.g., "land with a building")
2. Correctly identifies property types (land, house, building, warehouse)
3. Separates multiple properties
4. Calculates each property type individually
5. Provides detailed investment analysis
"""

from typing import Dict, List
from property_identifier import PropertyIdentifier, Property, PropertyType
from property_calculator import PropertyCalculator, format_currency


class PropertyInvestmentSystem:
    """
    Main system that integrates property identification and calculation
    """

    def __init__(self):
        self.identifier = PropertyIdentifier()
        self.calculator = PropertyCalculator()

    def analyze_from_natural_language(
        self,
        description: str,
        values: Dict[str, float] = None,
        areas: Dict[str, float] = None,
        years: int = 5
    ) -> Dict:
        """
        Complete analysis from natural language description

        Args:
            description: Natural language description (e.g., "land with a building")
            values: Dictionary mapping property types to their values
            areas: Dictionary mapping property types to their areas
            years: Investment period in years

        Returns:
            Complete analysis with identification and calculations
        """
        # Step 1: Identify and separate properties
        properties = self.identifier.separate_and_identify(description)

        # Step 2: Add values and areas to properties
        if values:
            for prop in properties:
                prop_type_key = prop.property_type.value
                if prop_type_key in values:
                    prop.value = values[prop_type_key]

        if areas:
            for prop in properties:
                prop_type_key = prop.property_type.value
                if prop_type_key in areas:
                    prop.area = areas[prop_type_key]

        # Step 3: Calculate each property separately
        results = self.calculator.calculate_multiple_properties(properties, years)

        # Step 4: Add identification info
        results['original_description'] = description
        results['identified_properties'] = [
            {
                'type': prop.property_type.value,
                'description': prop.description,
                'area': prop.area,
                'value': prop.value
            }
            for prop in properties
        ]

        return results

    def print_analysis_report(self, analysis: Dict):
        """Print a detailed analysis report"""
        print("\n" + "="*80)
        print("PROPERTY INVESTMENT ANALYSIS REPORT")
        print("="*80)
        print(f"\nOriginal Input: '{analysis['original_description']}'")
        print(f"\nProperties Identified: {analysis['num_properties']}")

        # Show identified properties
        print("\n--- PROPERTY IDENTIFICATION ---")
        for i, prop in enumerate(analysis['identified_properties'], 1):
            print(f"\n{i}. Property Type: {prop['type'].upper()}")
            print(f"   Description: {prop['description']}")
            print(f"   Area: {prop['area']} sq ft")
            print(f"   Value: {format_currency(prop['value'])}")

        # Show individual calculations
        print("\n" + "="*80)
        print("INDIVIDUAL PROPERTY CALCULATIONS")
        print("="*80)

        for i, calc in enumerate(analysis['individual_calculations'], 1):
            prop_calc = calc['calculation']
            print(f"\n{i}. {prop_calc['property_type']}: '{calc['property_description']}'")
            print(f"   {'-'*70}")
            print(f"   Initial Value:        {format_currency(prop_calc['initial_value'])}")
            print(f"   Future Value ({prop_calc['years']}y):   {format_currency(prop_calc['future_value'])}")
            print(f"   Appreciation:         {format_currency(prop_calc['total_appreciation'])} ({prop_calc['appreciation_rate']*100}% annual)")
            if prop_calc['rental_income'] > 0:
                print(f"   Rental Income:        {format_currency(prop_calc['rental_income'])}")
            print(f"   Maintenance Cost:     {format_currency(prop_calc['maintenance_cost'])}")
            print(f"   Net Profit:           {format_currency(prop_calc['net_profit'])}")
            print(f"   ROI:                  {prop_calc['roi_percentage']:.2f}%")

        # Show aggregate if multiple properties
        if analysis['num_properties'] > 1:
            agg = analysis['aggregate']
            print("\n" + "="*80)
            print("AGGREGATE ANALYSIS (ALL PROPERTIES COMBINED)")
            print("="*80)
            print(f"Total Initial Investment:  {format_currency(agg['total_initial_investment'])}")
            print(f"Total Future Value:        {format_currency(agg['total_future_value'])}")
            print(f"Total Rental Income:       {format_currency(agg['total_rental_income'])}")
            print(f"Total Maintenance:         {format_currency(agg['total_maintenance_cost'])}")
            print(f"Total Net Profit:          {format_currency(agg['total_net_profit'])}")
            print(f"Overall ROI:               {agg['overall_roi_percentage']:.2f}%")

        print("\n" + "="*80 + "\n")


def run_examples():
    """Run example scenarios demonstrating the system"""
    system = PropertyInvestmentSystem()

    print("\n" + "#"*80)
    print("# PROPERTY INVESTMENT PROFILER - DEMONSTRATION")
    print("#"*80)

    # Example 1: Single land
    print("\n\nEXAMPLE 1: Single property - Land")
    print("-"*80)
    analysis1 = system.analyze_from_natural_language(
        description="vacant land",
        values={"land": 150000},
        areas={"land": 5000},
        years=5
    )
    system.print_analysis_report(analysis1)

    # Example 2: Single house
    print("\n\nEXAMPLE 2: Single property - House")
    print("-"*80)
    analysis2 = system.analyze_from_natural_language(
        description="residential house",
        values={"house": 400000},
        areas={"house": 2500},
        years=5
    )
    system.print_analysis_report(analysis2)

    # Example 3: Land with a building (multiple properties)
    print("\n\nEXAMPLE 3: Multiple properties - Land with a building")
    print("-"*80)
    analysis3 = system.analyze_from_natural_language(
        description="land with a building",
        values={"land": 200000, "building": 600000},
        areas={"land": 8000, "building": 6000},
        years=5
    )
    system.print_analysis_report(analysis3)

    # Example 4: Land with warehouse
    print("\n\nEXAMPLE 4: Multiple properties - Land with a warehouse")
    print("-"*80)
    analysis4 = system.analyze_from_natural_language(
        description="land with a warehouse",
        values={"land": 250000, "warehouse": 500000},
        areas={"land": 15000, "warehouse": 12000},
        years=5
    )
    system.print_analysis_report(analysis4)

    # Example 5: Complex - Building and land and warehouse
    print("\n\nEXAMPLE 5: Multiple properties - Land with building and warehouse")
    print("-"*80)
    analysis5 = system.analyze_from_natural_language(
        description="land with a commercial building and a warehouse",
        values={"land": 300000, "building": 700000, "warehouse": 450000},
        areas={"land": 20000, "building": 8000, "warehouse": 10000},
        years=5
    )
    system.print_analysis_report(analysis5)

    # Example 6: Verify correct identification (land doesn't become house)
    print("\n\nEXAMPLE 6: Verification - Ensuring land stays land, house stays house")
    print("-"*80)
    test_cases = [
        "land",
        "house",
        "building",
        "warehouse",
        "land with house",
        "house with land",
    ]

    identifier = PropertyIdentifier()
    for test in test_cases:
        result = identifier.validate_identification(test)
        print(f"\nInput: '{test}'")
        for i, prop in enumerate(result['properties'], 1):
            print(f"  Property {i}: {prop['type'].upper()} ('{prop['description']}')")


if __name__ == "__main__":
    run_examples()
