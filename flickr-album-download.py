#!/usr/bin/env python

import flickrapi
import math

api_key = u''
api_secret = u''
user = u''
photo_set = u''

PAGE_SIZE = 500

def generate_download_list():
  photos = flickr.photosets.getPhotos(photoset_id=photo_set, user_id=user)
  total = photos[u'photoset'][u'total']
  pages_necessary = int(math.ceil(float(total)/PAGE_SIZE))

  for current_page in xrange(pages_necessary):
    photos = flickr.photosets.getPhotos(photoset_id=photo_set, user_id=user, page=current_page+1, extras='url_o')
    for photo in photos[u'photoset'][u'photo']:
      print photo['url_o'] 

if __name__ == "__main__":
  flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
  flickr.authenticate_via_browser(perms='read')
  generate_download_list()

