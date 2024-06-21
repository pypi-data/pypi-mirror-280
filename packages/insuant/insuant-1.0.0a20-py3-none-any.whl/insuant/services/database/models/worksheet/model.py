from sqlmodel import Field, SQLModel, String, Integer, Boolean


class Worksheet(SQLModel, table=True, table_name="worksheet"):
    id: int = Field(default=None, primary_key=True, index=True)  # Auto-generated integer ID
    title: str = Field(index=True)
    description: str = Field(index=True)
    owner_id: int = Field(index=True)
    is_active: bool = Field(default=True)
