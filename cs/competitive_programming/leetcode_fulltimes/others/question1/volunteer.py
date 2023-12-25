class Volunteer(object):
    def __init__(self, name):
        self._name = name  # string
        self.interested_tasks = []

    def __str__(self):
        return str(self._name)

    def __repr__(self):
        return str(self._name)

    @property
    def name(self):
        return self._name

    def __lt__(self, other):
        return True

    def add_interested_task(self, task):
        self.interested_tasks.append(task)

    def remove_interested_task(self, task):
        self.interested_tasks.remove(task)

    def is_interested(self, task):
        return task in self.interested_tasks

    def get_task_desirability_score(self, task):
        """
        Returns a float representing how desirable the given task is to this
        volunteer.
        """
        for idx_of_task in range(len(self.interested_tasks)):
            if self.interested_tasks[idx_of_task] == task:
                return (1/(idx_of_task+1))

        return 0
