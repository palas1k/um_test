"""fix table

Revision ID: 132c4a3e914f
Revises: e547a9c87121
Create Date: 2024-10-24 22:56:47.411398

"""
import os

import sqlalchemy as sa
from alembic import context
from alembic import op
from loguru import logger

from src.config import get_config


# revision identifiers, used by Alembic.
revision = '132c4a3e914f'
down_revision = 'e547a9c87121'

cfg = get_config()

def upgrade():
    op.execute('CREATE SCHEMA IF NOT EXISTS __alembic_schema')
    op.execute('CREATE SCHEMA IF NOT EXISTS ege_schema')

    schema_upgrades()
    # x-flag for data
    if context.get_x_argument(as_dictionary=True).get("data", None):
        data_upgrades()

    logger.info("Migration complete [OK]")


def downgrade():
    data_downgrades()
    schema_downgrades()

def schema_upgrades():
    """schema upgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'score', ['telegram_id'], schema='ege_schema')
    # ### end Alembic commands ###

def schema_downgrades():
    """schema downgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'score', schema='ege_schema', type_='unique')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass