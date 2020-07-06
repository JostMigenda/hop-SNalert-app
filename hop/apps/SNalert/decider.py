import db_storage

class Decider(object):
    def __init__(self, time_threshold, datetime_format):
        # intialize and use redis storage
        self.db = db_storage.storage(time_threshold, datetime_format)

    def deciding(self):
        """

        :return: True or false indicating the possibility of a supernova
        """
        # if self.db.cacheEmpty() == True:
        #     return False
        return not self.db.cacheEmpty()

    def add_log(self, time, message):
        """
        logs should be a gcn or other format of record retrieved from hopskotch stream.
        :param logs:
        :return:
        """
        # insert it the deque
        self.db.insert(time, message)