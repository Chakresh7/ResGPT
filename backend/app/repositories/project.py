from sqlalchemy.orm import Session

from app.models.project import Project


def create(db: Session, user_id, title: str, description: str | None) -> Project:
    project = Project(user_id=user_id, title=title, description=description)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def list_for_user(db: Session, user_id) -> list[Project]:
    return db.query(Project).filter(Project.user_id == user_id).order_by(Project.created_at.desc()).all()


def get_by_id(db: Session, project_id) -> Project | None:
    return db.query(Project).filter(Project.id == project_id).first()


def delete(db: Session, project: Project) -> None:
    db.delete(project)
    db.commit()
