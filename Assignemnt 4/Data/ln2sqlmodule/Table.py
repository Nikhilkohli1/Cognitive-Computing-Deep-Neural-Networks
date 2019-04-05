# -*- coding: utf-8 -*

import sys
import unicodedata
import settings

reload(sys)
sys.setdefaultencoding("utf-8")

from Column import Column

class Table:
    name = ''
    columns = []
    primary_keys = []
    foreign_keys = []
    
    def __init__(self, name=None, columns=None, primary_keys=None):

        if name is None:
            self.name = ''
        else:
            self.name = name
        
        if columns is None:
            self.columns = []
        else:
            self.columns = columns
        
        if primary_keys is None:
            self.primary_keys = []
        else:
            self.primary_keys = primary_keys
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_number_of_columns(self):
        return len(self.columns)
    
    def get_columns(self):
        return self.columns

    def add_column(self, column_name, column_type):
        self.columns.append(Column(column_name, column_type))

    def get_number_of_primary_keys(self):
        return len(self.primary_keys)

    def get_primary_keys(self):
        return self.primary_keys

    def add_primary_key(self, primary_key):
        if settings.DEBUG:
            print '%s : primary key added:%s' % (self.name, primary_key)
        self.primary_keys.append(primary_key)

    def get_number_of_foreign_keys(self):
        return len(self.foreign_keys)

    def get_foreign_keys(self):
        return self.foreign_keys

    def add_foreign_key(self, col, ref_table, ref_col):
        if settings.DEBUG:
            print 'foreign key added : %s.%s->%s.%s' % (self.name, col, ref_table, ref_col)
        self.foreign_keys.append({'col':col,'ref_table':ref_table,'ref_col':ref_col})


