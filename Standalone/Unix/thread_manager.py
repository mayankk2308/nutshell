import threading

class thread_manager(object):

    # off-main thread execution
    # background_thread must be joined manually
    # execute asynchronously after join
    def background_exec(self, operation, *args):
        background_thread = threading.Thread(target=operation, args=args)
        background_thread.start()
        return background_thread
