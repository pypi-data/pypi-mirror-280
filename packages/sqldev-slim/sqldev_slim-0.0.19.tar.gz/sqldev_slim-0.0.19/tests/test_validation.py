from typing import Optional

import pytest
from pydantic.error_wrappers import ValidationError
from sqldev import SQLDev

from .conftest import needs_pydanticv1, needs_pydanticv2


@needs_pydanticv1
def test_validation_pydantic_v1(clear_sqldev):
    """Test validation of implicit and explicit None values.

    # For consistency with pydantic, validators are not to be called on
    # arguments that are not explicitly provided.

    https://github.com/khulnasoft/sqldev/issues/230
    https://github.com/samuelcolvin/pydantic/issues/1223

    """
    from pydantic import validator

    class Hero(SQLDev):
        name: Optional[str] = None
        secret_name: Optional[str] = None
        age: Optional[int] = None

        @validator("name", "secret_name", "age")
        def reject_none(cls, v):
            assert v is not None
            return v

    Hero.validate({"age": 25})

    with pytest.raises(ValidationError):
        Hero.validate({"name": None, "age": 25})


@needs_pydanticv2
def test_validation_pydantic_v2(clear_sqldev):
    """Test validation of implicit and explicit None values.

    # For consistency with pydantic, validators are not to be called on
    # arguments that are not explicitly provided.

    https://github.com/khulnasoft/sqldev/issues/230
    https://github.com/samuelcolvin/pydantic/issues/1223

    """
    from pydantic import field_validator

    class Hero(SQLDev):
        name: Optional[str] = None
        secret_name: Optional[str] = None
        age: Optional[int] = None

        @field_validator("name", "secret_name", "age")
        def reject_none(cls, v):
            assert v is not None
            return v

    Hero.model_validate({"age": 25})

    with pytest.raises(ValidationError):
        Hero.model_validate({"name": None, "age": 25})
