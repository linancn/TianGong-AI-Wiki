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
data = [['**Repository**', 'Select the repository you want to deploy. Default is the *current repository*.'], ['**Branch**', 'Select the branch you want to deploy. Default is *main*.'], ['**Main file path**', 'Set the path to the main Python script that runs your app. Keep the default settings.'], ['**App URL (Optional)**', 'Set the URL where your app will be deployed. Default is *https://share.streamlit.io/your-username/your-repo-name*.']]

print(generate_rst_table(headers, data))

# rst_table = """
# +-----------------+--------------------------------------------------------------------------------------------------+
# | **Repository**  | Select the repository you want to deploy. Default is the *current repository*.                 |
# +-----------------+--------------------------------------------------------------------------------------------------+
# | **Branch**      | Select the branch you want to deploy. Default is *main*.                                       |
# +-----------------+--------------------------------------------------------------------------------------------------+
# | **Main file path**   | Set the path to the main Python script that runs your app. Keep the default settings.            |
# +-----------------+--------------------------------------------------------------------------------------------------+
# | **App URL (Optional)**     | Set the URL where your app will be deployed. Default is *https://share.streamlit.io/your-username/your-repo-name*.       |
# +-----------------+--------------------------------------------------------------------------------------------------+
# """

# lines = rst_table.strip().split("\n")
# data_lines = [line for line in lines if '|' in line and '+' not in line]
# data = []

# for line in data_lines:
#     parts = [part.strip() for part in line.split('|')[1:-1]]
#     data.append(parts)

# print(data)
