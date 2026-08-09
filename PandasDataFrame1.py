import pandas as pd

def main():
   Data = {
       "Name":["sagar","amit","pooja"],
       "Age":[27,28,25],
       "City":["pune","kolhapur","satara"]
   }
   print(Data)
   print(type(Data))

   print(Data["Name"])
    
if __name__=="__main__":
    main()