import time
start_time = time.time()
# your script
elapsed_time = time.time() - start_time
print 'elapsed time (hh:mm:ss): ', time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
