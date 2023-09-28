def generate_rst_table(headers, data):
    column_widths = [max(len(str(item)) for item in col) for col in zip(headers, *data)]
    separator = '+' + '+'.join(['-' * (width + 2) for width in column_widths]) + '+'

    lines = [separator]
    header_line = '| ' + ' | '.join([str(header).ljust(width) for header, width in zip(headers, column_widths)]) + ' |'
    lines.append(header_line)
    lines.append(separator)

    for row in data:
        row_line = '| ' + ' | '.join([str(item).ljust(width) for item, width in zip(row, column_widths)]) + ' |'
        lines.append(row_line)
        lines.append(separator)

    return '\n'.join(lines)

headers = ['Parameter', 'Description']
data = [
    ['openai_api_key', 'Your OpenAI API key, you can get it from :ref:`here <openai>`'], 
    ['pinecone_api_key', 'Your Pinecone API key,you can get it from :ref:`here <pinecone>`'], 
    ['pinecone_environment', 'Details about your Pinecone environment'], 
    ['pinecone_index', 'Information about your Pinecone index'], 
    ['xata_api_key', 'Your Xata API key'], 
    ['xata_db_url', 'The URL for your Xata database'], 
    ['langchain_verbose', 'Indicates if Langchain should be verbose (true/false)'], 
    ['llm_model', 'The name of your LLM model'], 
    ['password', 'Your password. If needed, set "need_passwd" to *True* in `tiangong-en.py` at line 2.'],
]

print(generate_rst_table(headers, data))

# rst_table = """
# +-----------------------+-----------------------------------------------------------------+
# | Parameter             | Description                                                     |
# +-----------------------+-----------------------------------------------------------------+
# | openai_api_key        | Your OpenAI API key, you can get it from :ref:`here <openai>`   |
# +-----------------------+-----------------------------------------------------------------+
# | pinecone_api_key      | Your Pinecone API key,you can get it from :ref:`here <pinecone>`|
# +-----------------------+-----------------------------------------------------------------+
# | pinecone_environment  | Details about your Pinecone environment                         |
# +-----------------------+-----------------------------------------------------------------+
# | pinecone_index        | Information about your Pinecone index                           |
# +-----------------------+-----------------------------------------------------------------+
# | xata_api_key          | Your Xata API key                                               |
# +-----------------------+-----------------------------------------------------------------+
# | xata_db_url           | The URL for your Xata database                                  |
# +-----------------------+-----------------------------------------------------------------+
# | langchain_verbose     | Indicates if Langchain should be verbose (true/false)           |
# +-----------------------+-----------------------------------------------------------------+
# | llm_model             | The name of your LLM model                                      |
# +-----------------------+-----------------------------------------------------------------+
# | password              | Your password. If needed, set "need_passwd" to *True* in `tiangong-en.py` at line 2.|
# +-----------------------+-----------------------------------------------------------------+
# """

# lines = rst_table.strip().split("\n")
# data_lines = [line for line in lines if '|' in line and '+' not in line]
# data = []

# for line in data_lines:
#     parts = [part.strip() for part in line.split('|')[1:-1]]
#     data.append(parts)

# print(data)
