# Create your views here.
import pprint
from django.shortcuts import render_to_response
from twitter import TwitterError
from overlaps.AccessAPI.Compare import Compare


def home(request):
    return render_to_response('overlaps/home.html')


def twitter_compare(request):
    print request.GET
    twitter_name_1 = request.GET.get('twitter_name_one', '')
    twitter_name_2 = request.GET.get('twitter_name_two', '')

    allow_cached = True
    user_allowing_cache = request.GET.get('allow_cache', '')
    print user_allowing_cache
    if user_allowing_cache is not '':
        allow_cached = False

    compare = Compare()
    try:
        u1_ids, u2_ids, commons, cached = compare.get_matches(twitter_name_1, twitter_name_2, allow_cached)
        u1_followed_by, u2_followed_by, commons_followed_by, cached_followed_by = compare.get_follower_matches(twitter_name_1, twitter_name_2, allow_cached)

        full_text = 'Commonalities between {} and {} : {} / ({}) / {}'.format(twitter_name_1, twitter_name_2, len(u1_ids), len(commons), len(u2_ids))
        # text_1 = '{} : {}'.format(twitter_name_1, float(len(commons))/len(u1_ids))
        # text_2 = '{} : {}'.format(twitter_name_2, float(len(commons))/len(u2_ids))

        followed_by_full = 'Commonalities between {} and {} : {} / ({}) / {}'.format(twitter_name_1, twitter_name_2, len(u1_followed_by), len(commons_followed_by), len(u2_followed_by))
        # followed_text_1 = '{} : {}'.format(twitter_name_1, float(len(commons_followed_by))/len(u1_followed_by))
        # followed_text_2 = '{} : {}'.format(twitter_name_2, float(len(commons_followed_by))/len(u2_followed_by))

        cache_used = False
        if cached or cached_followed_by:
            cache_used = True

        return render_to_response('twitter_compare.html', {
            'twitter_name_one': twitter_name_1,
            'twitter_name_two': twitter_name_2,
            'full': full_text,
            # 't1': text_1,
            # 't2': text_2,
            't1_size': len(u1_ids),
            't2_size': len(u2_ids),
            'commons_size': len(commons),
            't1_following_percent': '{0:.2f}'.format(float(len(commons))/len(u1_ids) * 100),
            't2_following_percent': '{0:.2f}'.format(float(len(commons))/len(u2_ids) * 100),
            'followed_full': followed_by_full,
            # 'followed_t1': followed_text_1,
            # 'followed_t2': followed_text_2,
            'followed_t1_size': len(u1_followed_by),
            'followed_t2_size': len(u2_followed_by),
            'followed_commons_size': len(commons_followed_by),
            't1_followed_percent': '{0:.2f}'.format(float(len(commons_followed_by))/len(u1_followed_by) * 100),
            't2_followed_percent': '{0:.2f}'.format(float(len(commons_followed_by))/len(u2_followed_by) * 100),
            'cached': cache_used
        })

    except TwitterError as t:
        # print t
        # rate = compare.api.GetRateLimitStatus()

        return render_to_response('twitter_error.html', {
            'error': t
            # 'rate': pprint.pformat(rate)
        })