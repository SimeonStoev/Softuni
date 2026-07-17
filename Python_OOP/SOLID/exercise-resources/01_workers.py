from abc import ABC, abstractmethod


class AbsWorkers(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(AbsWorkers):

    def work(self):
        print("I'm working!!")


class SuperWorker(AbsWorkers):

    def work(self):
        print("I work very hard!!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbsWorkers), '`worker` must be of type {}'.format(AbsWorkers)

        self.worker = worker

    def manage(self):
        if self.worker:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
