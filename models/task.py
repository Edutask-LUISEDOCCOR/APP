from database.config import Task

class TaskModel():
    def __init__(self) -> None:
        self.task = Task

    def create(self, title, content, user_id):
        #try:
            data = self.task(title=title, content=content, user=user_id)
            data.save()
            return data
        #except:
            return False