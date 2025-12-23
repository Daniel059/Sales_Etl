<div align="left">


# Sales Data ETL Pipeline for Reporting

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen?style=for-the-badge)](https://github.com/Daniel059/Sales_Etl)

</div>

## 📖 Introduction

This project implements a **beginner-friendly Extract, Transform, Load (ETL) pipeline** designed for sales data processing. It serves as a comprehensive guide to processing raw sales information from CSV files, performing essential data transformations using Python and the Pandas library, and preparing cleaned data for reporting or further analytical tasks.

### ✨ Key Features

- 🔄 **Automated Data Processing** - Extract, transform, and load sales data seamlessly
- 📅 **Date Handling** - Proper datetime conversion for temporal analysis
- 💰 **Price Calculations** - Automatic total price computation
- 🔢 **Type Safety** - Ensures correct data types for robust analysis



## Setup
To run this project, you will need Python installed on your system, along with the Pandas library.

1.  **Clone the repository (if applicable) or create your project directory:**
   ### Clone the Repository

```bash
git clone https://github.com/Daniel059/Sales_Etl.git
cd Sales_Etl
```
### Or Creat project directory

```bash
    mkdir sales_etl_project
    cd sales_etl_project
```

2.  **Install Python (if not already installed):**
    Download from [python.org](https://www.python.org/downloads/).

3.  **Install Pandas:**
```bash
    pip install pandas
```

4.  **Prepare your data:**
    Create a `data` directory within your project folder and place your raw sales data CSV file named `dataset.csv` inside it. Ensure the CSV file contains the columns specified in the Data Dictionary section.
```
    sales_etl_project/
    ├── data/
    │   └── dataset.csv
    └── main.py
```

## Usage
1.  **Create your ETL script:**
    Create a Python file named `main.py` in your project's root directory (or use the provided one).

2.  **The ETL script performs:**
    * **Extract**: Loads `dataset.csv` from the `data/` directory.
    * **Transform**: 
        - Converts `order_date` to datetime format for proper date handling
        - Calculates `total_price` by multiplying `quantity` × `price_per_unit`
        - Converts ID fields (`order_id`, `customer_id`, `product_id`) to string type
    * **Load**: Saves the transformed data to `processed_sales_data.csv` in the `processed_data/` directory.

3.  **Run the ETL pipeline:**
    Execute the Python script from your terminal:
```bash
    python main.py
```
    After execution, you will find the `processed_sales_data.csv` file in the `processed_data/` directory.

## Project Structure
```
sales_etl_project/
├── data/
│   └── dataset.csv              # Raw input sales data
├── processed_data/              # Directory for processed output data (created by script)
│   └── processed_sales_data.csv # Cleaned and transformed sales data
└── main.py                      # Python script containing the ETL logic
```

## Data Dictionary

| Column | Type | Description | Constraints |
|--------|------|-------------|-------------|
| order_id | String | A unique identifier for each individual sales order. | Unique, Not Null |
| customer_id | String | An identifier for the customer who placed the order. | Not Null |
| product_id | String | An identifier for the specific product purchased in the order. | Not Null |
| product_name | String | The name or description of the product purchased. | Not Null |
| quantity | Integer | The number of units of the product purchased in this order line item. | Not Null, Greater than 0 |
| price_per_unit | Float | The price of a single unit of the product at the time of purchase. | Not Null, Greater than 0 |
| order_date | Date | The calendar date on which the order was placed. | Not Null, Valid Date Format (e.g., YYYY-MM-DD) |
| region | String | The geographical region associated with the order or customer. | Not Null, Categorical (e.g., 'North', 'South', 'East', 'West') |
| total_price | Float | The calculated total price for the specific product line item (quantity × price_per_unit). This is a derived column from the ETL process. | Not Null, Greater than or equal to 0 |

## Business Requirements

### Primary Objective
To build a basic Extract, Transform, Load (ETL) pipeline for sales data to prepare it for reporting and further analysis by loading raw sales data from a CSV, performing essential data transformations (e.g., calculating total price, converting data types), and ensuring data quality.

### Key Stakeholders
* Sales Analysts
* Business Intelligence Team
* Data Engineers (for pipeline maintenance)
* Marketing Department (for sales performance insights)

### Success Metrics
* **Data Accuracy**: Transformed data accurately reflects raw data and calculated metrics.
* **Data Availability**: Processed sales data is available for reporting within defined timeframes.
* **Data Consistency**: All necessary data types are correctly formatted for downstream systems.
* **Ease of Use**: The ETL script is straightforward to run and understand for basic operations.
* **Completeness**: All required columns are present and appropriately transformed.

### Assumptions & Constraints
* The raw sales data will always be provided in a CSV file format.
* The input CSV file will consistently contain the specified columns (`order_id`, `customer_id`, `product_id`, `product_name`, `quantity`, `price_per_unit`, `order_date`, `region`).
* The `order_date` column will be in a parseable date format (e.g., YYYY-MM-DD).
* The `quantity` and `price_per_unit` columns will contain numeric values suitable for calculations.
* A Python environment with Pandas installed is available for running the ETL script.

## Expected Output
Upon successful execution, the pipeline will:
1. Create a `processed_data/` directory (if it doesn't exist)
2. Generate `processed_sales_data.csv` containing all original columns plus the calculated `total_price` column
3. Display progress messages in the console confirming each stage of the ETL process

## Troubleshooting
* **File not found error**: Ensure `dataset.csv` exists in the `data/` directory
* **Module not found error**: Install pandas using `pip install pandas`
* **Date parsing errors**: Verify that `order_date` column is in a valid date format (YYYY-MM-DD recommended)

## License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Contributing
Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
```bash
   git checkout -b feature/your-feature-name
```
3. **Make your changes and commit them**
```bash
   git commit -m "Add: description of your changes"
```
4. **Push to your branch**
```bash
   git push origin feature/your-feature-name
```
5. **Open a Pull Request**

### Contribution Guidelines
- Ensure your code follows Python best practices (PEP 8)
- Test your changes thoroughly before submitting
- Update documentation if you're adding new features
- Keep commit messages clear and descriptive

### Reporting Issues
If you find a bug or have a suggestion, please open an issue on GitHub with:
- A clear description of the problem or suggestion
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- Your Python and Pandas versions

---

**Author**: Daniel Nzioki Musyoka  
**Contact**: danzioki01@gmail.com
