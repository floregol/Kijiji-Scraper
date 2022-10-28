import sched, time
if __name__=="__main__":
    
    
    s = sched.scheduler(time.time, time.sleep)
    def do_something(sc): 
        exec(open("launcher.py").read())

        # do your stuff
        sc.enter(10, 1, do_something, (sc,))

    s.enter(10, 1, do_something, (s,))
    s.run()
    