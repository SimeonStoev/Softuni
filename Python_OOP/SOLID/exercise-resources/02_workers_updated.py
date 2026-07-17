from abc import ABCMeta, abstractmethod
import time


class AbstractWorkable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def work(self):
        pass


class AbstractEatable(AbstractWorkable):
    @abstractmethod
    def eat(self):
        pass


class Worker(AbstractEatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(AbstractEatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(AbstractWorkable):

    def work(self):
        print("I'm a robot. I'm working....")


class WorkManager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorkable), "`worker` must be of type {}".format(AbstractWorkable)

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(WorkManager):
    def __init__(self):
        super().__init__()

    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass
