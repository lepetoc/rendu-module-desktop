import json
import os

class tasks_manager:
    def __init__(self, tasks_file_path):
        self.tasks_file_path = tasks_file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from the JSON file."""
        if not os.path.exists(self.tasks_file_path):
            return {}
        with open(self.tasks_file_path, "r") as file:
            tasks = json.load(file)
        return tasks

    def save_tasks(self):
        """Save tasks to the JSON file."""
        with open(self.tasks_file_path, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task_description):
        """Add a new task."""
        # Ensure all keys are integers and find the max
        int_keys = [int(k) for k in self.tasks.keys() if k.isdigit()]
        task_id = max(int_keys, default=0) + 1
        self.tasks[task_id] = task_description
        self.save_tasks()
        print(f"Task added with ID: {task_id}")

    def delete_task(self, task_id):
        """Delete an existing task."""
        if task_id in self.tasks:
            del self.tasks[task_id]
            self.save_tasks()
            print(f"Task {task_id} deleted.")
        else:
            print(f"Task {task_id} not found.")