# Property Investment Profiler

A natural language processing system for property investment analysis that correctly identifies, separates, and calculates different property types.

## Features

✅ **Correct Property Type Identification**
- Land stays as LAND
- House stays as HOUSE
- Building stays as BUILDING
- Warehouse stays as WAREHOUSE
- No mixing or confusion between types

✅ **Property Separation**
- Handles multiple properties in one description
- "land with a building" → separated into LAND + BUILDING
- "land with warehouse" → separated into LAND + WAREHOUSE
- Each property is identified and tracked separately

✅ **Individual Calculations**
- Each property type has its own calculation logic
- Land calculated separately from buildings
- Buildings calculated separately from warehouses
- Different appreciation rates, rental yields, and maintenance costs per type

## System Architecture

```
property_identifier.py      - Natural language processing for property type identification
property_calculator.py       - Individual calculation logic for each property type
property_investment_system.py - Main integrated system
```

## Property Types & Calculations

### LAND
- **Appreciation Rate**: 8% annual
- **Rental Yield**: 0% (land typically doesn't generate rental income)
- **Maintenance**: 0.5% annual

### HOUSE
- **Appreciation Rate**: 5% annual
- **Rental Yield**: 3% annual
- **Maintenance**: 2% annual

### BUILDING
- **Appreciation Rate**: 6% annual
- **Rental Yield**: 6% annual
- **Maintenance**: 2.5% annual

### WAREHOUSE
- **Appreciation Rate**: 4% annual
- **Rental Yield**: 8% annual
- **Maintenance**: 3% annual

## Usage Examples

### Example 1: Single Property
```python
from property_investment_system import PropertyInvestmentSystem

system = PropertyInvestmentSystem()

# Analyze a single land property
analysis = system.analyze_from_natural_language(
    description="vacant land",
    values={"land": 150000},
    areas={"land": 5000},
    years=5
)

system.print_analysis_report(analysis)
```

### Example 2: Multiple Properties (Land with Building)
```python
# Analyze land with a building - they will be separated and calculated individually
analysis = system.analyze_from_natural_language(
    description="land with a commercial building",
    values={
        "land": 200000,
        "building": 600000
    },
    areas={
        "land": 8000,
        "building": 6000
    },
    years=5
)

system.print_analysis_report(analysis)
```

### Example 3: Complex Properties (Land with Building and Warehouse)
```python
# Analyze land with multiple structures
analysis = system.analyze_from_natural_language(
    description="land with a building and a warehouse",
    values={
        "land": 300000,
        "building": 700000,
        "warehouse": 450000
    },
    areas={
        "land": 20000,
        "building": 8000,
        "warehouse": 10000
    },
    years=5
)

system.print_analysis_report(analysis)
```

## Running the Examples

```bash
# Test property identification
python property_identifier.py

# Test individual calculations
python property_calculator.py

# Run complete system demonstration
python property_investment_system.py
```

## How It Works

1. **Natural Language Input**: User provides a description like "land with a building"

2. **Property Identification**: System uses regex patterns to identify property types:
   - Checks for warehouse keywords first (most specific)
   - Then house keywords
   - Then building keywords
   - Finally land keywords

3. **Property Separation**: Splits on separators like "with", "and", "including"
   - "land with a building" → ["land", "building"]
   - Each segment is identified separately

4. **Individual Calculation**: Each property is calculated with its own metrics:
   - Land: High appreciation, no rental income
   - House: Moderate appreciation, low rental yield
   - Building: Good appreciation, moderate rental yield
   - Warehouse: Lower appreciation, high rental yield

5. **Aggregated Results**: If multiple properties, shows both individual and combined metrics

## Key Benefits

- **No Confusion**: Land will never be identified as a house, or vice versa
- **Proper Separation**: Multiple properties are always separated and tracked individually
- **Accurate Calculations**: Each property type uses appropriate financial metrics
- **Detailed Reports**: Clear breakdown of each property's performance
- **Flexible Input**: Accepts various natural language descriptions

## Testing

The system includes comprehensive test cases:
- Single property types (land, house, building, warehouse)
- Multiple properties with various separators
- Complex combinations
- Verification that types are correctly identified

Run tests to verify:
```bash
python property_investment_system.py
```

## Future Enhancements

Potential improvements:
- Add more property types (apartment, condo, farm, etc.)
- Support for custom appreciation/rental rates
- Integration with real market data
- Support for multiple languages
- Tax calculations
- Financing options

## Requirements

- Python 3.7+
- No external dependencies (uses standard library only)
