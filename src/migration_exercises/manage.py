from .app import create_app
from .extensions import db
from .models import Student, Assignment, Grade
app = create_app()


if __name__ == "__main__":
    app.run(debug=True)