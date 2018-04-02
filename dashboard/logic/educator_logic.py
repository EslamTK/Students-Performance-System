from .unit_of_work import UnitOfWork

unit_of_work = UnitOfWork()


def get_educator_info(educator_id):
    educator = unit_of_work.educators.get_one(educator_id)
    educator_info = {
        'id': educator.user_id,
        'name': educator.name,
        'image_url': educator.image_url,
        'title': educator.title,
        'email': educator.email,
        'about_me': educator.about_me
    }
    return educator_info


def get_educator_accounts(educator_id):
    accounts = unit_of_work.educators_accounts.get_educator_accounts(educator_id)
    educator_accounts = []
    for i in accounts:
        account = {
            'account_url': i.url,
            'id': i.account.id,
            'name': i.account.name,
            'logo_url': i.account.logo_url
        }
        educator_accounts.append(account)
    return educator_accounts


def get_review_items():
    items = unit_of_work.review_items.get_all()

    review_items = []
    for i in items:
        item = {
            'id': i.id,
            'name': i.name
        }
        review_items.append(item)

    return review_items


"""
add review

    student = unit_of_work.students.get_one(user=user)
    educator = unit_of_work.educators.get_one(user_1)

    review = StudentReview(student=student, educator=educator, content='zay al fol')
    review.save()
    review_x = unit_of_work.review_items.get_all().first()
    review_item = StudentReviewItem(student_review=review, review_item=review_x, rate=3)
    review_item.save()

"""

"""
result = unit_of_work.students_review_items.get_educator_rating(educator=educator)
"""
