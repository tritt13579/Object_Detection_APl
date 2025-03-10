"""Initial migration

Revision ID: 68bf3d9a05de
Revises: 
Create Date: 2025-03-08 16:12:02.782957

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68bf3d9a05de'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('version', sa.String(), nullable=True),
    sa.Column('filename', sa.String(), nullable=True),
    sa.Column('original_filename', sa.String(), nullable=True),
    sa.Column('model_metadata', sa.String(), nullable=True),
    sa.Column('upload_time', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('uploader', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('filename'),
    sa.UniqueConstraint('name', 'version', name='unique_name_version')
    )
    op.create_index(op.f('ix_models_id'), 'models', ['id'], unique=False)
    op.create_index(op.f('ix_models_name'), 'models', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_models_name'), table_name='models')
    op.drop_index(op.f('ix_models_id'), table_name='models')
    op.drop_table('models')
    # ### end Alembic commands ###
