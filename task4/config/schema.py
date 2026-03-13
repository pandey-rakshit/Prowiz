SCHEMA = {
    "customers": {
        "CustomerKey": "int64",
        "Gender"     : "object",
        "Name"       : "object",
        "City"       : "object",
        "State Code" : "object",
        "State"      : "object",
        "Zip Code"   : "object",
        "Country"    : "object",
        "Continent"  : "object",
        "Birthday"   : "datetime64[ns]",
    },
    "sales": {
        "Order Number" : "int64",
        "Line Item"    : "int64",
        "Order Date"   : "datetime64[ns]",
        "Delivery Date": "datetime64[ns]",
        "CustomerKey"  : "int64",
        "StoreKey"     : "int64",
        "ProductKey"   : "int64",
        "Quantity"     : "int64",
        "Currency Code": "object",
    },
    "products": {
        "ProductKey"    : "int64",
        "Product Name"  : "object",
        "Brand"         : "object",
        "Color"         : "object",
        "Unit Cost USD" : "float64",
        "Unit Price USD": "float64",
        "SubcategoryKey": "int64",
        "Subcategory"   : "object",
        "CategoryKey"   : "int64",
        "Category"      : "object",
    },
    "stores": {
        "StoreKey"     : "int64",
        "Country"      : "object",
        "State"        : "object",
        "Square Meters": "float64",
        "Open Date"    : "datetime64[ns]",
    },
    "exchange_rates": {
        "Date"    : "datetime64[ns]",
        "Currency": "object",
        "Exchange": "float64",
    },
}

DATE_COLS = {
    "customers"     : ["Birthday"],
    "sales"         : ["Order Date", "Delivery Date"],
    "stores"        : ["Open Date"],
    "exchange_rates": ["Date"],
}

FK_PAIRS = [
    ("sales", "CustomerKey", "customers", "CustomerKey", "Sales->Customers"),
    ("sales", "ProductKey",  "products",  "ProductKey",  "Sales->Products"),
    ("sales", "StoreKey",    "stores",    "StoreKey",    "Sales->Stores"),
]

PRICE_COLS= ["Unit Cost USD", "Unit Price USD"]