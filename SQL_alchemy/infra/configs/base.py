from sqlalchemy.orm import registry
mapper_registy = registry()
Base = mapper_registy.generate_base()