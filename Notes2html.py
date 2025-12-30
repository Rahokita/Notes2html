import pandas as pd

document_file_path = '/content/Document.csv'

try:
    # 1. document.csv ファイルをcp932エンコーディングを使用してデータフレームとして読み込み、df_documentという変数に格納します。
    df_document = pd.read_csv(document_file_path, encoding='cp932')
    print("document.csv loaded successfully into DataFrame 'df_document'.")

    # 2. df_documentから'formName', 'notesId', 'Categories', 'Subject', 'modifiedTime'の列を抽出し、df_document_processedという新しいデータフレームを作成します。
    columns_to_extract = ['formName', 'notesId', 'Categories', 'Subject', 'modifiedTime']
    df_document_processed = df_document[columns_to_extract].copy()
    print("Specified columns extracted successfully into 'df_document_processed'.")

    # 3. df_document_processedに、'notesId'列の値をコピーして新しい'parentId'列を追加します。
    df_document_processed['parentId'] = df_document_processed['notesId']
    print("'parentId' column created by copying 'notesId'.")

    # 4. 処理されたデータフレームdf_document_processedの最初の5行を表示して、正しく処理されたことを確認します。
    print("First 5 rows of the processed DataFrame 'df_document_processed':")
    print(df_document_processed.head())
except FileNotFoundError:
    print(f"Error: The file '{document_file_path}' was not found. Please ensure the path is correct.")
except KeyError as e:
    print(f"Error: One or more specified columns not found in 'df_document': {e}. Please check the column names.")
except Exception as e:
    print(f"An error occurred while reading or processing the CSV file: {e}")

response_file_path = '/content/Response.csv'

try:
    # 1. response.csv ファイルをcp932エンコーディングを使用してデータフレームとして読み込み、df_response_processedという変数に格納します。
    df_response_processed = pd.read_csv(response_file_path, encoding='cp932')
    print("response.csv loaded successfully into DataFrame 'df_response_processed'.")

    # 2. df_response_processedから'formName','notesId', 'parentId', 'Subject', 'modifiedTime'の列を抽出します。
    columns_to_extract = ['formName','notesId', 'parentId', 'Subject', 'modifiedTime']
    df_response_processed = df_response_processed[columns_to_extract].copy()
    print("Specified columns extracted successfully.")

    # 3. 抽出されたデータフレームに、すべての行で空の文字列''を持つ'Categories'という新しい列を追加します。
    df_response_processed['Categories'] = ''
    print("'Categories' column added with empty strings.")

    # 4. 処理されたデータフレームdf_response_processedの最初の5行を表示して、正しく処理されたことを確認します。
    print("First 5 rows of the processed DataFrame 'df_response_processed':")
    print(df_response_processed.head())

except FileNotFoundError:
    print(f"Error: The file '{response_file_path}' was not found. Please ensure the path is correct.")
except KeyError as e:
    print(f"Error: One or more specified columns not found in 'df_response_processed': {e}. Please check the column names.")
except Exception as e:
    print(f"An error occurred while reading or processing the CSV file: {e}")

# 1. df_document_processedとdf_response_processedの2つのデータフレームを結合し、df_combinedという名前の新しいデータフレームを作成します。
df_combined = pd.concat([df_document_processed, df_response_processed], ignore_index=True)
print("Dataframes combined into 'df_combined'.")


# 2. df_combinedデータフレームを'parentId'列、次に'formName'に基づいて昇順にソートします。
df_combined_sorted = df_combined.sort_values(by=['parentId', 'formName'], ascending=[True, True], ignore_index=True)
print("Combined dataframe sorted by 'parentId' and 'formName'.")


# 3. ソートされたデータフレームの列を、'notesId', 'parentId', 'Categories', 'Subject', 'modifiedTime'の順に並べ替えます。
final_columns = ['notesId', 'parentId', 'Categories', 'Subject', 'modifiedTime']
df_final = df_combined_sorted[final_columns]
print("Columns reordered.")

# 4. 最終的なデータフレームの最初の5行を表示して、正しく統合およびソートされたことを確認します。
print("First 5 rows of the final combined and sorted DataFrame:")
print(df_final.head())


# 5.Generate an HTML table from this final DataFrame, embedding relative links in the 'notesId' column
df_final_with_links = df_final.copy()
df_final_with_links['notesId'] = df_final_with_links['notesId'].apply(lambda x: f'<a href="{x}/body.html">{x}</a>')

html_table_final = df_final_with_links.to_html(index=False, escape=False)
print("Generated HTML table from final merged data with links:\n")
print(html_table_final) # Print the entire HTML table for verification

# 6. Save this HTML table string to a file named 'output.html'
output_file_path = 'output.html'

try:
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(html_table_final)
    print(f"HTML table successfully saved to '{output_file_path}'.")
except Exception as e:
    print(f"An error occurred while saving the HTML file: {e}")