from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: any
    __name__: str

    # Generate __tablename__ if not defined in models
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
