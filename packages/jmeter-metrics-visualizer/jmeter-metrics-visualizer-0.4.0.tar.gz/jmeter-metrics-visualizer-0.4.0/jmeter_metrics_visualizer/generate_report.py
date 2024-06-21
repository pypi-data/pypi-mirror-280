import pandas as pd
import plotly.express as px
import plotly.io as pio
from jinja2 import Template
from datetime import datetime
import pkg_resources


def load_csv(file_paths):
    """Load CSV files into a list of DataFrames and extract file labels from timestamps."""
    dfs = []
    labels = []
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        dfs.append(df)

        # Extract the timestamp from the first row
        timestamp_str = df['timeStamp'][0]
        # Convert to datetime object
        timestamp = datetime.fromtimestamp(int(timestamp_str) / 1000)
        # Extract month and year
        file_label = timestamp.strftime('%B %Y %H:%M')

        # Extract number of virtual users
        virtual_users = df['allThreads'].unique().size

        # Combine label with number of virtual users
        file_label = f'{file_label} (Virtual Users: {virtual_users})'

        labels.append(file_label)

    return dfs, labels


def calculate_metrics(dfs):
    """Calculate important metrics from the list of DataFrames."""
    avg_response_times = [df['elapsed'].mean() for df in dfs]
    error_rates = [(df['success'] == False).sum() / df.shape[0] if df.shape[0] != 0 else 0 for df in dfs]
    return avg_response_times, error_rates


def filter_data(dfs, label):
    """Filter data based on the label for each DataFrame in the list."""
    filtered_dfs = [df[df['label'] == label] for df in dfs]
    return filtered_dfs


def generate_html_report(file_paths, output_path):
    # Load CSV files
    dfs, file_labels = load_csv(file_paths)

    # Calculate overall error rates for each file
    overall_error_rates = [(df['success'] == False).sum() / df.shape[0] * 100 if df.shape[0] != 0 else 0 for df in dfs]

    # Get unique labels (scenarios) from the first dataframe
    labels = dfs[0]['label'].unique()

    # Dictionary to hold HTML plots and error percentages for each label
    response_time_plots = {}
    error_rate_plots = {}
    error_percentages = {}

    # Dictionary to hold total virtual users for each label
    total_virtual_users = {}

    # Generate plots and calculate error percentages for each label
    for label in labels:
        filtered_dfs = filter_data(dfs, label)

        avg_response_times, error_rates = calculate_metrics(filtered_dfs)

        # Create a DataFrame for response times
        response_time_data = {
            'File': file_labels,
            'Avg Response Time (ms)': avg_response_times,
            'Color': ['Color {}'.format(i+1) for i in range(len(file_labels))]
        }
        response_time_df = pd.DataFrame(response_time_data)

        # Create a DataFrame for error rates
        error_rate_data = {
            'File': file_labels,
            'Error Rate (%)': [rate * 100 for rate in error_rates],
            'Color': ['Color {}'.format(i+1) for i in range(len(file_labels))]
        }
        error_rate_df = pd.DataFrame(error_rate_data)

        # Generate the response time plot
        response_time_fig = px.bar(
            response_time_df, x='File', y='Avg Response Time (ms)',
            title=f'Average Response Time for Scenario: {label}',
            labels={'Avg Response Time (ms)': 'Avg Response Time (ms)', 'File': 'Date & Virtual Users'},
            color='Color'
        )
        response_time_fig.update_layout(
            autosize=False,
            width=600,
            height=400,
            margin=dict(l=50, r=50, b=100, t=100, pad=4),
            paper_bgcolor="White",
        )
        response_time_plot_html = pio.to_html(response_time_fig, full_html=False)
        response_time_plots[label] = response_time_plot_html

        # Generate the error rate plot
        error_rate_fig = px.bar(
            error_rate_df, x='File', y='Error Rate (%)',
            title=f'Error Percentage for Scenario: {label}',
            labels={'Error Percentage (%)': 'Error Percentage (%)', 'File': 'Date & Virtual Users'},
            color='Color'
        )
        error_rate_fig.update_layout(
            autosize=False,
            width=600,
            height=400,
            margin=dict(l=50, r=50, b=100, t=100, pad=4),
            paper_bgcolor="White",
        )
        error_rate_plot_html = pio.to_html(error_rate_fig, full_html=False)
        error_rate_plots[label] = error_rate_plot_html

        error_percentages[label] = [rate * 100 for rate in error_rates]

        # Calculate total virtual users for the label
        total_virtual_users[label] = filtered_dfs[0].shape[0]

    # Dropdown options for labels (scenarios)
    label_options = [{'label': label, 'value': label} for label in labels]

    # Create a dictionary to store tables for each unique virtual user count
    virtual_user_tables = {}

    # Populate the virtual user tables dictionary
    for i in range(len(overall_error_rates)):
        virtual_users = file_labels[i].split('(')[-1].split(')')[0].split(': ')[-1]
        date = file_labels[i].split(' (')[0]
        error_rate = overall_error_rates[i]

        if virtual_users not in virtual_user_tables:
            virtual_user_tables[virtual_users] = []

        virtual_user_tables[virtual_users].append({'date': date, 'error_rate': error_rate})

    # Load the HTML template from the package
    template_path = pkg_resources.resource_filename('jmeter_metrics_visualizer', 'template/template.html')
    with open(template_path, 'r', encoding='utf-8') as file:
        html_template = file.read()

    # Render the HTML report with virtual user tables
    template = Template(html_template)
    html_content = template.render(response_time_plots=response_time_plots, error_rate_plots=error_rate_plots,
                                   label_options=label_options, labels=labels,
                                   virtual_user_tables=virtual_user_tables)

    # Save the HTML report to a file with UTF-8 encoding explicitly specified
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"HTML report generated: {output_path}")
