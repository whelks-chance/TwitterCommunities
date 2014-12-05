# Create your views here.
from django.shortcuts import render_to_response
from overlaps.AccessAPI.Compare import Compare


def home(request):
    return render_to_response('overlaps/home.html')


def twitter_compare(request):
    twitter_name_1 = request.GET.get('twitter_name_one', '')
    twitter_name_2 = request.GET.get('twitter_name_two', '')

    compare = Compare()
    u1_ids, u2_ids, commons = compare.get_matches(twitter_name_1, twitter_name_2)

    full_text = 'Commonalities between {} and {} : {} / ({}) / {}'.format(twitter_name_1, twitter_name_2, len(u1_ids), len(commons), len(u2_ids))
    text_1 = '{} : {}'.format(twitter_name_1, float(len(commons))/len(u1_ids))
    text_2 = '{} : {}'.format(twitter_name_2, float(len(commons))/len(u2_ids))


    return render_to_response('twitter_compare.html', {
        'twitter_name_one': twitter_name_1,
        'twitter_name_two': twitter_name_2,
        'full': full_text,
        't1': text_1,
        't2': text_2
    })