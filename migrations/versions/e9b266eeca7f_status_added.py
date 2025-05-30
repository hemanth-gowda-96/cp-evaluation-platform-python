"""status added

Revision ID: e9b266eeca7f
Revises: 
Create Date: 2025-05-06 00:02:59.647401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9b266eeca7f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question_papers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('file_name', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('status', sa.String(length=255), nullable=False))
        batch_op.alter_column('paper_id',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.create_unique_constraint(None, ['paper_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question_papers', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('paper_id',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.drop_column('status')
        batch_op.drop_column('file_name')
        batch_op.drop_column('id')

    # ### end Alembic commands ###
