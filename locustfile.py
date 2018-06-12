
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(1)
    def index(self):
        self.client.get("http://www.testfan.cn/")

    @task(2)
    def search(self):
        self.client.get("http://www.testfan.cn/list/2/220.htm")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
                