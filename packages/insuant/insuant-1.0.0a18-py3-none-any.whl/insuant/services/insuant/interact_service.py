from insuant.services.database.models.interact import UserRequest, SystemResponse, InteractionTask, UserInteraction
from insuant.database import SessionLocal


class InteractService:
    def __init__(self):
        self.db = SessionLocal()

    def create_user_request(self, user_request: UserRequest):
        self.db.add(user_request)
        self.db.commit()
        self.db.refresh(user_request)
        return user_request

    def create_system_response(self, system_response: SystemResponse):
        self.db.add(system_response)
        self.db.commit()
        self.db.refresh(system_response)
        return system_response

    def create_interaction_task(self, interaction_task: InteractionTask):
        self.db.add(interaction_task)
        self.db.commit()
        self.db.refresh(interaction_task)
        return interaction_task

    def create_user_interaction(self, user_interaction: UserInteraction):
        self.db.add(user_interaction)
        self.db.commit()
        self.db.refresh(user_interaction)
        return user_interaction

    def get_user_interaction(self, id: int):
        return self.db.query(UserInteraction).filter(UserInteraction.id == id).first()

    def get_user_interactions(self, user_id: int):
        return self.db.query(UserInteraction).filter(UserInteraction.user_id == user_id).all()

    def get_all_sessions(self):
        # retrive all sessions descending sorted by timestamp
        return self.db.query(UserInteraction).order_by(UserInteraction.timestamp.desc()).all()

    def update_user_interaction(self):
        pass
