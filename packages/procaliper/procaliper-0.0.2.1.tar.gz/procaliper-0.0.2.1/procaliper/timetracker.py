import time

class timer:
    
    is_on = False
    start_time = 0
    time_chunks = []
    
    
    def __init__(self, start_on = False):
        if start_on:
            self.start()
    
    def start(self):
        if self.is_on == False:
            self.is_on = True
            self.start_time = time.time()
            
    
    def stop(self):
        if self.is_on == True:
            self.time_chunks.append(time.time() - self.start_time)
            self.is_on = False
    
    def get_time_passed(self):
        return sum(self.time_chunks)
        
    def get_chunks(self):
        return self.time_chunks
        
    def print_total_time(self):
        self.print_time(self.get_time_passed())
        
    def print_last_chunk(self):
        if len(self.time_chunks) > 0:
            self.print_time(self.time_chunks[-1])
        
    # Prints time passed from a start and end time.
    def print_time(self, elapsed_time_secs):
        # Print Time
        if elapsed_time_secs < 60:
            print(f"Elapsed time : {elapsed_time_secs:.1f} seconds")
        elif elapsed_time_secs < 3600:
            elapsed_time_minutes = elapsed_time_secs / 60
            print(f"Elapsed time : {elapsed_time_minutes:.1f} minutes")
        else:
            elapsed_time_hours = elapsed_time_secs / 3600
            print(f"Elapsed time : {elapsed_time_hours:.1f} hours")
