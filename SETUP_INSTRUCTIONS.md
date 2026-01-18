# Job Application Tracker Setup

## Prerequisites
- Python 3.10+
- Flutter SDK 3.10+

## Backend Setup (Django)

1. Navigate to the root directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the server:
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/api/v1/`.

## Frontend Setup (Flutter)

1. Navigate to `flutter_app`:
   ```bash
   cd flutter_app
   ```
2. Install dependencies:
   ```bash
   flutter pub get
   ```
3. Run the app:
   - For Web:
     ```bash
     flutter run -d chrome
     ```
   - For Windows:
     ```bash
     flutter run -d windows
     ```

## Notes
- **API URL**: The app is configured to connect to `http://127.0.0.1:8000/api/v1`. If running on Android Emulator, you may need to change `baseUrl` in `lib/services/api_service.dart` to `http://10.0.2.2:8000/api/v1`.
- **Authentication**: You must Sign Up / Login in the app to access data.
- **Charts**: The dashboard uses `fl_chart` for visualization.
