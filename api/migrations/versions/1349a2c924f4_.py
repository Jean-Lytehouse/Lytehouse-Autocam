"""empty message

Revision ID: 1349a2c924f4
Revises: 8a1468838847
Create Date: 2019-03-26 15:24:11.894634

"""

# revision identifiers, used by Alembic.
revision = '1349a2c924f4'
down_revision = '8a1468838847'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    review_form_table = table(
        'review_form',
        column('id', sa.Integer()),
        column('application_form_id', sa.Integer()),
        column('is_open', sa.Boolean()),
        column('deadline', sa.DateTime())
    )
    op.bulk_insert(
        review_form_table,
        [
            {
                'id': 1,
                'application_form_id': 1,
                'is_open': True,
                'deadline': '10 May 2019'
            }
        ]
    )

    review_question_table = table(
        'review_question',
        sa.Column('id', sa.Integer()),
        sa.Column('review_form_id', sa.Integer()),
        sa.Column('question_id', sa.Integer()),
        sa.Column('description', sa.String()),
        sa.Column('headline', sa.String()),
        sa.Column('type', sa.String()),
        sa.Column('placeholder', sa.String()),
        sa.Column('options', sa.JSON()),
        sa.Column('is_required', sa.Boolean()),
        sa.Column('order', sa.Integer()),
        sa.Column('validation_regex', sa.String()),
        sa.Column('validation_text', sa.String()),
        sa.Column('weight', sa.Float())
    )
    op.bulk_insert(
        review_question_table,
        [
            {
                'id': 1,
                'review_form_id': 1,
                'question_id': None,
                'headline': 'Encourage field of study?',
                'description': 'Is the applicant from a field of study we want to encourage? ie outside of CS/Maths/Stats?',
                'type': 'checkbox',
                'options': None,
                'is_required': False,
                'order': 1,
                'weight': 0
            },
            {
                'id': 2,
                'review_form_id': 1,
                'question_id': 1,
                'headline': None,
                'description': None,
                'type': 'multi-choice',
                'options': [
                    {'label': 'Poor', 'value': 0},
                    {'label': 'Below Average', 'value': 1},
                    {'label': 'Average', 'value': 2},
                    {'label': 'Above Average', 'value': 3},
                    {'label': 'Excellent', 'value': 4}
                ],
                'is_required': True,
                'order': 2,
                'weight': 0
            },
            {
                'id': 3,
                'review_form_id': 1,
                'question_id': 2,
                'headline': None,
                'description': None,
                'type': 'multi-choice',
                'options': [
                    {'label': 'Poor', 'value': 0},
                    {'label': 'Below Average', 'value': 1},
                    {'label': 'Average', 'value': 2},
                    {'label': 'Above Average', 'value': 3},
                    {'label': 'Excellent', 'value': 4}
                ],
                'is_required': True,
                'order': 3,
                'weight': 0
            },
            {
                'id': 4,
                'review_form_id': 1,
                'question_id': 3,
                'headline': None,
                'description': None,
                'type': 'multi-choice',
                'options': [
                    {'label': 'Poor', 'value': 0},
                    {'label': 'Below Average', 'value': 1},
                    {'label': 'Average', 'value': 2},
                    {'label': 'Above Average', 'value': 3},
                    {'label': 'Excellent', 'value': 4}
                ],
                'is_required': True,
                'order': 4,
                'weight': 0
            },
            {
                'id': 5,
                'review_form_id': 1,
                'question_id': 4,
                'headline': None,
                'description': 'Based on this answer, do you believe the applicant has been a tutor for a relevant course?',
                'type': 'multi-choice',
                'options': [
                    {'label': 'Poor', 'value': 0},
                    {'label': 'Below Average', 'value': 1},
                    {'label': 'Average', 'value': 2},
                    {'label': 'Above Average', 'value': 3},
                    {'label': 'Excellent', 'value': 4}
                ],
                'is_required': True,
                'order': 5,
                'weight': 0
            },
            {
                'id': 6,
                'review_form_id': 1,
                'question_id': 5,
                'headline': None,
                'description': None,
                'type': 'multi-choice',
                'options': [
                    {'label': 'Poor', 'value': 0},
                    {'label': 'Below Average', 'value': 1},
                    {'label': 'Average', 'value': 2},
                    {'label': 'Above Average', 'value': 3},
                    {'label': 'Excellent', 'value': 4}
                ],
                'is_required': True,
                'order': 6,
                'weight': 0
            },
            {
                'id': 7,
                'review_form_id': 1,
                'question_id': 15,
                'headline': None,
                'description': None,
                'type': 'information',
                'options': None,
                'is_required': False,
                'order': 7,
                'weight': 0
            },
            {
                'id': 8,
                'review_form_id': 1,
                'question_id': 16,
                'headline': None,
                'description': None,
                'type': 'multi-choice',
                'options': [
                    {'label': 'Poor', 'value': 0},
                    {'label': 'Below Average', 'value': 1},
                    {'label': 'Average', 'value': 2},
                    {'label': 'Above Average', 'value': 3},
                    {'label': 'Excellent', 'value': 4}
                ],
                'is_required': False,
                'order': 8,
                'weight': 0
            },
            {
                'id': 9,
                'review_form_id': 1,
                'question_id': 8,
                'headline': None,
                'description': None,
                'type': 'information',
                'options': None,
                'is_required': False,
                'order': 9,
                'weight': 0
            },
            {
                'id': 10,
                'review_form_id': 1,
                'question_id': 11,
                'headline': None,
                'description': None,
                'type': 'information',
                'options': None,
                'is_required': False,
                'order': 10,
                'weight': 0
            },
            {
                'id': 11,
                'review_form_id': 1,
                'question_id': 9,
                'headline': None,
                'description': None,
                'type': 'multi-choice',
                'options': [
                    {'label': 'Poor', 'value': 0},
                    {'label': 'Below Average', 'value': 1},
                    {'label': 'Average', 'value': 2},
                    {'label': 'Above Average', 'value': 3},
                    {'label': 'Excellent', 'value': 4}
                ],
                'is_required': False,
                'order': 11,
                'weight': 0
            },
            {
                'id': 12,
                'review_form_id': 1,
                'question_id': 17,
                'headline': None,
                'description': None,
                'type': 'information',
                'options': None,
                'is_required': False,
                'order': 12,
                'weight': 0
            },
            {
                'id': 13,
                'review_form_id': 1,
                'question_id': 18,
                'headline': None,
                'description': None,
                'type': 'information',
                'options': None,
                'is_required': False,
                'order': 13,
                'weight': 0
            },
            {
                'id': 14,
                'review_form_id': 1,
                'question_id': None,
                'headline': 'Final Verdict',
                'description': 'Do you think this applicant should attend the Indaba?',
                'type': 'multi-choice',
                'options': [
                    {'label': 'No', 'value': 0},
                    {'label': 'Maybe', 'value': 1},
                    {'label': 'Yes', 'value': 2}
                ],
                'is_required': True,
                'order': 14,
                'weight': 0
            }
        ]
    )

    op.get_bind().execute("""SELECT setval('review_question_id_seq', (SELECT max(id) FROM review_question));""")
    op.get_bind().execute("""SELECT setval('review_form_id_seq', (SELECT max(id) FROM review_form));""")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.get_bind().execute('DELETE FROM review_question WHERE id <= 14; DELETE FROM review_form WHERE id = 1;')
    op.get_bind().execute("""SELECT setval('review_question_id_seq', (SELECT max(id) FROM review_question));""")
    op.get_bind().execute("""SELECT setval('review_form_id_seq', (SELECT max(id) FROM review_form));""")
    # ### end Alembic commands ###
