from DigitalProfile.celery import app
from profile.Parser import analysis_user, get_user_id,get_keywords,get_tags
from profile.models import Profile
from account.models import Account


@app.task
def get_user_skills(user,vk_id):
    path = '/home/sergeybildin/Рабочий стол/DigitalProfile/DigitalProfile/DigitalProfile/apps/profile/keyword.txt'
    account = Account.objects.get(email=user)
    accunt_id = account.id
    obj = Profile.objects.get(user=account.id)
    obj.skills = set(analysis_user(get_user_id(vk_id),get_keywords(path),get_tags(path)))
    obj.save()
    
    

    