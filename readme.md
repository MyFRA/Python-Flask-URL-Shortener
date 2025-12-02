## URL SHORTENER

a simple url shortener build with python + flask + postgresql

### Installation

-   `pip install -r requirements.txt`
-   Edit environment variables
    -   `cp .env.example .env`
    -   change value in .env
        -   `SQLALCHEMY_DATABASE_URI="postgresql://postgres:12345@localhost:5433/your_db"`
-   Migrate Database
    -   `flask --app src/main.py db init`
    -   `flask --app src/main.py db migrate`
    -   `flask --app src/main.py db upgrade`
-   Run your app
    -   `python src/main.py`

### Endpoint

1. **POST** `/shorten`

    Desc: generate shortener url

    `Request Body (JSON):`

    ```json
    {
        "url": "https://www.example.com"
    }
    ```

    `Response(JSON):`

    ```json
    {
        "short_url": "localhost:5000/aekbK"
    }
    ```

2. **GET** `/{code}`

    Desc: get original url

    `Response(JSON):`

    ```json
    {
        "amount_clicked": 0,
        "code": "MBaud",
        "created_at": "2025-12-02T03:52:03.403075",
        "id": 14,
        "url": "https://google.com"
    }
    ```
