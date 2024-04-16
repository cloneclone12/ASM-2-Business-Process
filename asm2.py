import pandas as pd

# Function to print debug messages
def debug(message):
    if DEBUG:
        print(message)

# Read data from CSV file
def read_data(file_path):
    try:
        df = pd.read_csv(file_path)
        debug("Data read successfully.")
        return df
    except FileNotFoundError:
        debug("File not found.")
        return None
    except Exception as e:
        debug(f"Error reading data: {str(e)}")
        return None

# Check for null data
def check_null_data(df):
    null_data = df[df.isnull().any(axis=1)]
    if not null_data.empty:
        print("There are rows with null values.")
        debug(null_data)
        # Handle null values here if necessary

# Check for empty data
def check_empty_data(df):
    empty_rows = df[df.applymap(lambda x: isinstance(x, str) and x.strip() == '').all(axis=1)]
    if not empty_rows.empty:
        print("There are empty rows.")
        debug(empty_rows)

# Check and remove duplicate data
def check_remove_duplicates(df):
    duplicate_rows = df[df.duplicated()]
    if not duplicate_rows.empty:
        print("There are duplicate rows. Removing duplicate rows...")
        debug(duplicate_rows)
        df = df.drop_duplicates()
    else:
        print("No duplicate rows.")

# Identify and handle missing data
def handle_missing_data(df):
    missing_data = df.isnull().sum()
    print("Missing data in each column:")
    print(missing_data)
    debug(missing_data)

# Convert column 'gender' to the correct format
def convert_gender(df):
    if 'gender' in df.columns:
        valid_genders = ['Male', 'Female', 'Other', 'Unknown']
        df['gender'] = df['gender'].apply(lambda x: x if x in valid_genders else 'Unknown')
        print(df['gender'].value_counts())
    else:
        print("Column 'gender' does not exist in the DataFrame.")

# Check and fix email syntax errors
def check_fix_email_errors(df):
    if 'email' in df.columns:
        df = df[df['email'].str.contains(r"(^[a-zA-Z0-9_.+-]+@gmail\.com$)", na=False)]
        print(df['email'])
    else:
        print("Column 'email' does not exist in the DataFrame.")

# Remove unnecessary attributes
def remove_unnecessary_attributes(df):
    df = df.drop(columns=['id'])
    debug(df)

# Identify and handle outliers
def handle_outliers(df):
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
    for column in numerical_columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        if not outliers.empty:
            print(f"Outliers detected in column '{column}'. Handling outliers...")
            debug(outliers)
            df.loc[(df[column] < lower_bound) | (df[column] > upper_bound), column] = df[column].median()
        else:
            print(f"No outliers detected in column '{column}'.")
    print("Outlier handling completed.")

# Save processed data to a new CSV file
def save_processed_data(df, file_path):
    try:
        df.to_csv(file_path, index=False)
        print("Data processing completed. The data has been saved to the file Asm2_Cleaned_Data.csv.")
        debug(df)
    except Exception as e:
        print(f"Error saving processed data: {str(e)}")

# Main function
def main():
    global DEBUG
    DEBUG = True  # Set DEBUG to True for debug messages
    
    file_path = 'Asm2_Data.csv'
    
    # Read data
    df = read_data(file_path)
    if df is None:
        print("Error reading data. Exiting program.")
        return
    
    # Data cleaning and preprocessing
    check_null_data(df)
    check_empty_data(df)
    check_remove_duplicates(df)
    handle_missing_data(df)
    convert_gender(df)
    check_fix_email_errors(df)
    remove_unnecessary_attributes(df)
    handle_outliers(df)
    
    # Save processed data
    save_processed_data(df, 'Asm2_Cleaned_Data.csv')

if __name__ == "__main__":
    main()