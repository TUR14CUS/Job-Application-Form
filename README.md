# Job Application Form

This is a simple web application built using Flask for collecting job applications. It includes a form with fields for the applicant's personal information, and the submitted data is stored in a SQLite database. Additionally, an email notification is sent to the applicant using Flask-Mail.

## Prerequisites

Make sure you have the following installed on your system:

- Python (3.6 or higher)
- Flask
- Flask-SQLAlchemy
- Flask-Mail

You can install the required packages using the following command:

```bash
pip install Flask Flask-SQLAlchemy Flask-Mail
```

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/TUR14CUs/job-application-form.git
cd job-application-form
```

2. Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure the application:

   - Open `main.py` and update the configuration variables under `app.config`:
      - `SECRET_KEY`: Change to a secure random key.
      - `SQLALCHEMY_DATABASE_URI`: Set the database URI.
      - `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USE_SSL`, `MAIL_USERNAME`, `MAIL_PASSWORD`: Configure your email server details.

5. Initialize the database:

```bash
python main.py
```

This will create an SQLite database file named `database.db`.

6. Run the application:

```bash
python main.py
```

The application will be accessible at [http://localhost:5001](http://localhost:5001).

## Usage

- Access the application through a web browser.
- Fill out the job application form and submit.
- A confirmation message will be displayed, and an email will be sent to the provided email address.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize the README further based on your project's specific details and requirements.