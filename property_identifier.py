"""
Property Type Identifier - Natural Language Processing for Property Types
Correctly identifies and separates: land, house, building, warehouse
"""

import re
from typing import List, Dict, Tuple
from dataclasses import dataclass
from enum import Enum


class PropertyType(Enum):
    """Enum for different property types"""
    LAND = "land"
    HOUSE = "house"
    BUILDING = "building"
    WAREHOUSE = "warehouse"
    UNKNOWN = "unknown"


@dataclass
class Property:
    """Represents a single property with its type and details"""
    property_type: PropertyType
    description: str
    area: float = 0.0
    value: float = 0.0

    def __str__(self):
        return f"{self.property_type.value.upper()}: {self.description} (Area: {self.area}, Value: {self.value})"


class PropertyIdentifier:
    """Identifies property types from natural language descriptions"""

    def __init__(self):
        # Define keywords for each property type - order matters!
        # More specific terms first to avoid misclassification
        self.property_keywords = {
            PropertyType.WAREHOUSE: [
                r'\bwarehouse\b',
                r'\bwarehouses\b',
                r'\bstorage\s+facility\b',
                r'\bstorage\s+building\b',
                r'\bgodown\b',
                r'\bdepot\b',
            ],
            PropertyType.HOUSE: [
                r'\bhouse\b',
                r'\bhome\b',
                r'\bresidence\b',
                r'\bresidential\s+property\b',
                r'\bvilla\b',
                r'\bbungalow\b',
                r'\bapartment\b',
                r'\bflat\b',
                r'\bcondo\b',
                r'\bcondominium\b',
            ],
            PropertyType.BUILDING: [
                r'\bbuilding\b',
                r'\bbuildings\b',
                r'\bcommercial\s+building\b',
                r'\boffice\s+building\b',
                r'\bstructure\b',
                r'\bedifice\b',
                r'\bpremises\b',
            ],
            PropertyType.LAND: [
                r'\bland\b',
                r'\bplot\b',
                r'\bparcel\b',
                r'\bacreage\b',
                r'\bacres\b',
                r'\blot\b',
                r'\bsite\b',
                r'\bground\b',
                r'\bvacant\s+land\b',
                r'\bempty\s+land\b',
            ],
        }

        # Separators that indicate multiple properties
        self.separators = [
            r'\bwith\s+a\b',
            r'\bwith\b',
            r'\band\s+a\b',
            r'\band\b',
            r'\bplus\b',
            r'\balong\s+with\b',
            r'\bincluding\b',
            r'\bhas\b',
            r'\bhaving\b',
            r'\bcontaining\b',
            r',',
        ]

    def identify_property_type(self, text: str) -> PropertyType:
        """
        Identify a single property type from text
        Returns the most specific match found
        """
        text_lower = text.lower().strip()

        # Check each property type in order (most specific first)
        for prop_type, keywords in self.property_keywords.items():
            for pattern in keywords:
                if re.search(pattern, text_lower):
                    return prop_type

        return PropertyType.UNKNOWN

    def extract_properties_from_text(self, text: str) -> List[Dict[str, str]]:
        """
        Extract multiple properties from a single text description
        Handles cases like "land with a building" or "house and warehouse"
        """
        text_lower = text.lower().strip()

        # Create a pattern that splits on separators
        separator_pattern = '|'.join(self.separators)

        # Split the text into segments
        segments = re.split(separator_pattern, text_lower)

        # Clean up segments
        segments = [seg.strip() for seg in segments if seg.strip()]

        properties = []
        for segment in segments:
            prop_type = self.identify_property_type(segment)
            if prop_type != PropertyType.UNKNOWN:
                properties.append({
                    'type': prop_type,
                    'description': segment
                })

        # If no properties found, treat the whole text as one property
        if not properties:
            prop_type = self.identify_property_type(text)
            properties.append({
                'type': prop_type,
                'description': text_lower
            })

        return properties

    def separate_and_identify(self, description: str) -> List[Property]:
        """
        Main method: separates multiple properties and identifies each type
        Returns a list of Property objects
        """
        extracted = self.extract_properties_from_text(description)

        properties = []
        for item in extracted:
            prop = Property(
                property_type=item['type'],
                description=item['description']
            )
            properties.append(prop)

        return properties

    def validate_identification(self, description: str) -> Dict[str, any]:
        """
        Validates that properties are correctly identified
        Returns a report with original text and identified properties
        """
        properties = self.separate_and_identify(description)

        return {
            'original_text': description,
            'num_properties_found': len(properties),
            'properties': [
                {
                    'type': prop.property_type.value,
                    'description': prop.description
                }
                for prop in properties
            ]
        }


def test_property_identifier():
    """Test the property identifier with various examples"""
    identifier = PropertyIdentifier()

    test_cases = [
        "land",
        "house",
        "building",
        "warehouse",
        "land with a building",
        "land with a house",
        "land with a warehouse",
        "building and land",
        "house and warehouse",
        "land with a building and a warehouse",
        "commercial building",
        "vacant land",
        "residential house",
        "storage warehouse",
        "land plot with a commercial building",
        "house with land",
        "warehouse on land",
    ]

    print("="*80)
    print("PROPERTY TYPE IDENTIFICATION TEST")
    print("="*80)

    for test in test_cases:
        print(f"\nInput: '{test}'")
        result = identifier.validate_identification(test)
        print(f"Properties found: {result['num_properties_found']}")
        for i, prop in enumerate(result['properties'], 1):
            print(f"  {i}. Type: {prop['type'].upper()}, Description: '{prop['description']}'")

    print("\n" + "="*80)


if __name__ == "__main__":
    test_property_identifier()
