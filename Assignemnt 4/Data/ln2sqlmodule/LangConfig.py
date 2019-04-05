# -*- coding: utf-8 -*

import sys, re
import unicodedata

reload(sys)
sys.setdefaultencoding("utf-8")

class LangConfig:

	def __init__(self):
		self.avg_keywords = []
		self.sum_keywords = []
		self.max_keywords = []
		self.min_keywords = []
		self.count_keywords = []
		self.junction_keywords = []
		self.disjunction_keywords = []
		self.greater_keywords = []
		self.less_keywords = []
		self.between_keywords = []
		self.order_by_keywords = []
		self.group_by_keywords = []
		self.negation_keywords = []

	def get_avg_keywords(self):
		return self.avg_keywords

	def get_sum_keywords(self):
		return self.sum_keywords

	def get_max_keywords(self):
		return self.max_keywords

	def get_min_keywords(self):
		return self.min_keywords

	def get_count_keywords(self):
		return self.count_keywords

	def get_junction_keywords(self):
		return self.junction_keywords

	def get_disjunction_keywords(self):
		return self.disjunction_keywords

	def get_greater_keywords(self):
		return self.greater_keywords

	def get_less_keywords(self):
		return self.less_keywords

	def get_between_keywords(self):
		return self.between_keywords

	def get_order_by_keywords(self):
		return self.order_by_keywords

	def get_group_by_keywords(self):
		return self.group_by_keywords

	def get_negation_keywords(self):
		return self.negation_keywords

	def remove_accents(self, string):
		nkfd_form = unicodedata.normalize('NFKD', unicode(string))
		return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

	def load(self, path):
		with open(path) as f:
			content = f.readlines()
			self.avg_keywords = map(self.remove_accents, map(str.strip, content[0].replace(':',',').split(",")))
			self.avg_keywords = self.avg_keywords[1:len(self.avg_keywords)]
			self.sum_keywords = map(self.remove_accents, map(str.strip, content[1].replace(':',',').split(",")))
			self.sum_keywords = self.sum_keywords[1:len(self.sum_keywords)]
			self.max_keywords = map(self.remove_accents, map(str.strip, content[2].replace(':',',').split(",")))
			self.max_keywords = self.max_keywords[1:len(self.max_keywords)]
			self.min_keywords = map(self.remove_accents, map(str.strip, content[3].replace(':',',').split(",")))
			self.min_keywords = self.min_keywords[1:len(self.min_keywords)]
			self.count_keywords = map(self.remove_accents, map(str.strip, content[4].replace(':',',').split(",")))
			self.count_keywords = self.count_keywords[1:len(self.count_keywords)]
			self.junction_keywords = map(self.remove_accents, map(str.strip, content[5].replace(':',',').split(",")))
			self.junction_keywords = self.junction_keywords[1:len(self.junction_keywords)]
			self.disjunction_keywords = map(self.remove_accents, map(str.strip, content[6].replace(':',',').split(",")))
			self.disjunction_keywords = self.disjunction_keywords[1:len(self.disjunction_keywords)]
			self.greater_keywords = map(self.remove_accents, map(str.strip, content[7].replace(':',',').split(",")))
			self.greater_keywords = self.greater_keywords[1:len(self.greater_keywords)]
			self.less_keywords = map(self.remove_accents, map(str.strip, content[8].replace(':',',').split(",")))
			self.less_keywords = self.less_keywords[1:len(self.less_keywords)]
			self.between_keywords = map(self.remove_accents, map(str.strip, content[9].replace(':',',').split(",")))
			self.between_keywords = self.between_keywords[1:len(self.between_keywords)]
			self.order_by_keywords = map(self.remove_accents, map(str.strip, content[10].replace(':',',').split(",")))
			self.order_by_keywords = self.order_by_keywords[1:len(self.order_by_keywords)]
			self.group_by_keywords = map(self.remove_accents, map(str.strip, content[11].replace(':',',').split(",")))
			self.group_by_keywords = self.group_by_keywords[1:len(self.group_by_keywords)]
			self.negation_keywords = map(self.remove_accents, map(str.strip, content[12].replace(':',',').split(",")))
			self.negation_keywords = self.negation_keywords[1:len(self.negation_keywords)]

	def print_me(self):
		if settings.DEBUG :
			print self.avg_keywords
			print self.sum_keywords
			print self.max_keywords
			print self.min_keywords
			print self.count_keywords
			print self.junction_keywords
			print self.disjunction_keywords
			print self.greater_keywords
			print self.less_keywords
			print self.between_keywords
			print self.order_by_keywords
			print self.group_by_keywords
			print self.negation_keywords
        