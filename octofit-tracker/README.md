# OctoFit Tracker

A fitness tracking application built with Django REST Framework backend and React frontend.

## Features

- **User Management**: Track users and their team affiliations
- **Team Competition**: Compete with Marvel vs DC superhero teams
- **Activity Logging**: Log various fitness activities (running, walking, cycling, swimming, strength training)
- **Leaderboard**: View rankings based on total points and activities
- **Workout Suggestions**: Get personalized workout recommendations

## Technology Stack

### Backend
- **Django 4.1.7**: Web framework
- **Django REST Framework**: API development
- **SQLite**: Database (configured for MongoDB compatibility with Djongo)
- **CORS Headers**: Cross-origin resource sharing

### Frontend
- **React**: UI framework
- **React Router**: Navigation
- **Bootstrap**: Styling and responsive design

## Project Structure

```
octofit-tracker/
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── db.sqlite3
│   ├── venv/
│   └── octofit_tracker/
│       ├── settings.py
│       ├── urls.py
│       ├── views.py
│       ├── models.py
│       ├── serializers.py
│       ├── admin.py
│       ├── migrations/
│       └── management/
│           └── commands/
│               └── populate_db.py
└── frontend/
    ├── package.json
    ├── public/
    └── src/
        ├── App.js
        ├── App.css
        ├── index.js
        └── components/
            ├── Users.js
            ├── Teams.js
            ├── Activities.js
            ├── Leaderboard.js
            └── Workouts.js
```

## Setup Instructions

### Backend Setup

1. Create and activate virtual environment:
```bash
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r octofit-tracker/backend/requirements.txt
```

3. Run migrations:
```bash
cd octofit-tracker/backend
python manage.py makemigrations
python manage.py migrate
```

4. Populate database with test data:
```bash
python manage.py populate_db
```

5. Start Django development server:
```bash
python manage.py runserver 0.0.0.0:8000
```

The API will be available at `http://localhost:8000/api/`

### Frontend Setup

1. Install dependencies:
```bash
cd octofit-tracker/frontend
npm install
```

2. Start React development server:
```bash
npm start
```

The React app will be available at `http://localhost:3000`

## API Endpoints

- `GET /api/` - API root with all endpoint links
- `GET /api/users/` - List all users
- `GET /api/teams/` - List all teams
- `GET /api/activities/` - List all activities
- `GET /api/leaderboard/` - View leaderboard rankings
- `GET /api/workouts/` - Get workout suggestions

All endpoints support standard REST operations (GET, POST, PUT, PATCH, DELETE).

## GitHub Codespaces Support

The application is configured to work in GitHub Codespaces with:
- Automatic ALLOWED_HOSTS configuration for Codespace URLs
- CORS enabled for cross-origin requests
- Environment variable support for CODESPACE_NAME

## Sample Data

The application comes pre-populated with:
- 2 teams (Team Marvel and Team DC)
- 10 superhero users
- 80+ activity entries
- Leaderboard rankings
- 5 workout suggestions

## Development Notes

- The backend uses SQLite for development but is structured to work with MongoDB using Djongo
- CORS is enabled for all origins in development
- REST Framework pagination is set to 10 items per page
- Bootstrap is used for responsive design
- React Router handles client-side routing

## License

MIT License
