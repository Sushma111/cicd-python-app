from fastapi import FASTAPI
app = FASTAPI()
users = []
@app.get("/")
def home():
    return{"message":"User service running"}
@app.post("/users")
def create_user(name :str):
    users.append(name)
    return{"message":f"user {name} added"}
@app.get("/users")
def get_users():
    return {"users": users}




