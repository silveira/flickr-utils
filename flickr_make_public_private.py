#!/usr/bin/env python

import flickrapi

api_key = u''
api_secret = u''
user = u''

if __name__ == "__main__":
  flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
  flickr.authenticate_via_browser(perms='write')

  results = flickr.photos.search(user_id=user, privacy_filter=1)
  page = 1
  total = results[u'photos'][u'total']
  pages = results[u'photos'][u'pages']
  print 'total', total

  while page <= pages:
    for photo in results[u'photos'][u'photo']:
      print flickr.photos.setPerms(photo_id=photo[u'id'], is_public=0, is_friend=0, is_family=0)
    page = page + 1
    results = flickr.photos.search(user_id=user, privacy_filter=1, page=page)

