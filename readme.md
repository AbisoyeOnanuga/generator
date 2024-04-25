## Generator

# A Google Gemini AI FastAPI Service

This FastAPI service utilizes the Google's Gemini AI API to process input data and generate responses based on the provided text prompts.

## Features

- **GET endpoint** at `/` which returns a welcome message.
- **POST endpoint** at `/generate` which processes the provided data and returns a generated response.

## Configuration

Before running the service, make sure to configure the Gemini AI API by setting your API key:

```python
genai.configure(api_key="YOUR_API_KEY")
