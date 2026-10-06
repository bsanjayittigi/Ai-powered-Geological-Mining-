"""
OreSight Authentication & RBAC APIs
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from backend.app.services.mock_data import DEMO_USERS

router = APIRouter(prefix="/auth", tags=["Authentication"])

class LoginRequest(BaseModel):
    employee_id: str
    password: str
    remember_me: Optional[bool] = False

class UserResponse(BaseModel):
    id: str
    employee_id: str
    full_name: str
    role: str
    organization: str
    subsidiary: str
    department: str
    email: str
    token: str

@router.post("/login")
def login(req: LoginRequest):
    # Match user by employee_id or fallback to first user
    user = None
    for u in DEMO_USERS:
        if u["employee_id"].lower() == req.employee_id.strip().lower():
            user = u
            break

    if not user:
        # Allow default guest/demo login
        user = DEMO_USERS[0]

    return {
        "status": "success",
        "user": user,
        "token": f"oresight-jwt-token-{user['employee_id']}-valid",
        "message": f"Welcome back, {user['full_name']} ({user['role']})"
    }

@router.get("/users")
def get_users():
    return DEMO_USERS
