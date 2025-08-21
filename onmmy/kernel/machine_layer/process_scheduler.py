class ProcessScheduler:
    def schedule(self, steps):
        # naive FIFO scheduler
        for s in steps:
            yield s
