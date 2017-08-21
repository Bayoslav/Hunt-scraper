
import bs4 as bs
from rest_framework import viewsets
from . import serializers
# Create your views here.
import requests
from . import skillcraper
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
def poyy(offset):
  content = []

  link = 'https://www.freelancer.com/ajax/directory/getFreelancer.php?' + offset
  #hourly_rate_min=20&hourly_rate_max=30&online_only=true'
  r = requests.get(link)
  dt = r.json()
  ab = dt.get('users')
  for i in ab:
      usernm = (i.get('username'))
      rating = (i.get('freelancer_reputation'))
      country = (i.get('country'))
      rate = (i.get('hourlyrate'))
      bodytxt = (i.get('about'))
      photosrc = (i.get('logo_url'))
      urlic = 'https://www.freelancer.com/u/' + usernm
      dict = {
          'usernm' : usernm,
          'rating' : rating,
          'url' : urlic,
          'photosrc' : photosrc,
          'ratephr' : rate,
          'bodytxt' : bodytxt,
          'country' : country
          }
      content.append(dict)
  return(content)
class Table(APIView):
    jobcont = []
    def get(self,request):
        jobdt = skillcraper.printJobs()
        return Response(jobdt)





class Freelancer(APIView):


  def get(self, request, offset, format=None):
        """
        Return a list of all users.
        """
        kdata = poyy(offset)
        # usernames = ['blab']
        return Response(kdata)
