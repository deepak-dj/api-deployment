"""creating tables

Revision ID: 934482cff6cb
Revises: 
Create Date: 2024-11-09 20:48:11.474939

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '934482cff6cb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('indications',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('diagnosis_code',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('indication_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['indication_id'], ['indications.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('market_basket',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('indication_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['indication_id'], ['indications.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('surgery_code',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('indication_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['indication_id'], ['indications.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('surgery_code')
    op.drop_table('market_basket')
    op.drop_table('diagnosis_code')
    op.drop_table('indications')
    # ### end Alembic commands ###