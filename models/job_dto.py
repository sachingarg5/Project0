class Job:
    def __init__(self,job_id: int,user_id: int, job_type:str,description:str,budget:int,contact:str):
        self.job_id = job_id
        self.user_id=user_id
        self.job_type=job_type
        self.description=description
        self.budget=budget
        self.contact=contact

    def __repr__(self) -> str:
        return f"Job Info: {self.job_id} + {self.user_id} + {self.job_type} + {self.description} + {self.budget} + {self.contact}"