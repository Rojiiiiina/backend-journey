from fastapi import FastAPI

app = FastAPI()

#Endpoint 1 - homeroute
@app.get("/")
def home():
    return {"message":"Hello! I am building my backend journey",
            "status":"dai 1 complete"
            }
    
#Endpoint 2 - about me
@app.get("/about") 
def about():
    return {
        "name" : "Rojina Mishra",
        "goal" : "Become an AI engineer",
        "current_foucs" : "Backend development with Python",
        "location" : "Kathmandu, Nepal"
        }   
    
#Endpoint 3 - skills
@app.get("/skills")
def skills():
    return {
        "programming_languages" : ["Python", "FastAPI", "PostgreSQL"],
        "days into journey" : 1,
        "target_job" : "Junior Backend Developer"
    }