from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: any
    __name__: str

    # Génère automatiquement __tablename__ si non défini dans le modèle
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
