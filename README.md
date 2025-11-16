# Property Investment Profiler - Sri Lanka

An AI-powered property investment analysis tool designed specifically for the Sri Lankan real estate market.

## Overview

This web application helps real estate investors, property buyers, and agents analyze property investments in Sri Lanka. It uses intelligent text parsing to extract property details and generates comprehensive investment reports with financial projections, ROI calculations, and market analysis.

## Features

### 🔍 Intelligent Property Analysis
- **Automatic property type detection** (Land, House, Apartment, Commercial)
- **Smart location extraction** covering major Sri Lankan cities and areas
- **Price parsing** with support for multiple formats (per perch, per sq.ft, total price)
- **Size extraction** for both land extent (perches/acres) and built area (sq.ft)
- **Feature detection** (bedrooms, bathrooms, parking, amenities)

### 📊 Investment Calculations
- **Property valuation** with detailed breakdowns
- **ROI projections** (1, 3, 5, and 10-year forecasts)
- **Capital appreciation forecasts** based on property type
- **Rental yield calculations** for income-generating properties
- **Cash flow projections** with maintenance costs

### 🏦 Financial Tools
- **Mortgage calculator** with customizable:
  - Property value
  - Down payment percentage
  - Interest rate
  - Loan period
- **Total interest and payment calculations**

### 💾 Data Management
- **Save analyses** to browser local storage
- **Load saved properties** for review
- **Compare multiple properties** side-by-side
- **Export to PDF** via print functionality

### 🎯 Market Intelligence
- **Target buyer profiles** for each property type
- **Risk assessment** with legal due diligence checklist
- **Investment strategy recommendations**
- **Market liquidity analysis**

## How to Use

1. **Open the application**: Simply open `index.html` in a web browser
2. **Enter property details**: Paste or type property description in the input area
3. **Generate profile**: Click "Generate Profile" to analyze the property
4. **Review analysis**: See comprehensive investment breakdown
5. **Use tools**: Access mortgage calculator and other features
6. **Save results**: Save analyses for future reference

### Example Input Formats

**Land:**
```
21 perches in Colombo 5, asking 19 million per perch
Land for sale in Galle, 45 perches at 5 million per perch
```

**House:**
```
House in Colombo 7, 2500 sq ft built on 15 perch land, asking 120 million
Modern two story house, 4 bedrooms, 2400 sq ft on 8.5 perches, land rate 28.5M per perch, building rate 18500 per sqft
```

**Apartment:**
```
Luxury 3BR apartment in Colombo 3, 1500 sq ft, 45 million
2 bedroom unit at Independence Square, 1200 sq ft at 30000 per sq ft, 9th floor with city views
```

## Technical Details

### Built With
- **HTML5** - Structure and semantics
- **CSS3** - Responsive design with modern gradients and animations
- **Vanilla JavaScript** - No dependencies required
- **LocalStorage API** - Client-side data persistence

### Browser Compatibility
- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera

### Features
- Fully responsive design (mobile, tablet, desktop)
- Print-optimized layout for PDF export
- Accessible UI with clear visual hierarchy
- Toast notifications for user feedback
- Modal dialogs for enhanced UX

## Key Metrics & Calculations

### Appreciation Rates (Annual)
- **Land**: 12%
- **House**: 10%
- **Apartment**: 8%
- **Commercial**: 9%

### Rental Yields (Annual)
- **House**: 7%
- **Apartment**: 8%
- **Commercial**: 10%

### Maintenance Costs
- 15% of monthly rental income

## Location Coverage

The application recognizes 40+ Sri Lankan locations including:
- All Colombo districts (1-15)
- Major cities (Kandy, Galle, Negombo, Jaffna, etc.)
- Tourist destinations (Mirissa, Ella, Unawatuna, etc.)
- Suburban areas (Nugegoda, Rajagiriya, Malabe, etc.)

## Use Cases

1. **Property Investors**: Evaluate potential investments with comprehensive financial analysis
2. **Real Estate Agents**: Generate professional property reports for clients
3. **Home Buyers**: Understand true property value and mortgage implications
4. **Developers**: Assess land banking and development opportunities
5. **Financial Advisors**: Support clients with property investment decisions

## Privacy & Data Security

- All data is stored locally in your browser
- No server-side processing or data transmission
- Your property analyses remain completely private
- Clear local storage anytime to remove all saved data

## Quick Start

```bash
# Clone or download the repository
# Open index.html in your browser
# Start analyzing properties!
```

No installation, no dependencies, no setup required. Just open and use!

---

**Version**: 2.0 Enhanced
**Last Updated**: 2025-11-16
**Target Market**: Sri Lankan Real Estate