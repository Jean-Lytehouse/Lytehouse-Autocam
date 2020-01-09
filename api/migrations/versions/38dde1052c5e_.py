"""empty message

Revision ID: 38dde1052c5e
Revises: 351c26992f23
Create Date: 2019-01-23 19:56:29.948294

"""

# revision identifiers, used by Alembic.
revision = '38dde1052c5e'
down_revision = 'c8d762cf6784'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    event = op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('event_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['app_user.id'] ),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'] ),
    sa.PrimaryKeyConstraint('id')
    )

    ### end Alembic commands ###
    op.bulk_insert(event,
    [
        {
            'id': 1,
            'name': 'indaba 2019',
            'description': """ The Deep Learning Indaba 2019, Kenyatta University, Nairobi, Kenya """,
            'start_date': '25 August 2019',
            'end_date': '31 August 2019'
        }
    ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event_role')    
    op.drop_table('event')
    # ### end Alembic commands ###
