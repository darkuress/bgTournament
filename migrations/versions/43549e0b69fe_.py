"""empty message

Revision ID: 43549e0b69fe
Revises: d84db99c7646
Create Date: 2020-08-09 05:54:09.871972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43549e0b69fe'
down_revision = 'd84db99c7646'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('posted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'posted')
    # ### end Alembic commands ###
