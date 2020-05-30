from DigitalProfile.celery import app
from profile.Parser import analysis_user, get_user_id,get_keywords,get_tags


@app.task
def get_user_skills(vk_id):
    path = '/home/sergeybildin/Рабочий стол/DigitalProfile/DigitalProfile/DigitalProfile/apps/profile/keyword.txt'
    skills = analysis_user(get_user_id(vk_id),get_keywords(path),get_tags(path))
    return skills