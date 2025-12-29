import pandas as pd

# User will specify the file path for the CSV file here.
# For example: file_path = 'your_file_name.csv'
file_path = '/content/Document.csv' # Keeping the original file path that caused the encoding error

try:
    df = pd.read_csv(file_path, encoding='cp932') # Added encoding='latin1'
    print("CSV file loaded successfully into DataFrame 'df'.")
    print("First 5 rows of the DataFrame:")
    print(df.head())
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please ensure the path is correct.")
except Exception as e:
    print(f"An error occurred while reading the CSV file: {e}")


# 特定の列の抽出
selected_columns = ['notesId', 'Categories', 'Subject', 'modifiedTime']

try:
    df_selected = df[selected_columns]
    print("Specified columns extracted successfully into 'df_selected'.")
    print("First 5 rows of the extracted DataFrame:")
    print(df_selected.head())
except KeyError as e:
    print(f"Error: One or more specified columns not found: {e}. Please check the column names.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# データからHTMLテーブルの生成
df_with_links = df_selected.copy()
df_with_links['notesId'] = df_with_links['notesId'].apply(lambda x: f'<a href="{x}/body.html">{x}</a>')

html_table = df_with_links.to_html(index=False, escape=False)
print("Generated HTML table with links:\n")
print(html_table)

#save the generated HTML table string to an HTML file named output.html.
output_file_path = 'output.html'

try:
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(html_table)
    print(f"HTML table with links successfully saved to '/content/Document.html'.")
except Exception as e:
    print(f"An error occurred while saving the HTML file: {e}")