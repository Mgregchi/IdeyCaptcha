# ideycaptcha

A simple and extensible captcha solution using Django for the backend and React for the frontend. This project aims to provide an easy-to-implement captcha system where users are presented with instructions and must select the correct option from a dropdown menu. The options can be either images or text, and the selection is validated on the server.

## Features

- Provides captcha instructions and options from the Django backend.
- Options can be either images or text, based on the captcha type.
- Validates user selections on the server.
- Simple and easy to extend.

## Getting Started

### Prerequisites

- Python 3.x
- Node.js (with npm)

### Backend Setup (Django)

1. Clone the repository:

    ```bash
    git clone https://github.com/mgregchi/ideycaptcha.git
    cd ideycaptcha/backend
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations and start the server:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

### Frontend Setup (React)

1. Navigate to the frontend directory:

    ```bash
    cd ../frontend
    ```

2. Install the dependencies:

    ```bash
    npm install
    ```

3. Start the development server:

    ```bash
    npm start
    ```

### Usage

1. Ensure both backend and frontend servers are running.
2. Open your browser and navigate to `http://localhost:3000` to see the captcha in action.

## Project Structure

- `backend/`: Contains the Django backend code.
  - `captcha/`: Django app for captcha models, views, urls and serializers.
  - `backend/`: Django project settings.
  - `manage.py`: Django management script.
- `frontend/`: Contains the React frontend code.
  - `src/components/CaptchaCard.js`: Main component for displaying the captcha.

## Models

### Captcha

- `instruction`: Instruction text for the captcha.
- `captcha_type`: Type of captcha (`image` or `text`).

### Option

- `captcha`: Foreign key to the Captcha model.
- `text`: Text option (if applicable).
- `image_url`: Image URL option (if applicable).

## API Endpoints

- `GET /captcha/get-captcha/`: Fetch a random captcha.
- `POST /captcha/validate-captcha/`: Validate the user's selection.

## Future Enhancements

- Add more captcha types and options.
- Improve security and robustness of the captcha validation.
- Enhance the frontend UI/UX.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

---

### Simple Idea, Easy to Extend

This project is a basic implementation of a captcha system and is intended to be simple and straightforward. It can be enhanced and improved in various ways, making it a great starting point for learning and experimentation.

---

Feel free to replace `https://github.com/mgregchi/ideycaptcha.git` with your actual GitHub repository URL.