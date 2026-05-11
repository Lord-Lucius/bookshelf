```
bookshelf/
├── app/
│   ├── __init__.py
│   ├── main.py                    # Création de l'app FastAPI, montage des routers
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py              # Settings via pydantic-settings (env vars)
│   │   ├── security.py            # Hash password, création/décodage JWT
│   │   └── dependencies.py        # get_current_user, get_db, etc.
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── session.py             # SessionLocal, engine SQLAlchemy
│   │   └── base.py                # Base déclarative SQLAlchemy
│   │
│   ├── models/                    # Modèles SQLAlchemy (DB)
│   │   ├── __init__.py
│   │   ├── book.py
│   │   ├── note.py
│   │   ├── user.py
│   │   └── refresh_token.py
│   │
│   ├── schemas/                   # Modèles Pydantic (HTTP)
│   │   ├── __init__.py
│   │   ├── book.py                # BookCreate, BookUpdate, BookRead
│   │   ├── note.py
│   │   ├── user.py
│   │   ├── auth.py                # LoginRequest, TokenPair, RefreshRequest
│   │   └── common.py              # PaginatedResponse, ErrorResponse
│   │
│   ├── repositories/              # Accès DB pur, requêtes SQLAlchemy
│   │   ├── __init__.py
│   │   ├── book.py
│   │   ├── note.py
│   │   ├── user.py
│   │   └── refresh_token.py
│   │
│   ├── services/                  # Logique métier
│   │   ├── __init__.py
│   │   ├── book_service.py
│   │   ├── note_service.py
│   │   ├── user_service.py
│   │   └── auth_service.py
│   │
│   ├── routes/                    # Endpoints HTTP
│   │   ├── __init__.py
│   │   ├── books.py
│   │   ├── notes.py
│   │   ├── users.py
│   │   ├── auth.py
│   │   └── health.py              # GET / et GET /health
│   │
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── request_id.py          # X-Request-ID
│   │   └── logging.py             # Log de chaque requête
│   │
│   └── exceptions/
│       ├── __init__.py
│       ├── handlers.py            # Exception handlers FastAPI
│       └── errors.py              # Classes d'erreurs métier (BookNotFound, etc.)
│
├── alembic/
│   ├── versions/                  # Tes migrations (générées)
│   ├── env.py
│   └── script.py.mako
├── alembic.ini
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                # Fixtures pytest (DB en mémoire, client, user de test)
│   ├── test_books.py
│   ├── test_notes.py
│   ├── test_auth.py
│   └── test_ownership.py
│
├── docker/
│   ├── Dockerfile
│   └── Caddyfile
├── docker-compose.yml
│
├── .env.example                   # Template des variables d'environnement
├── .gitignore
├── .python-version
├── pyproject.toml                 # Dépendances + config ruff, mypy, pytest
├── README.md
└── JOURNAL.md                     # Ton journal d'apprentissage
```
