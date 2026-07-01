from flask import Flask

from app.config import Config
from app.extensions import db, migrate, login_manager


def create_app():
    from app.routes.auth import auth
    from app.routes.home import home
    from app.routes.like import like
    from app.routes.post import post
    from app.routes.profile import profile
    from app.routes.follow import follow  
    from app.routes.comment import comment 
    from app.routes.notification import notification
    from app.routes.search import search
    from app.routes.message import message

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    
    app.register_blueprint(post)
    app.register_blueprint(auth)
    app.register_blueprint(home)
    app.register_blueprint(like)
    app.register_blueprint(profile)
    app.register_blueprint(follow)      
    app.register_blueprint(comment)
    app.register_blueprint(notification)
    app.register_blueprint(search)
    app.register_blueprint(message)

    return app