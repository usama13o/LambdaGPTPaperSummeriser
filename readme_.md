# Notion + Lambda + OpenAI ChatGPT PDF Summary Tool

This tool is designed to help you summarize PDFs of research papers and add the summaries back into your Notion databases. It uses the Notion API to access your databases, the OpenAI ChatGPT model to generate the summaries, and AWS Lambda to run the code.

## Installation

To use this tool, you'll need to have Python and pip installed on your machine. You'll also need to install the following packages:

- `notion-client`
- `openai`

You can install these packages by running the following command:

## Usage

To use this tool, you'll need to set up a few things first:

1. Set up a Notion integration and get your API key.
2. Create a database in Notion to store your research papers.
3. Create a Lambda function in AWS and upload the code.
4. Set up an API Gateway to trigger the Lambda function.

Once you've set up these things, you can start using the tool. Here's how:

1. Use the Notion API to retrieve the PDFs of your research papers.
3. Use the OpenAI ChatGPT model to generate a summary of the text.
4. Use the Notion API to add the summary back into your database.

You can run the tool manually or set up a cron job to run it automatically at regular intervals.

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.