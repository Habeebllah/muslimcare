from app.models import *
from user.models import *

def extra(request):
    services = Services.objects.all()
    news_category = Category.objects.all().order_by('created_at')
    top_quote = Top_Quote.objects.filter().first()
    logo = Logo.objects.filter().first()
    event = Event.objects.filter(approval=True)[:5]
    popular_news = News.objects.filter(status='Published', approval=True).order_by('-created_at')[:3]
    footertexts = FooterTexts.objects.filter().first()
    
    return{'footertexts': footertexts, 'popular_news': popular_news ,'event': event, 'services': services, 'news_category': news_category, 'top_quote': top_quote, 'logo': logo}