"""Zero to AI Engineer · Python · Part 11 of 25
Slide: Commit, Roll Back, Always Release
Run: python 11_commit_roll_back_always_release.py
"""
# --- repeated from 10_enter_cleans_up_its_own_mess.py so this file runs on its own ---
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

# --- this slide ---
class Transaction(TxBase):
    def __exit__(self, exc_type, exc, tb):
        try:
            if exc_type is None:
                self.conn.commit()
            else:
                rollback_quietly(self.conn)
        finally:
            self.pool.release(self.conn)
        return False
