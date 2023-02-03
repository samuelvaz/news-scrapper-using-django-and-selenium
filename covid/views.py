from django.shortcuts import render
from .scrapper import *
from django.views import View

class HomeView(View):
	template_name = 'home.html'


	def get(self , request):

		headlines = get_headline()
		bot = Coronavirus()
		data = bot.get_data()
		context = {
			'headlines':headlines,
			'deaths_1': data['death_1'],
			'recovered_1':data['recovered_1'],
			'total_1': data['total_1'],
			'deaths_2': data['death_2'],
			'recovered_2': data['recovered_2'],
			'total_2': data['total_2'],

		}
		
		return render(request, self.template_name, context )