# coding=utf-8
import codecs
import json
import os
import random
import time
from gensim_utils import lda_utils
from wechat_analyzer import TaggingUtils
from wechat_analyzer.TaggingUtils import passage_first_level_classify

import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'jayvee'


def classify_text_files(files_root_path, result_path):
    flist = os.listdir(files_root_path)
    for f in flist:
        print f
        ftext = codecs.open('%s/%s' % (files_root_path, f), 'r').read()
        try:
            json_obj = json.loads(ftext)
            result = passage_first_level_classify(json_obj['post_content'])
        except Exception, e:  # 懒得差各种异常了，直接重复
            print e
            continue
        try:
            fout = codecs.open('%s/%s/%s' % (result_path, result, f), 'w')
        except Exception, e:
            print e
            os.mkdir('%s/%s' % (result_path, result))
            fout = codecs.open('%s/%s/%s' % (result_path, result, f), 'w')
        fout.write(ftext)
        time.sleep(random.random())
    print 'done'


def train_lda_among_classify(class_path, model_outpath, num_topics=15, iterations=200, passes=20, is_tfidf=False):
    lda_model = lda_utils.train_model_by_rootpath(class_path, num_topics=num_topics, iterations=iterations,
                                                  passes=passes, is_tfidf=is_tfidf)
    lda_model.save(model_outpath)
    lda_model.print_topics()


if __name__ == '__main__':
    # classify_text_files(u'../wechat_crawler/crawl_data/大象公会', './wechat_data/daxiang_result')

    class_type = '军事'
    train_lda_among_classify('./wechat_data/daxiang_result/%s' % class_type,
                             './wechat_data/lda_in_daxiang/%s.model' % class_type, num_topics=10)
    lm = lda_utils.loda_ldamodel_by_file('./wechat_data/lda_in_daxiang/%s.model' % class_type)
    for i in lm.print_topics(num_topics=20):
        print i

        # test_text = open('./wechat_data/sample.txt', 'r').read()
        # TaggingUtils.passage_second_level_classify(test_text)