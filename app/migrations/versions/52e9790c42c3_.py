"""empty message

Revision ID: 52e9790c42c3
Revises: 03499836b261
Create Date: 2024-01-22 09:12:19.361137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52e9790c42c3'
down_revision = '03499836b261'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sweet', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=False)
        batch_op.alter_column('updated_at',
               existing_type=sa.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=False)

    with op.batch_alter_table('vendor', schema=None) as batch_op:
        batch_op.alter_column('create_at',
               existing_type=sa.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=False)
        batch_op.alter_column('update_at',
               existing_type=sa.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=False)

    with op.batch_alter_table('vendor_sweet', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=False)
        batch_op.alter_column('updated_at',
               existing_type=sa.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vendor_sweet', schema=None) as batch_op:
        batch_op.alter_column('updated_at',
               existing_type=sa.DateTime(),
               type_=sa.TIMESTAMP(),
               existing_nullable=False)
        batch_op.alter_column('created_at',
               existing_type=sa.DateTime(),
               type_=sa.TIMESTAMP(),
               existing_nullable=False)

    with op.batch_alter_table('vendor', schema=None) as batch_op:
        batch_op.alter_column('update_at',
               existing_type=sa.DateTime(),
               type_=sa.TIMESTAMP(),
               existing_nullable=False)
        batch_op.alter_column('create_at',
               existing_type=sa.DateTime(),
               type_=sa.TIMESTAMP(),
               existing_nullable=False)

    with op.batch_alter_table('sweet', schema=None) as batch_op:
        batch_op.alter_column('updated_at',
               existing_type=sa.DateTime(),
               type_=sa.TIMESTAMP(),
               existing_nullable=False)
        batch_op.alter_column('created_at',
               existing_type=sa.DateTime(),
               type_=sa.TIMESTAMP(),
               existing_nullable=False)

    # ### end Alembic commands ###
