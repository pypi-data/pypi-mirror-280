import time
from datetime import timedelta

class Interval:
    '''Format: HH:mm:ss
    '''
    def __init__(self,hours:int=0, minutes:int=0, seconds:int=0) -> None:
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
    def __repr__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

class Chronometer:
    def __init__(self) -> None:
        self.reset()
    def start(self)->None:
        '''Start the stopwatch
        '''
        self.reset()
        self.__start_time = time.time()
    def stop(self)->None:
        '''End stopwatch
        '''
        self.__end_time = time.time()
    def reset(self)->None:
        '''Set the stopwatch to zero
        '''
        self.__start_time=0
        self.__end_time=0
    def get_elapsed_time(self,interval_format:bool=True)->Interval|timedelta:
        '''Description
        :return Interval(str): HH:mm:ss format supported for inserting records into databases and adding elapsed times

        ## Example
        ```Python
        from datetime import timedelta
        from jaanca_chronometer import Chronometer
        import time

        if __name__=="__main__":
            chronometer=Chronometer()

            print(f"date_time format or interval format: {chronometer.get_format_time()}")

            chronometer.start()
            time.sleep(1)
            chronometer.stop()
            elapsed_time=str(chronometer.get_elapsed_time())
            print(f"type[str]:{elapsed_time}")

            chronometer.start()
            time.sleep(2)
            chronometer.stop()
            elapsed_time=str(chronometer.get_elapsed_time())
            print(f"type[str]:{elapsed_time}")

            chronometer.start()
            time.sleep(3)
            chronometer.stop()
            elapsed_time:timedelta=chronometer.get_elapsed_time(interval_format=False)
            print(f"type[timedelta] to insert into databases like PostgreSQL:{elapsed_time}")
            print(f"timedelta[seconds]:{elapsed_time.seconds}")
        ´´´
        '''
        elapsed_seconds = self.__end_time - self.__start_time
        hours = int(elapsed_seconds / 3600)
        minutes = int((elapsed_seconds % 3600) / 60)
        seconds = int(elapsed_seconds % 60)
        if interval_format:
            return Interval(hours, minutes, seconds)
        else:
            hours, minutes, seconds = map(int, str(Interval(hours, minutes, seconds)).split(':'))
            return timedelta(hours=hours, minutes=minutes, seconds=seconds)

    def get_format_time(self)->str:
        return "HH:mm:ss"

    @classmethod
    def parse_elapsed_time(self,elapsed_time:str="00:00:00")->timedelta:
        try:
            hours, minutes, seconds = map(int,str(elapsed_time).split(":"))
            return timedelta(hours=hours, minutes=minutes, seconds=seconds)
        except:
            return timedelta(hours=0, minutes=0, seconds=0)