from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        self.client.post("/login_action", {"username": "wujianxin1", "password": "wjx@wjx77I"})

    # 使用task修饰该方法为一个事务,数字代表权重，越大则权重越大
    @task(2)
    def event_manage(self):
        self.client.get("/event_manage")

    @task(2)
    def guest_manage(self):
        self.client.get("/guest_manage")


class APIBehavior(TaskSet):
    @task()
    def user_sign(self):
        self.client.post("/api/user_sign/", data={"eid": "1", "phone": "11111111111"})


class WebsiteUser(HttpLocust):
    # 指向一个定义的用户行为类
    # task_set = UserBehavior
    task_set = APIBehavior
    # 事务直接用户等待时间的下界
    min_wait = 0
    # 事务直接用户等待时间的上界
    max_wait = 0
