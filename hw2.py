# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 10:37:56 2016

@author: arvil
"""

#Compares two words and outputs sentence counts for September 2016

import logging
import mediacloud, datetime

mc = mediacloud.api.MediaCloud('e0ca07461a0f1fb81d96d5584ab9ddc02bed9978581a0a770dd9b3ce75b0d82f')

def CountSentences():
    
    phrase1 = raw_input("Enter first word: ")
    phrase2 = raw_input("Enter second word: ")
    
    logging.basicConfig(filename='example.log',level=logging.INFO)
    logging.info('succes', phrase1, phrase2)
    
    SentCount1 = mc.sentenceCount(phrase1, solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 10, 1) ), 'tags_id_media:1' ])
    SentCount2 = mc.sentenceCount(phrase2, solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 10, 1) ), 'tags_id_media:1' ])
    
    print SentCount1['count'] # prints the number of sentences found
    print SentCount2['count'] # prints the number of sentences found
    
    logging.info(SentCount1,SentCount2)

CountSentences()