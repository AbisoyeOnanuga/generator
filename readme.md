# Generator

## Contents
- [About](#A-Google-Gemini-AI-FastAPI-Service)
- [Features](#features)
- [Configuration](#configuration)
- [Model Setup](#model-setup)
- [Usage](#usage)
- [Data processing](#data-processing)
- [Response](#response)
- [Disclaimer](#disclaimer)

## A Google Gemini AI FastAPI Service

This FastAPI service utilizes the Google's Gemini AI API to process input data and generate responses based on the provided text prompts.

## Features

- **GET endpoint** at `/` which returns a welcome message.
- **POST endpoint** at `/generate` which processes the provided data and returns a generated response.

## Configuration

Before running the service, make sure to configure the Gemini AI API by setting your API key:

```
    genai.configure(api_key="YOUR_API_KEY")
```

## Model Setup
The service uses the following configuration for the Gemini AI model:
```
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                safety_settings=safety_settings)
```

## Usage
To start the FastAPI service, run:
Then, you can send a GET request to http://127.0.0.1:8000/ or a POST request to http://127.0.0.1:8000/generate with the necessary data.

## Data Processing
The /generate endpoint expects a data.csv file to be processed. The service will use the Gemini AI API to generate a response based on the content of this file.

## Response
The generated response will be printed to the console and can also be accessed via the /generate endpoint.

## Disclaimer
Please ensure that you have the right to use the Gemini AI API and that you comply with their terms of service.
```
    Remember to replace `"YOUR_API_KEY"` with your actual API key. Also, ensure that the `data.csv` file processing logic is implemented as per your requirements, as this README assumes such functionality is in place.
```
