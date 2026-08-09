import pandas as pd

def main():
   Data = {
       "Name":["sagar","amit","pooja"],
       "Age":[27,28,25],
       "City":["pune","kolhapur","satara"]
   }

   dobj = pd.DataFrame(Data)

   print(dobj)

   #print(dobj[0])  Not Allowed

   print(dobj["Age"])
    
if __name__=="__main__":
    main()
