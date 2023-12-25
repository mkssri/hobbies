from util import load_volunteers, load_tasks


class AssignmentServer(object):
    def __init__(self):
        self.assignments = {}  # Maps Volunteer -> Set of Tasks
        self.tasks = {}  # Maps task_id -> Task
        self.volunteers = []

    def import_tasks_from_csv(self, csv_filename):
        self.tasks = load_tasks(csv_filename)

    def import_volunteers_from_csv(self, csv_filename):
        self.volunteers.extend(load_volunteers(csv_filename, self.tasks))

    def get_interested_volunteers(self, task, improve=False):
        """
        Returns a List of the Volunteers who have indicated interest in the 
        given task.
        """
        interested_volunteers = []

        # Iterate over all volunteers
        for volunteer in self.volunteers:
            # Iterate over each interested task of above volunteer
            for interest_task in volunteer.interested_tasks:
                # If interested task matches the given task
                if interest_task == task:
                    # Form a tuple with desirability score and volunteer, and add it to a list
                    desirability_score_volunteer_tuple = (volunteer.get_task_desirability_score(interest_task), volunteer)
                    interested_volunteers.append(desirability_score_volunteer_tuple)
        # Sort this list based on desirability score in descending order.
        # ------------- This is the improvement Algorithm -----------------------
        if improve:
            interested_volunteers.sort(reverse=True)
        # Extract the volunteers objects and return
        return [volunteer_tuple[1] for volunteer_tuple in interested_volunteers]

    def get_tasks_by_desirability(self):
        """
        Returns a List of Tasks sorted by desirability.
        """

        task_desirability_tuples = []
        for task_id in self.tasks:
            interested_volunteers = self.get_interested_volunteers(self.tasks[task_id])

            task_desirability_score=0.0
            for volunteer in interested_volunteers:
                task_desirability_score += volunteer.get_task_desirability_score(self.tasks[task_id])
                # Store tuple of people facing, task desirability and the task
            task_desirability_tuples.append((self.tasks[task_id]._people_facing, task_desirability_score,self.tasks[task_id]))

        # sort this list of tuples by inverse order in people facing, desirability score
        task_desirability_tuples.sort(reverse=True)
        
        return [task_tuple[2] for task_tuple in task_desirability_tuples]

    def assign_tasks(self, improve = False):
        """
        Assigns Tasks to Volunteers by inserting them into the assignment map,
        in order of desirability. Tasks are assigned to the first Volunteer with
        interest. If there are no interested Volunteers, they are assigned to the
        first available Volunteer.
        """
        for task in self.get_tasks_by_desirability():
            interested_volunteers = self.get_interested_volunteers(task, improve)

            if len(interested_volunteers) > 0:
                self.assign_task(task, interested_volunteers[0])
            elif len(self.volunteers) > 0:
                self.assign_task(task, self.volunteers[0])

    def assign_task(self, task, volunteer):
        """
        Adds the given Task to the specified Volunteer's Set of assigned Tasks.
        """
        if volunteer not in self.assignments:
            self.assignments[volunteer] = set()
        self.assignments[volunteer].add(task)

    def assign_tasks_improved(self):
        """
        Assigns Tasks to Volunteers based on their interests.
        """
        # We are improving the algorithm by sorting the interested volunteers list by their task desirability score
        # This is improving the satisfaction from 12 to 38

        self.assign_tasks(True)
        pass
