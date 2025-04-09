# Chatbox - AI-Powered Telecom Data Analysis

Chatbox is an AI-powered application designed to process and analyze telecom-related files using a local Qwen 2.5 7B LLM. The application provides natural language interaction for querying telecom data, including Call Detail Records (CDRs), revenue data, and financial transactions.

## Features

- Natural language query processing for telecom data analysis
- Support for various file formats (CSV, JSON, XML, PDF, etc.)
- Local LLM processing using Qwen 2.5 7B
- Modern web interface for data visualization
- Secure file management and data processing

## Tech Stack

- **Backend**:
  - Python (FastAPI)
  - Rust (for performance-critical components)
  - LangChain & LangGraph
  - SQLAlchemy (Database ORM)
  - Qwen 2.5 7B LLM

- **Frontend**:
  - React with TypeScript
  - Material-UI
  - Chart.js for visualizations

## Prerequisites

- Python 3.8+
- Node.js 14+
- Rust (latest stable version)
- CUDA-capable GPU (recommended)
- PostgreSQL (optional, SQLite by default)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chatbox.git
   cd chatbox
   ```

2. Set up the Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

4. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Update the variables as needed

5. Initialize the database:
   ```bash
   cd backend
   python -m models.database
   ```

## Running the Application

1. Start the backend server:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

2. Start the frontend development server:
   ```bash
   cd frontend
   npm start
   ```

3. Access the application at `http://localhost:3000`

## Usage

1. Upload telecom data files through the web interface
2. Use natural language queries to analyze data, e.g.:
   - "What was the total revenue from the North region in Q3 2023?"
   - "Find anomalies in the CDR data for last week"
3. View results in text, tabular, or chart format

## API Documentation

The API documentation is available at `http://localhost:8000/docs` when the backend server is running.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers. 