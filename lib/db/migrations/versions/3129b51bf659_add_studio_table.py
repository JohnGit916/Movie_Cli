"""Add Studio table

Revision ID: 3129b51bf659
Revises: c18edcd4931c
Create Date: 2025-06-01 17:09:09.588868

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3129b51bf659'
down_revision: Union[str, None] = 'c18edcd4931c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create studios table
    op.create_table(
        'studios',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Add studio_id column and foreign key using batch mode
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('studio_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_movies_studio_id',  # <-- Explicit constraint name
            'studios',
            ['studio_id'],
            ['id']
        )


def downgrade() -> None:
    # Drop foreign key and column using batch mode
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.drop_constraint('fk_movies_studio_id', type_='foreignkey')
        batch_op.drop_column('studio_id')

    # Drop studios table
    op.drop_table('studios')
