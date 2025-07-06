from fastapi import Request

class AddClothe:
    async def post(self, request: Request):
        return {"message": "Look at THIS! You are awesome!"}
