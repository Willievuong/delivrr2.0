from models.Account import Account
from app import app 


user = Account(firstName="Will", lastName="Vuong", age="12")


@app.route('/')
def Hello():
    return user
  
print(user.firstName)
    
# if __name__ == '__main__':
#   app.run()

