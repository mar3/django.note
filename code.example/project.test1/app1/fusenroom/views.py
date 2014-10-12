# coding: utf-8

import sys
import codecs
import django
import uuid
import json
import logging
import subprocess
import datetime
import time
import inspect
import project1
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext
from app1.utils import *
from app1.form import *
from django.contrib.auth.decorators import login_required

# Create your views here.

logger = logging.getLogger(__name__)


def _enum_fusen_elements():

	return FusenManager().all()

@login_required
def default(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# デフォルトページのアクション
	#
	#
	# *************************************************************************
	# *************************************************************************
	# *************************************************************************

	# logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> $$$ start $$$');

	# =========================================================================
	# setup
	# =========================================================================

	# =========================================================================
	# validation
	# =========================================================================

	# =========================================================================
	# process
	# =========================================================================
	
	# =========================================================================
	# contents
	# =========================================================================

	# logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');

	fields = {}

	fields['window_title'] = 'ふせん部屋'

	fields['form'] = {
		'fusen_elements': _enum_fusen_elements()
	}

	util.fill_menu_items(request, fields)
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('fusenroom/default.html')
	return django.http.HttpResponse(template.render(context))

def elements(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# 付箋を返す API みたいな例
	#
	#
	# *************************************************************************
	# *************************************************************************
	# *************************************************************************

	# =========================================================================
	# setup
	# =========================================================================

	# =========================================================================
	# validation
	# =========================================================================

	# =========================================================================
	# process
	# =========================================================================

	# =========================================================================
	# contents
	# =========================================================================
	items = []
	for e in _enum_fusen_elements():
		items.append(e.as_dict())
	response = {
		'time': str(datetime.datetime.now()),
		'fusen_elements': items
	}

	return django.http.HttpResponse(json.dumps(response, indent=4))