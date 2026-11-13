"""Zero to AI Engineer · Python · Part 11 of 25
Slide: Enter Cleans Up Its Own Mess
Run: python 10_enter_cleans_up_its_own_mess.py
"""
class TxBase:
    def __init__(self, pool):
        self.pool = pool
    def __enter__(self):
        self.conn = self.pool.acquire()
        try:
            self.conn.begin()
        except BaseException:
            # __exit__ will not run
            self.pool.release(self.conn)
            raise
        return self.conn
