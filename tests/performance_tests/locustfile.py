from locust import HttpUser, task

class ProjetPerfTest(HttpUser):

    @task
    def login(self):
        self.client.post("/showSummary", data={"email":"admin@ironman.com"})

    @task
    def pointBoard(self):
        self.client.get('/pointsBoard')