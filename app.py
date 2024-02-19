from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

pages = {
    1: "Page 1",
    2: "Page 2",
    3: "Page 3",
    4: "Page 4",
    5: "Page 5",
    6: "Page 6",
    7: "Page 7",
    8: "Page 8",
    9: "Page 9",
    10: "Page 10"
}

group_ids = {
    "developers": 1,
    "analytics": 2
}

group_permissions = {
    1: None, 
    2: None   
}

class GroupPermission(BaseModel):
    read: bool = False
    create: bool = False
    delete: bool = False
    update: bool = False

@app.get("/groups/{group_id}/permissions")
def get_group_permissions(group_id:int):
    if group_id not in group_ids.values():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    if group_permissions[group_id] is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permissions for the group have not been set yet")
    permission=group_permissions[group_id]
    return {"group_id":group_id,"group_permission":permission}

@app.post("/groups/{group_id}/permissions")
def set_group_permission(group_id: int, permission: GroupPermission):
    if group_id not in group_ids.values():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    group_permissions[group_id] = permission
    return {
        "message": f"Permissions updated successfully for group with ID {group_id}",
        "group_permission":permission
            }

@app.put("/groups/{group_id}/permissions")
def update_group_permission(group_id: int, permission: GroupPermission):
    if group_id not in group_ids.values():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    if group_permissions[group_id] is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permissions for the group have not been set yet")
    group_permissions[group_id] = permission
    return {
        "message": f"Permissions updated successfully for group with ID {group_id}",
        "group_permission":permission
            }

@app.delete("/groups/{group_id}/permissions")
def delete_group_permission(group_id: int):
    if group_id not in group_ids.values():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    if group_permissions[group_id] is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permissions for the group have not been set yet")
    group_permissions[group_id]=None
    return {"message": f"Permissions deleted successfully for group with ID {group_id}"}
