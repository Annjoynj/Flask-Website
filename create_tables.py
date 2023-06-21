
from website import create_app, db
from website.models import User, Note

app = create_app()
app.app_context().push()

with app.app_context():
    db.create_all()
