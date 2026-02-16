import requests
def coin_price(coin,currency):

    url="https://api.coingecko.com/api/v3/simple/price"

    params={
        "ids":coin,"vs_currencies":currency
    }
    try:
        response=requests.get(url,params=params)
        data=response.json()
    except:
        print("Network error try again")
        return

    if response.status_code!=200:
        print("error connecting to api")
        return
 
  
    
    if coin not in data:
        print("invalid coin name try again")
        return
     
    price=data[coin][currency]

    print(f"{coin.capitalize()} price in {currency.upper()}:{price:,}")

def main():
   
 
  while True:
   choice=(input("1.check crypto price\n2.Exit\nenter choice:-"))
   if(choice == "1"):
        coin=input("enter coin name:-").lower()
        currency=input("enter type of currency:-")
        coin_price(coin,currency)
        
   elif(choice == "2"):
       print("you exited")
       break
   else:
       print("invalid choice")
       
       


if __name__=="__main__":
    main()