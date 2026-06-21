from fastapi import FastAPI
from password_service import fetch , create_pass , fetch_all
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,           # Set to True if handling cookies/sessions
    allow_methods=["*"],              # Ensures OPTIONS, POST, GET, etc. are allowed
    allow_headers=["*"],
)

@app.get("/health")
def home():
    return {
        'Response' : 'Running...',
        'Succes' : True
    }

#  Get: Get password from saved list 
@app.get('/fetch-password')
async def recall(website_name:str): # Query parameter 
    decypered_pass = fetch(website_name)
    return {
       'website_name' : website_name,
        'decryped' : decypered_pass,
        'succes' : True
    }
# Post: Create a new password and store it into password list
@app.post('/create-password')
async def create(site_input:str, pass_len:int):

    generated_pass = create_pass(pass_len, site_input)
    return {
        'generated' : generated_pass,
        'response' : 'Creating Password',
        'succes' : True
    }
# Put: Change or update a saved password 
@app.put('/change-password')
def change():
    return {
        'Response' : 'Changing Password',
        'Succes' : True
    }
# Delete: Delete a saved password 
@app.delete('/delete-password')
def delete():
    return {
        'Response' : 'Deleting Password',
        'Succes' : True
    }

#  Get: Get password from saved list 
@app.get('/password-library')
async def fetch_web(): # Query parameter 
    websites = fetch_all()
    return {
       'websites' : websites,
        'succes' : True
    }