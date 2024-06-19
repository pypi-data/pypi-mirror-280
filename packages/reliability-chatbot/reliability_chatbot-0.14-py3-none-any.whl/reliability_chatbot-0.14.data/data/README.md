# My Django Package

My Django Package is a web application for managing and querying documents using a chatbot interface. It supports multiple file formats, extracts text from documents, and uses an AI model to answer questions based on the content of uploaded documents.

## Features

- View and manage chat sessions

## Installation

### Prerequisites

- Python 3.11
- Django 3.2 or higher

### Steps

1. **Install the package:**

   ```bash
   pip install reliability-chatbot
   ```

2. **Set up a virtual environment:**

   ```bash
   pip install virtualenv

   virtualenv env

   # On Windows
   .\env\Scripts\activate

   # On macOS/Linux
   source env/bin/activate
   ```

3. **Set up the Django project:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

4. **Open your browser and navigate to:**

   ```plaintext
   http://127.0.0.1:8000/
   ```

   This will display your Django project with the integrated `app1` app.

## Usage

1. **Integrate the library in your code:**
   **settings.py:**

   Add `app1` to your `INSTALLED_APPS` list:

   ```python
   INSTALLED_APPS = [

       'app1',

   ]
   ```

**views.py:**

```python
from app1.views import save_to_database  # to save questions and answers in the database
from app1.views import get_answer_from_database  # to check answers from database before asking llm
```

**urls.py:**

```python
from django.urls import path
from app1.views import submit_feedback   # to send feedback for the generated or retrieved answer

urlpatterns = [
    path('submit_feedback/', submit_feedback, name='submit_feedback'),
    # other paths...
]
```

By following these instructions, you should be able to set up and use your Django package correctly.
