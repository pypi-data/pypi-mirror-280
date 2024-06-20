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
   pip install unique-log-questions
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

## Usage

## Usage

1. **Integrate the library in your code:**

   **settings.py:**

   Add `unique_log_question_app` to your `INSTALLED_APPS` list:

   ```python
   INSTALLED_APPS = [

       'unique_log_question_app',
   ]
   ```

**views.py:**

```python
from unique_log_question_app.views import display_log_questions  # for log questions
from unique_log_question_app.views import display_unique_questions  # for unique questions
from unique_log_question_app.views import delete_chat_session  # for delete unique questions
from unique_log_question_app.views import delete_log_question  # for delete log questions
from unique_log_question_app.views import edit_chat_session    # for edit chat sessions
from unique_log_question_app.views import edit_similar_question  # for edit similar questions
```

**urls.py:**

```python
from django.urls import path
from unique_log_question_app.views import display_unique_questions, display_log_questions,delete_log_question,delete_chat_session,edit_chat_session,edit_similar_question

urlpatterns = [
    path('unique_questions/', display_unique_questions, name='display_unique_questions'),
    path('log_questions/', display_log_questions, name='display_log_questions'),
    path('delete_unique/<int:session_id>/', delete_chat_session, name='delete_chat_session'),
    path('delete_log/<int:question_id>/', delete_log_question, name='qna_delete_log'),
    path('log_questions/', display_log_questions, name='display_log_answers'),
    path('edit_chat_session/<int:session_id>/', edit_chat_session, name='edit_chat_session'),
    path('edit_similar_question/<int:question_id>/', edit_similar_question, name='edit_similar_question'),
]
```
