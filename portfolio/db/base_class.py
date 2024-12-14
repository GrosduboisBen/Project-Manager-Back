from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: any
    __name__: str

    # To automatically generate __tablename__ if not defined in the model
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
