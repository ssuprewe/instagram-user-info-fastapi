# Basic API Scraper Template

A minimal, barebones [FastAPI](https://fastapi.tiangolo.com/) template designed for one simple task: to take a `username`, query an external API endpoint with it, and return the raw JSON response.

This project is intended as a starting point or a boilerplate for developers who need to quickly set up a simple API proxy or scraper to see what data an endpoint returns.

## Features

-   Single, dynamic endpoint: `/api/{username}`
-   Proxies the request to an external source.
-   Returns the untouched JSON data from the source.
-   Basic error handling for 404 (Not Found) and connection issues.

## How to Run

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Start the server:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be running at `http://127.0.0.1:8000`.

## Usage Example

Once the server is running, you can test it by visiting the following URL in your browser or API client to see the JSON response:

`http://127.0.0.1:8000/api/instagram`

You can also access the auto-generated documentation at `http://127.0.0.1:8000/docs`.

---

### **Disclaimer**

The example URL in the code (`main.py`) points to an Instagram endpoint. Web scraping may be against the Terms of Service of many websites, including Instagram. This code is provided for **educational purposes only**. The user assumes all responsibility for its use. Endpoints from third-party services can change or be deprecated at any time.
