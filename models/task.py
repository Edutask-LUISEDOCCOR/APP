from database.config import Task

class TaskModel():
    def __init__(self) -> None:
        self.task = Task

    def create(self, title, content, user_id):
        try:
            data = self.task(title=title, content=content, user=user_id)
            data.save()
            return data
        except:
            return False

    def getById(self, task_id, user_id):
        try:
            task = self.task.get(id=task_id, user=user_id)
            return task
        except:
            return False

    def change_status(self, task_id, user_id):
        try:
            task = self.getById(task_id, user_id)
            if(not task): 
                return False
            query = self.task.update(isDone=(not task.isDone)).where(self.task.id == task_id)
            query.execute()
            return True
        except:
            return False
    
    def delete(self, task_id, user_id):
        try:
            task = self.getById(task_id, user_id)
            if(not task): 
                return False
            query = self.task.delete().where(self.task.id == task_id)
            query.execute()
            return True
        except:
            return False
    
    def update(self, task_id, user_id, title, content):
        try:
            task = self.getById(task_id, user_id)
            if(not task): 
                return False
            query = self.task.update(title=title, content=content).where(self.task.id == task_id)
            query.execute()
            return True
        except:
            return False