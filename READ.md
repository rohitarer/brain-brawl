Planned project structure
brain-brawl-api/
├── main.py              # FastAPI entry point
├── database.py          # DB connection & sessions
├── routers/             # API endpoints
├── schemas/             # Pydantic validation
├── services/            # Quiz and scoring logic
├── repositories/        # Database queries
├── db_models/           # SQLAlchemy models
├── core/                # JWT, config, security
├── tests/               # Pytest
├── .env                 # Environment variables
└── requirements.txt


Main modules
Module	        Features
Users	        Register, login, profile
Categories	    Science, Movies, Technology
Questions	    Create, list, update, delete
Gameplay	    Start quiz, submit answers, calculate score
Results	        Score history, previous attempts
Leaderboard	    Rankings and highest scores