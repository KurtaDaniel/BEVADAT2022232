import pandas as pd

class NJCleaner():
    def __init__(self, path = "2018_03.csv") -> None:
        self.data = pd.read_csv(path)
        

    def order_by_scheduled_time(self) -> pd.DataFrame:
        ret = self.data.sort_values(by=["scheduled_time"])
        return ret

    def drop_columns_and_nan(self) -> pd.DataFrame:
        ret = self.data.drop(columns=["to","from"])
        ret = ret.dropna()
        return ret

    def convert_date_to_day(self) -> pd.DataFrame:
        ret = self.data.copy()
        ret["day"] = pd.to_datetime(self.data["date"]).dt.day_name()
        ret = ret.drop(columns=["date"])
        return ret
    
    def convert_scheduled_time_to_part_of_the_day(self) -> pd.DataFrame:
        ret = self.data.copy()
        
        ret["tmp"] = pd.to_datetime(self.data["scheduled_time"])
        ret["part_of_the_day"] = "a"
        i = 0

        night = pd.to_datetime("20:00:00").to_pydatetime().time()
        evening = pd.to_datetime("16:00:00").to_pydatetime().time()
        afternoon = pd.to_datetime("12:00:00").to_pydatetime().time()
        morning = pd.to_datetime("08:00:00").to_pydatetime().time()
        early_morning = pd.to_datetime("04:00:00").to_pydatetime().time()

        for item in ret["tmp"]:

            #print(item)
            
           # print(item.to_pydatetime().time())
           # print(pd.to_datetime("04:00:00").to_pydatetime().time())
            if(item.to_pydatetime().time() >= night):
                #print("night")
                ret.iat[i, 12] = "night"
            elif(item.to_pydatetime().time() >= evening):
                #print("evening")
                ret.iat[i, 12] = "evening"
            elif(item.to_pydatetime().time() >= afternoon):
                #print("afternoon")
                ret.iat[i, 12] = "afternoon"
            elif(item.to_pydatetime().time() >= morning):
                #print("morning")
                ret.iat[i, 12] = "morning"
            elif(item.to_pydatetime().time() >= early_morning ):
                #print("early_morning")
                ret.iat[i, 12] = "early_morning"
            else:
                #print("late_night")
                ret.iat[i,12] = "late_night"
            
            i+=1

            """""
            if(i<100000):
                i+=1
            else:
                break
            """
        ret = ret.drop(columns=["tmp"])    
        #print(ret["part_of_the_day"])
        return ret
        
    def convert_delay(self) -> pd.DataFrame:
        ret = self.data.copy()
        ret["delay"] = [1 if x >= 5 else 0 for x in ret["delay_minutes"]]
        
        return ret

    def drop_unnecessary_columns(self) -> pd.DataFrame:
        ret = self.data.drop(columns=["train_id", "scheduled_time","actual_time","delay_minutes"],axis=1, errors='ignore')
        return ret

    def save_first_60k(self, path = "data/NJ.csv") -> None:
        self.data.head(60000).to_csv(path,index=False)
        
    def prep_df(self, path = "data/NJ.csv") -> None:
        self.data = self.order_by_scheduled_time()
        self.data = self.drop_columns_and_nan()
        self.data = self.convert_date_to_day()
        self.data = self.convert_scheduled_time_to_part_of_the_day()
        self.data = self.convert_delay()
        self.data = self.drop_unnecessary_columns()

        self.save_first_60k(path)
        

#c = NJCleaner()
#c.prep_df()
