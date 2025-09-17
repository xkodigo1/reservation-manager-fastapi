🎯 Version v0.1.0 → Setup & Base

👉 Mission accomplished: project base ready, with DB connected and JWT configuration.
• feature/project-setup → folder structure, .gitignore, requirements.txt.
• feature/app-instance → FastAPI instance in main.py.
• feature/config-env → .env, settings.py with DB and JWT.
• feature/db-connection → session.py + get_db dependency.
• feature/db-models → SQLAlchemy models (User, Room, Reservation).
• feature/db-schemas → Pydantic schemas.
• feature/security-utils → password hashing, JWT utils.

📦 Release v0.1.0
• Initial project, server up and running and can connect to MySQL.
• No useful endpoints yet.

🎯 Release v0.2.0 → Auth & Users

👉 Goal: Provide JWT authentication and basic CRUD for users.
• feature/auth-routes → POST /auth/register, POST /auth/login.
• feature/users-routes → GET /users/me, GET /users, DELETE /users/{id}.

📦 Release v0.2.0
• Users can register and log in with JWT.
• Admin can list and delete users.

🎯 Version v0.3.0 → Rooms

👉 Objective: Manage rooms with roles (admin).
• feature/rooms-routes → GET /rooms, POST /rooms, PUT /rooms/{id}, DELETE /rooms/{id}.

📦 Release v0.3.0
• Rooms available with protected CRUD for admin.
