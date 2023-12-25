"""
A Task represents a duty to be assigned to a volunteer.
Tasks contain an id, name, and a description, as well as a flag indicating
whether the task is people-facing.
"""


class Task(object):
    def __init__(self, id, name, people_facing, description):
        self._id = id  # int
        self._name = name  # string
        self._people_facing = people_facing  # boolean
        self._description = description  # 
    
    def __eq__(self, other ):
        return self._id == other._id
    
    def __hash__(self):
        return hash((self._id, self._name, self._people_facing, self._description))

    def __str__(self):
        return f"Task #{self.id}: {self.name}"

    def __repr__(self):
        return f"Task({self.__dict__})"

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def people_facing(self):
        return self._people_facing
