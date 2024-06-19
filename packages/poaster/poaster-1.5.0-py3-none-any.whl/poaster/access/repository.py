from typing import Protocol

import sqlalchemy.exc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from poaster.core import exceptions, hashing

from . import schemas, tables


class SupportsUserRepository(Protocol):
    """Interface for handling users."""

    async def create(self, user: schemas.UserRegistrationSchema) -> schemas.UserSchema:
        """Create user after validating input schema."""
        ...

    async def update(self, user: schemas.UserRegistrationSchema) -> schemas.UserSchema:
        """Update user after validating input schema."""
        ...

    async def delete(self, username: str) -> None:
        """Delete user."""
        ...

    async def get_all(self) -> list[schemas.UserSchema]:
        """Fetch all users from DB."""
        ...

    async def get_by_username(self, username: str) -> schemas.UserSchema:
        """Fetch by username, raising exception if not found."""
        ...


class SqlalchemyUserRepository:
    """Implementation of the user repository with SqlAlchemy."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, user: schemas.UserRegistrationSchema) -> schemas.UserSchema:
        entry = tables.User(
            **user.model_dump(exclude={"password"}),
            password=hashing.pwd_context.hash(user.password),
        )
        self._session.add(entry)
        try:
            await self._session.commit()
        except sqlalchemy.exc.IntegrityError as err:
            await self._session.rollback()
            raise exceptions.AlreadyExists(f"User {user.username!r} exists.") from err
        else:
            return schemas.UserSchema.model_validate(entry)

    async def update(self, user: schemas.UserRegistrationSchema) -> schemas.UserSchema:
        qry = select(tables.User).where(tables.User.username == user.username).limit(1)
        result = await self._session.execute(qry)
        try:
            db_user = result.scalars().one()
        except sqlalchemy.exc.NoResultFound as err:
            raise exceptions.DoesNotExist(
                f"User {user.username!r} does not exist."
            ) from err

        db_user.password = hashing.pwd_context.hash(user.password)
        await self._session.commit()
        return schemas.UserSchema.model_validate(db_user)

    async def delete(self, username: str) -> None:
        qry = select(tables.User).where(tables.User.username == username).limit(1)
        result = await self._session.execute(qry)
        try:
            db_user = result.scalars().one()
        except sqlalchemy.exc.NoResultFound as err:
            raise exceptions.DoesNotExist(f"User {username!r} does not exist.") from err
        else:
            await self._session.delete(db_user)
            await self._session.commit()

    async def get_all(self) -> list[schemas.UserSchema]:
        results = await self._session.execute(select(tables.User))
        return [schemas.UserSchema.model_validate(res) for res in results.scalars()]

    async def get_by_username(self, username: str) -> schemas.UserSchema:
        qry = select(tables.User).where(tables.User.username == username).limit(1)
        result = await self._session.execute(qry)

        try:
            user = result.scalars().one()
        except sqlalchemy.exc.NoResultFound as err:
            raise exceptions.DoesNotExist(f"{username!r} does not exist.") from err

        return schemas.UserSchema.model_validate(user)
