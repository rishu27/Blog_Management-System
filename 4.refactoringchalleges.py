from fastapi import FastAPI, HTTPException

app = FastAPI()

def validate_password(password: str):
    """Validate that the password meets requirements."""
    if len(password) < 8:
        raise HTTPException(status_code=400, detail="Password too short")

def validate_email(email: str):
    """Validate the email format."""
    if "@" not in email:
        raise HTTPException(status_code=400, detail="Invalid email")

@app.post("/users/")
async def create_user(name: str, email: str, password: str):
    validate_password(password)  # Use the validation function
    validate_email(email)        # Use the email validation function
    return {"name": name, "email": email}

@app.put("/users/")
async def update_user(name: str, email: str, password: str):
    validate_password(password)  # Use the validation function
    validate_email(email)        # Use the email validation function
    return {"name": name, "email": email}